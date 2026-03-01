#!/usr/bin/env python3
"""
Git-Flow Skill - Workflow Orchestration
Provides gate-based workflow with role-based branching, review/approval gates,
phase tracking, and reversible approvals. Delegates git operations to git-manage.
"""

import argparse
import json
import os
import sys
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
from enum import Enum
from pipeline_manager import PipelineUpdateManager

# Import shared git command utility
sys.path.insert(0, str(Path(__file__).parent.parent / 'utils'))
from git_command import (
    run_git_command,
    get_current_branch,
    validate_branch_name,
    GitCommandError,
    GitCommandTimeout
)
from file_lock import write_locked_json, read_locked_json, FileLockError
from schema_validator import validate_workflow_state, validate_branch_state, SchemaValidationError


class BranchStatus(Enum):
    PENDING = "pending"
    REVIEWING = "reviewing"
    APPROVED = "approved"
    MERGED = "merged"
    UNAPPROVED = "unapproved"
    REVERTED = "reverted"
    NEEDS_CHANGES = "needs_changes"
    REJECTED = "rejected"


class PhaseStatus(Enum):
    PENDING = "pending"
    ACTIVE = "active"
    COMPLETE = "complete"
    BLOCKED = "blocked"


class WorkflowStatus(Enum):
    INITIALIZED = "initialized"
    IN_PROGRESS = "in_progress"
    COMPLETE = "complete"
    PAUSED = "paused"


class ReviewEvent:
    def __init__(self, action: str, actor: str, comment: Optional[str] = None, 
                 reason: Optional[str] = None, merge_commit: Optional[str] = None):
        self.action = action
        self.actor = actor
        self.timestamp = datetime.now().isoformat()
        self.comment = comment
        self.reason = reason
        self.merge_commit = merge_commit
    
    def to_dict(self) -> Dict:
        return {
            "action": self.action,
            "actor": self.actor,
            "timestamp": self.timestamp,
            "comment": self.comment,
            "reason": self.reason,
            "merge_commit": self.merge_commit
        }


class BranchState:
    def __init__(self, name: str, role: str, phase: int):
        self.name = name
        self.role = role
        self.status = BranchStatus.PENDING
        self.phase = phase
        self.created_at = datetime.now().isoformat()
        self.commits: List[Dict] = []
        self.merge_commit: Optional[str] = None
        self.approved_by: Optional[str] = None
        self.approved_at: Optional[str] = None
        self.unapproved_by: Optional[str] = None
        self.unapproved_at: Optional[str] = None
        self.dependencies: List[str] = []
        self.dependents: List[str] = []
        self.review_history: List[Dict] = []
    
    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "role": self.role,
            "status": self.status.value,
            "phase": self.phase,
            "created_at": self.created_at,
            "commits": self.commits,
            "merge_commit": self.merge_commit,
            "approved_by": self.approved_by,
            "approved_at": self.approved_at,
            "unapproved_by": self.unapproved_by,
            "unapproved_at": self.unapproved_at,
            "dependencies": self.dependencies,
            "dependents": self.dependents,
            "review_history": self.review_history
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'BranchState':
        branch = cls(data["name"], data["role"], data["phase"])
        branch.status = BranchStatus(data["status"])
        branch.created_at = data["created_at"]
        branch.commits = data.get("commits", [])
        branch.merge_commit = data.get("merge_commit")
        branch.approved_by = data.get("approved_by")
        branch.approved_at = data.get("approved_at")
        branch.unapproved_by = data.get("unapproved_by")
        branch.unapproved_at = data.get("unapproved_at")
        branch.dependencies = data.get("dependencies", [])
        branch.dependents = data.get("dependents", [])
        branch.review_history = data.get("review_history", [])
        return branch


class Phase:
    def __init__(self, name: str, role: str, order: int, required: bool):
        self.name = name
        self.role = role
        self.order = order
        self.required = required
        self.status = PhaseStatus.PENDING
        self.branch: Optional[str] = None
        self.dependencies: List[int] = []
        self.started_at: Optional[str] = None
        self.completed_at: Optional[str] = None
    
    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "role": self.role,
            "order": self.order,
            "required": self.required,
            "status": self.status.value,
            "branch": self.branch,
            "dependencies": self.dependencies,
            "started_at": self.started_at,
            "completed_at": self.completed_at
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Phase':
        phase = cls(data["name"], data["role"], data["order"], data["required"])
        phase.status = PhaseStatus(data["status"])
        phase.branch = data.get("branch")
        phase.dependencies = data.get("dependencies", [])
        phase.started_at = data.get("started_at")
        phase.completed_at = data.get("completed_at")
        return phase


class WorkflowState:
    def __init__(self, feature: str):
        self.feature = feature
        self.status = WorkflowStatus.INITIALIZED
        self.current_phase = 0
        self.phases: List[Phase] = []
        self.branches: Dict[str, BranchState] = {}
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
    
    def to_dict(self) -> Dict:
        return {
            "feature": self.feature,
            "status": self.status.value,
            "current_phase": self.current_phase,
            "phases": [p.to_dict() for p in self.phases],
            "branches": {k: v.to_dict() for k, v in self.branches.items()},
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'WorkflowState':
        workflow = cls(data["feature"])
        workflow.status = WorkflowStatus(data["status"])
        workflow.current_phase = data.get("current_phase", 0)
        workflow.phases = [Phase.from_dict(p) for p in data.get("phases", [])]
        workflow.branches = {k: BranchState.from_dict(v) for k, v in data.get("branches", {}).items()}
        workflow.created_at = data.get("created_at", datetime.now().isoformat())
        workflow.updated_at = data.get("updated_at", datetime.now().isoformat())
        return workflow


class DependencyGraph:
    def __init__(self):
        self.graph: Dict[str, List[str]] = {}
        self.reverse_graph: Dict[str, List[str]] = {}
    
    def add_dependency(self, branch: str, depends_on: List[str]):
        if branch not in self.graph:
            self.graph[branch] = []
        if branch not in self.reverse_graph:
            self.reverse_graph[branch] = []
        
        self.graph[branch].extend(depends_on)
        for dep in depends_on:
            if dep not in self.reverse_graph:
                self.reverse_graph[dep] = []
            self.reverse_graph[dep].append(branch)
    
    def get_dependents(self, branch: str) -> List[str]:
        return self.reverse_graph.get(branch, [])
    
    def get_all_dependents(self, branch: str) -> List[str]:
        dependents = []
        visited = set()
        
        def traverse(b: str):
            if b in visited:
                return
            visited.add(b)
            
            for dep in self.get_dependents(b):
                dependents.append(dep)
                traverse(dep)
        
        traverse(branch)
        return dependents


class GitFlow:
    def __init__(self, repo_root: Optional[Path] = None):
        self.repo_root = repo_root or Path.cwd()
        self.skill_dir = self.repo_root / '.iflow' / 'skills' / 'git-flow'
        self.config_file = self.skill_dir / 'config.json'
        self.phases_file = self.skill_dir / 'phases.json'
        self.workflow_state_file = self.skill_dir / 'workflow-state.json'
        self.branch_states_file = self.skill_dir / 'branch-states.json'
        self.git_manage_path = self.skill_dir / '..' / 'git-manage' / 'git-manage.py'
        
        self.load_config()
        self.load_phases()
        self.workflow_state: Optional[WorkflowState] = None
        self.dependency_graph = DependencyGraph()
        self.load_workflow_state()
        self.load_branch_states()
        self.pipeline_update_manager = PipelineUpdateManager('git-flow', self.skill_dir)
    
    def load_config(self):
        default_config = {
            "workflow": {
                "auto_detect_role": True,
                "auto_create_branch": True,
                "auto_phase_transition": True,
                "require_all_phases": False,
                "allow_parallel_phases": False,
                "phases_file": None
            },
            "merge": {
                "strategy": "rebase-merge",
                "delete_branch_after_merge": True,
                "require_dependencies_merged": True
            },
            "unapproval": {
                "allow_unapprove_after_merge": True,
                "default_action": "cascade-revert",
                "require_cascade_confirmation": True,
                "preserve_branch_after_revert": True,
                "auto_create_fix_branch": False
            },
            "notifications": {
                "enabled": True,
                "on_approve": True,
                "on_reject": True,
                "on_phase_change": True
            },
            "git_manage": {
                "command_path": ".iflow/skills/git-manage/git-manage.py"
            },
            "branch_protection": {
                "protected_branches": ["main", "master", "production"]
            }
        }
        
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    user_config = json.load(f)
                    self.config = self._merge_config(default_config, user_config)
            except (json.JSONDecodeError, IOError):
                self.config = default_config
        else:
            self.config = default_config
    
    def _merge_config(self, default: Dict, user: Dict) -> Dict:
        result = default.copy()
        for key, value in user.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = self._merge_config(result[key], value)
            else:
                result[key] = value
        return result
    
    def load_phases(self):
        default_phases = [
            {"name": "Requirements Gathering", "role": "Client", "order": 1, "required": True},
            {"name": "Architecture Design", "role": "Tech Lead", "order": 2, "required": True},
            {"name": "Implementation", "role": "Software Engineer", "order": 3, "required": True},
            {"name": "Testing", "role": "QA Engineer", "order": 4, "required": True},
            {"name": "Design", "role": "UI/UX Designer", "order": 5, "required": False},
            {"name": "Documentation", "role": "Documentation Specialist", "order": 6, "required": False},
            {"name": "Security Review", "role": "Security Engineer", "order": 7, "required": False},
            {"name": "Deployment", "role": "DevOps Engineer", "order": 8, "required": True}
        ]
        
        phases_file = self.config.get("workflow", {}).get("phases_file")
        if phases_file:
            phases_path = self.skill_dir / phases_file
            if phases_path.exists():
                with open(phases_path, 'r') as f:
                    phases_data = json.load(f)
                    self.phases = [Phase.from_dict(p) for p in phases_data.get("phases", default_phases)]
            else:
                self.phases = [Phase.from_dict(p) for p in default_phases]
        elif self.phases_file.exists():
            with open(self.phases_file, 'r') as f:
                phases_data = json.load(f)
                self.phases = [Phase.from_dict(p) for p in phases_data.get("phases", default_phases)]
        else:
            self.phases = [Phase.from_dict(p) for p in default_phases]
    
    def load_workflow_state(self):
        """Load workflow state with file locking and schema validation."""
        if self.workflow_state_file.exists():
            try:
                data = read_locked_json(self.workflow_state_file)
                
                # Validate against schema
                schema_dir = self.repo_root / '.iflow' / 'schemas'
                is_valid, errors = validate_workflow_state(data, schema_dir)
                
                if not is_valid:
                    print(f"Warning: Workflow state validation failed: {errors}")
                    # Continue loading despite validation errors for backward compatibility
                
                self.workflow_state = WorkflowState.from_dict(data)
            except (json.JSONDecodeError, IOError, FileLockError):
                self.workflow_state = None
    
    def load_branch_states(self):
        """Load branch states with file locking and schema validation."""
        if self.workflow_state and self.branch_states_file.exists():
            try:
                data = read_locked_json(self.branch_states_file)
                
                # Validate against schema
                schema_dir = self.repo_root / '.iflow' / 'schemas'
                
                for branch_name, branch_data in data.items():
                    is_valid, errors = validate_branch_state(branch_data, schema_dir)
                    
                    if not is_valid:
                        print(f"Warning: Branch state validation failed for {branch_name}: {errors}")
                        # Continue loading despite validation errors for backward compatibility
                    
                    branch = BranchState.from_dict(branch_data)
                    self.workflow_state.branches[branch_name] = branch
            except (json.JSONDecodeError, IOError, FileLockError):
                pass
    
    def save_workflow_state(self):
        """Save workflow state with file locking."""
        if self.workflow_state:
            self.workflow_state.updated_at = datetime.now().isoformat()
            try:
                write_locked_json(self.workflow_state_file, self.workflow_state.to_dict())
            except FileLockError as e:
                print(f"Warning: Failed to save workflow state: {e}")
    
    def save_branch_states(self):
        """Save branch states with file locking."""
        if self.workflow_state:
            try:
                write_locked_json(
                    self.branch_states_file,
                    {k: v.to_dict() for k, v in self.workflow_state.branches.items()}
                )
            except FileLockError as e:
                print(f"Warning: Failed to save branch states: {e}")
    
    def run_git_command(self, command: List[str], timeout: Optional[int] = 120) -> Tuple[int, str, str]:
        """Run a git command with timeout handling."""
        try:
            return run_git_command(command, cwd=self.repo_root, timeout=timeout)
        except GitCommandError as e:
            return e.returncode, '', e.message
        except GitCommandTimeout as e:
            return 124, '', str(e)
    
    def run_git_manage(self, args: List[str], timeout: Optional[int] = 120) -> Tuple[int, str, str]:
        """Run git-manage script with timeout handling."""
        git_manage_path = self.config.get("git_manage", {}).get("command_path", ".iflow/skills/git-manage/git-manage.py")
        git_manage_script = self.repo_root / git_manage_path
        
        if not git_manage_script.exists():
            return 1, '', f'git-manage not found at {git_manage_path}'
        
        try:
            result = subprocess.run(
                [sys.executable, str(git_manage_script)] + args,
                cwd=self.repo_root,
                capture_output=True,
                text=True,
                timeout=timeout
            )
            return result.returncode, result.stdout, result.stderr
        except subprocess.TimeoutExpired:
            return 124, '', f'git-manage command timed out after {timeout} seconds'
        except Exception as e:
            return 1, '', str(e)
    
    def get_current_branch(self) -> str:
        """Get current branch name."""
        try:
            return get_current_branch(self.repo_root)
        except Exception:
            return 'unknown'
    
    def is_protected_branch(self, branch: str) -> bool:
        protected = self.config.get("branch_protection", {}).get("protected_branches", ["main", "master"])
        return branch in protected
    
    def detect_role(self) -> str:
        current_branch = self.get_current_branch()
        
        if '/' in current_branch:
            role = current_branch.split('/')[0].replace('-', ' ').title()
            return role
        
        if self.workflow_state and self.workflow_state.current_phase > 0:
            phase = self.workflow_state.phases[self.workflow_state.current_phase - 1]
            return phase.role
        
        return 'Software Engineer'
    
    def to_slug(self, text: str) -> str:
        return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')
    
    def generate_branch_name(self, role: str, feature: str) -> str:
        role_slug = self.to_slug(role)
        feature_slug = self.to_slug(feature)
        short_id = datetime.now().strftime('%H%M%S')
        return f"{role_slug}/{feature_slug}-{short_id}"
    
    def create_branch(self, name: str) -> Tuple[int, str]:
        """Create a new branch with validation."""
        # Validate branch name
        is_valid, error_msg = validate_branch_name(name)
        if not is_valid:
            return 1, f'Invalid branch name: {error_msg}'
        
        code, stdout, stderr = self.run_git_command(['checkout', '-b', name])
        if code == 0:
            return 0, f'Created branch: {name}'
        else:
            return code, f'Failed to create branch: {stderr}'
    
    def start_workflow(self, feature: str) -> Tuple[int, str]:
        if self.workflow_state:
            return 1, 'Workflow already exists. Use status to view current workflow.'
        
        self.workflow_state = WorkflowState(feature)
        self.workflow_state.phases = [Phase.from_dict(p) for p in self.phases]
        self.workflow_state.status = WorkflowStatus.IN_PROGRESS
        
        self.save_workflow_state()
        
        output = [
            f'✓ Workflow initialized',
            f'Feature: {feature}',
            f'Phases: {len(self.phases)}',
            '',
            f'To start Phase 1, use: /git-flow phase next'
        ]
        
        return 0, '\n'.join(output)
    
    def commit(self, files: List[str]) -> Tuple[int, str]:
        if not self.workflow_state:
            return 1, 'No workflow initialized. Use /git-flow start <feature> to begin.'
        
        if self.workflow_state.current_phase == 0:
            return 1, 'No active phase. Use /git-flow phase next to activate the first phase.'
        
        role = self.detect_role()
        current_branch = self.get_current_branch()
        
        if self.is_protected_branch(current_branch):
            if self.config.get("workflow", {}).get("auto_create_branch", True):
                feature = self.workflow_state.feature
                new_branch = self.generate_branch_name(role, feature)
                code, output = self.create_branch(new_branch)
                if code != 0:
                    return code, output
                current_branch = new_branch
            else:
                return 1, f'Cannot commit to protected branch "{current_branch}". Create a feature branch first.'
        
        phase = self.workflow_state.phases[self.workflow_state.current_phase - 1]
        
        if current_branch not in self.workflow_state.branches:
            branch_state = BranchState(current_branch, role, phase.order)
            self.workflow_state.branches[current_branch] = branch_state
        
        code, stdout, stderr = self.run_git_manage(['commit'] + files)
        
        if code == 0:
            branch_state = self.workflow_state.branches[current_branch]
            if current_branch != phase.branch:
                phase.branch = current_branch
            
            output_lines = [
                f'✓ Commit successful',
                f'Branch: {current_branch}',
                f'Role: {role}',
                f'Phase: {phase.order} - {phase.name}',
                '',
                f'{stdout}'
            ]
            return 0, '\n'.join(output_lines)
        else:
            return code, f'Commit failed: {stderr}'
    
    def review(self) -> Tuple[int, str]:
        if not self.workflow_state:
            return 1, 'No workflow initialized.'
        
        pending_branches = [
            b for b in self.workflow_state.branches.values()
            if b.status in [BranchStatus.PENDING, BranchStatus.REVIEWING, BranchStatus.APPROVED]
        ]
        
        if not pending_branches:
            return 0, 'No branches pending review.'
        
        output = [
            '📋 Git-Flow Review Dashboard',
            f'Feature: {self.workflow_state.feature}',
            f'Status: {self.workflow_state.status.value.title()} (Phase {self.workflow_state.current_phase}/{len(self.workflow_state.phases)})',
            '',
            'Pending Reviews:'
        ]
        
        for i, branch in enumerate(pending_branches, 1):
            phase = self.workflow_state.phases[branch.phase - 1]
            status_icon = {
                BranchStatus.PENDING: '⏳',
                BranchStatus.REVIEWING: '👀',
                BranchStatus.APPROVED: '✅'
            }.get(branch.status, '❓')
            
            output.append('')
            output.append(f'[{i}] {branch.name}')
            output.append(f'    Role: {branch.role}')
            output.append(f'    Phase: {branch.order} - {phase.name}')
            output.append(f'    Commits: {len(branch.commits)}')
            output.append(f'    Status: {status_icon} {branch.status.value}')
            output.append(f'    Created: {branch.created_at}')
            
            if branch.commits:
                last_commit = branch.commits[-1]
                output.append(f'    Last commit: {last_commit.get("message", "N/A")}')
        
        output.append('')
        output.append('Actions:')
        output.append('[A] Approve: /git-flow review approve <branch>')
        output.append('[R] Reject: /git-flow review reject <branch> --reason "text"')
        output.append('[C] Request Changes: /git-flow review request-changes <branch> --comment "text"')
        
        return 0, '\n'.join(output)
    
    def review_approve(self, branch_name: str, comment: Optional[str] = None) -> Tuple[int, str]:
        if not self.workflow_state:
            return 1, 'No workflow initialized.'
        
        if branch_name not in self.workflow_state.branches:
            return 1, f'Branch "{branch_name}" not found in workflow.'
        
        branch = self.workflow_state.branches[branch_name]
        
        if branch.status == BranchStatus.MERGED:
            return 1, f'Branch "{branch_name}" is already merged.'
        
        branch.status = BranchStatus.APPROVED
        branch.approved_by = "you"
        branch.approved_at = datetime.now().isoformat()
        
        event = ReviewEvent("approve", "you", comment=comment)
        branch.review_history.append(event.to_dict())
        
        output = [
            f'✓ Approved: {branch_name}',
            ''
        ]
        
        if comment:
            output.append(f'💬 Comment: "{comment}"')
            output.append('')
        
        output.append('Starting merge...')
        
        code, merge_output = self.merge_branch(branch_name)
        
        if code == 0:
            output.append(merge_output)
            
            phase = self.workflow_state.phases[branch.phase - 1]
            if self.check_phase_complete(phase):
                output.append('')
                output.append(f'✓ Phase {phase.order} ({phase.name}) complete!')
                
                if self.config.get("workflow", {}).get("auto_phase_transition", True):
                    next_phase = self.get_next_phase(phase)
                    if next_phase:
                        output.append(self.advance_to_next_phase(phase)[1])
        else:
            output.append(f'❌ Merge failed: {merge_output}')
        
        self.save_branch_states()
        self.save_workflow_state()
        
        return 0, '\n'.join(output)
    
    def merge_branch(self, branch_name: str) -> Tuple[int, str]:
        if not self.workflow_state:
            return 1, 'No workflow initialized.'
        
        branch = self.workflow_state.branches[branch_name]
        
        if self.config.get("merge", {}).get("require_dependencies_merged", True):
            for dep_name in branch.dependencies:
                dep_branch = self.workflow_state.branches.get(dep_name)
                if dep_branch and dep_branch.status != BranchStatus.MERGED:
                    return 1, f'Dependency "{dep_name}" is not merged yet.'
        
        output = []
        
        output.append(f'Step 1: Checkout main...')
        code, stdout, stderr = self.run_git_command(['checkout', 'main'])
        if code != 0:
            return code, f'Failed to checkout main: {stderr}'
        output.append('✓ Checkout main')
        
        output.append(f'Step 2: Pull latest changes...')
        code, stdout, stderr = self.run_git_command(['pull'])
        if code != 0:
            return code, f'Failed to pull: {stderr}'
        output.append('✓ Pull complete')
        
        output.append(f'Step 3: Checkout {branch_name}...')
        code, stdout, stderr = self.run_git_command(['checkout', branch_name])
        if code != 0:
            return code, f'Failed to checkout {branch_name}: {stderr}'
        output.append(f'✓ Checkout {branch_name}')
        
        output.append(f'Step 4: Rebase onto main...')
        code, stdout, stderr = self.run_git_command(['rebase', 'main'])
        if code != 0:
            return code, f'Rebase failed: {stderr}'
        output.append('✓ Rebase complete')
        
        output.append(f'Step 5: Checkout main...')
        code, stdout, stderr = self.run_git_command(['checkout', 'main'])
        if code != 0:
            return code, f'Failed to checkout main: {stderr}'
        output.append('✓ Checkout main')
        
        output.append(f'Step 6: Merge {branch_name}...')
        code, stdout, stderr = self.run_git_command(['merge', '--no-ff', branch_name])
        if code != 0:
            return code, f'Merge failed: {stderr}'
        output.append('✓ Merge complete')
        
        code, stdout, stderr = self.run_git_command(['log', '-1', '--pretty=%H'])
        if code == 0:
            merge_commit = stdout.strip()
            branch.merge_commit = merge_commit
            branch.status = BranchStatus.MERGED
            
            event = ReviewEvent("merge", "you", merge_commit=merge_commit)
            branch.review_history.append(event.to_dict())
        
        if self.config.get("merge", {}).get("delete_branch_after_merge", True):
            output.append(f'Step 7: Delete branch {branch_name}...')
            self.run_git_command(['branch', '-D', branch_name])
            output.append('✓ Branch deleted')
        
        return 0, '\n'.join(output)
    
    def review_reject(self, branch_name: str, reason: str, keep_branch: bool = True) -> Tuple[int, str]:
        if not self.workflow_state:
            return 1, 'No workflow initialized.'
        
        if branch_name not in self.workflow_state.branches:
            return 1, f'Branch "{branch_name}" not found in workflow.'
        
        branch = self.workflow_state.branches[branch_name]
        branch.status = BranchStatus.REJECTED
        
        event = ReviewEvent("reject", "you", reason=reason)
        branch.review_history.append(event.to_dict())
        
        output = [
            f'✓ Rejected: {branch_name}',
            f'❌ Reason: "{reason}"',
            ''
        ]
        
        if keep_branch:
            output.append('⚠ Branch kept for fixes')
        else:
            output.append('🗑 Branch deleted')
            self.run_git_command(['branch', '-D', branch_name])
        
        output.append('')
        output.append('To fix:')
        output.append(f'1. git checkout {branch_name}')
        output.append('2. Make changes')
        output.append('3. /git-flow commit <files>')
        output.append('4. Resubmit for review')
        
        self.save_branch_states()
        
        return 0, '\n'.join(output)
    
    def review_request_changes(self, branch_name: str, comment: str) -> Tuple[int, str]:
        if not self.workflow_state:
            return 1, 'No workflow initialized.'
        
        if branch_name not in self.workflow_state.branches:
            return 1, f'Branch "{branch_name}" not found in workflow.'
        
        branch = self.workflow_state.branches[branch_name]
        branch.status = BranchStatus.NEEDS_CHANGES
        
        event = ReviewEvent("request_changes", "you", comment=comment)
        branch.review_history.append(event.to_dict())
        
        output = [
            f'✓ Changes requested: {branch_name}',
            f'💬 Comment: "{comment}"',
            '',
            f'To fix:')
        output.append(f'1. git checkout {branch_name}')
        output.append('2. Make changes')
        output.append('3. /git-flow commit <files>')
        output.append('4. Resubmit for review')
        
        self.save_branch_states()
        
        return 0, '\n'.join(output)
    
    def unapprove(self, branch_name: str, cascade: bool = False) -> Tuple[int, str]:
        if not self.workflow_state:
            return 1, 'No workflow initialized.'
        
        if branch_name not in self.workflow_state.branches:
            return 1, f'Branch "{branch_name}" not found in workflow.'
        
        branch = self.workflow_state.branches[branch_name]
        
        if branch.status != BranchStatus.MERGED:
            return 1, f'Branch "{branch_name}" is not merged. Use review reject instead.'
        
        if not self.config.get("unapproval", {}).get("allow_unapprove_after_merge", True):
            return 1, 'Unapproval after merge is disabled in configuration.'
        
        output = [
            f'⚠ Unapproving: {branch_name}',
            ''
        ]
        
        if cascade:
            dependents = self.dependency_graph.get_all_dependents(branch_name)
            to_revert = [branch_name] + dependents
            to_revert.sort(key=lambda b: self.workflow_state.branches[b].approved_at or '', reverse=True)
            
            output.append(f'Found {len(to_revert)} branches to revert:')
            for b in to_revert:
                output.append(f'  - {b}')
            output.append('')
            
            for b in to_revert:
                revert_output = self.revert_branch(b)
                output.append(revert_output)
        else:
            revert_output = self.revert_branch(branch_name)
            output.append(revert_output)
        
        output.append('')
        output.append('Next steps:')
        output.append('1. Fix issues in the branch')
        output.append('2. /git-flow commit <files>')
        output.append('3. Resubmit for review')
        
        self.save_branch_states()
        self.save_workflow_state()
        
        return 0, '\n'.join(output)
    
    def revert_branch(self, branch_name: str) -> str:
        if not self.workflow_state:
            return 'No workflow initialized.'
        
        branch = self.workflow_state.branches[branch_name]
        
        output = [
            f'Reverting: {branch_name}',
            ''
        ]
        
        if branch.merge_commit:
            code, stdout, stderr = self.run_git_command(['checkout', 'main'])
            if code != 0:
                return f'Failed to checkout main: {stderr}'
            
            revert_msg = f'Revert "Merge {branch_name}"\n\n" \
                        f"Original approval: {branch.approved_at}\n" \
                        f"Approver: {branch.approved_by}\n" \
                        f"Unapproved at: {datetime.now().isoformat()}"
            
            code, stdout, stderr = self.run_git_command(['revert', '-m', '1', branch.merge_commit, '-m', revert_msg])
            if code != 0:
                return f'Revert failed: {stderr}'
            
            branch.status = BranchStatus.UNAPPROVED
            branch.unapproved_by = "you"
            branch.unapproved_at = datetime.now().isoformat()
            
            event = ReviewEvent("unapprove", "you")
            branch.review_history.append(event.to_dict())
            
            output.append(f'✓ Reverted {branch_name}')
        else:
            output.append(f'⚠ No merge commit found for {branch_name}')
        
        return '\n'.join(output)
    
    def status(self) -> Tuple[int, str]:
        if not self.workflow_state:
            return 1, 'No workflow initialized. Use /git-flow start <feature> to begin.'
        
        output = [
            '📊 Git-Flow Status',
            f'Feature: {self.workflow_state.feature}',
            f'Status: {self.workflow_state.status.value.title()}',
            f'Created: {self.workflow_state.created_at}',
            ''
        ]
        
        output.append(f'Current Phase: {self.workflow_state.current_phase}/{len(self.workflow_state.phases)}')
        output.append('')
        
        for phase in self.workflow_state.phases:
            status_icon = {
                PhaseStatus.PENDING: '⏸',
                PhaseStatus.ACTIVE: '▶️',
                PhaseStatus.COMPLETE: '✅',
                PhaseStatus.BLOCKED: '🚫'
            }.get(phase.status, '❓')
            
            output.append(f'Phase {phase.order}: {phase.name} ({phase.role})')
            output.append(f'  Status: {status_icon} {phase.status.value}')
            
            if phase.branch:
                branch = self.workflow_state.branches.get(phase.branch)
                if branch:
                    output.append(f'  Branch: {phase.branch} ({branch.status.value})')
            
            output.append('')
        
        pending_branches = [
            b for b in self.workflow_state.branches.values()
            if b.status in [BranchStatus.PENDING, BranchStatus.REVIEWING, BranchStatus.APPROVED]
        ]
        
        if pending_branches:
            output.append('Pending Reviews:')
            for branch in pending_branches:
                output.append(f'  - {branch.name} ({branch.status.value})')
            output.append('')
        
        complete_phases = sum(1 for p in self.workflow_state.phases if p.status == PhaseStatus.COMPLETE)
        progress = int((complete_phases / len(self.workflow_state.phases)) * 100)
        output.append(f'Overall Progress: {progress}% ({complete_phases}/{len(self.workflow_state.phases)} phases complete)')
        
        return 0, '\n'.join(output)
    
    def get_next_phase(self, current_phase: Phase) -> Optional[Phase]:
        for phase in self.workflow_state.phases:
            if phase.order == current_phase.order + 1:
                return phase
        return None
    
    def check_phase_complete(self, phase: Phase) -> bool:
        if phase.status != PhaseStatus.ACTIVE:
            return False
        
        if not phase.branch:
            return False
        
        branch = self.workflow_state.branches.get(phase.branch)
        if not branch or branch.status != BranchStatus.MERGED:
            return False
        
        phase.status = PhaseStatus.COMPLETE
        phase.completed_at = datetime.now().isoformat()
        
        return True
    
    def advance_to_next_phase(self, current_phase: Phase) -> Tuple[int, str]:
        next_phase = self.get_next_phase(current_phase)
        
        if not next_phase:
            self.workflow_state.status = WorkflowStatus.COMPLETE
            return 0, '🎉 All phases complete! Workflow finished.'
        
        output = [
            f'✓ Phase {current_phase.order} ({current_phase.name}) complete!',
            ''
        ]
        
        next_phase.status = PhaseStatus.ACTIVE
        next_phase.started_at = datetime.now().isoformat()
        self.workflow_state.current_phase = next_phase.order
        
        role_slug = self.to_slug(next_phase.role)
        feature_slug = self.to_slug(self.workflow_state.feature)
        short_id = datetime.now().strftime('%H%M%S')
        branch_name = f"{role_slug}/{feature_slug}-{short_id}"
        
        next_phase.branch = branch_name
        
        output.append(f'▶️ Phase {next_phase.order} ({next_phase.name}) is now active')
        output.append(f'Role: {next_phase.role}')
        output.append(f'Branch: {branch_name}')
        output.append('')
        output.append(f'To start: git checkout {branch_name}')
        output.append(f'Then: /git-flow commit <files>')
        
        return 0, '\n'.join(output)
    
    def phase_next(self) -> Tuple[int, str]:
        if not self.workflow_state:
            return 1, 'No workflow initialized.'
        
        if self.workflow_state.current_phase == 0:
            return 1, 'No active phase. Use /git-flow phase next to activate the first phase.'
        
        current_phase = self.workflow_state.phases[self.workflow_state.current_phase - 1]
        
        if not self.check_phase_complete(current_phase):
            return 1, f'Phase {current_phase.order} ({current_phase.name}) is not complete yet.'
        
        code, output = self.advance_to_next_phase(current_phase)
        
        self.save_workflow_state()
        
        return code, output
    
    def history(self) -> Tuple[int, str]:
        if not self.workflow_state:
            return 1, 'No workflow initialized.'
        
        output = [
            '📜 Git-Flow History',
            f'Feature: {self.workflow_state.feature}',
            ''
        ]
        
        for branch_name, branch in self.workflow_state.branches.items():
            phase = self.workflow_state.phases[branch.phase - 1]
            output.append(f'Branch: {branch_name}')
            output.append(f'  Role: {branch.role}')
            output.append(f'  Phase: {phase.order} - {phase.name}')
            output.append(f'  Status: {branch.status.value}')
            output.append(f'  Created: {branch.created_at}')
            
            if branch.review_history:
                output.append(f'  Review History:')
                for event in branch.review_history:
                    output.append(f'    - {event["action"]} by {event["actor"]} at {event["timestamp"]}')
                    if event.get("comment"):
                        output.append(f'      Comment: {event["comment"]}')
                    if event.get("reason"):
                        output.append(f'      Reason: {event["reason"]}')
            
            output.append('')
        
        return 0, '\n'.join(output)


def main():
    parser = argparse.ArgumentParser(
        description='Git-Flow Skill - Workflow Orchestration',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    start_parser = subparsers.add_parser('start', help='Start a new workflow')
    start_parser.add_argument('feature', help='Feature name')
    
    commit_parser = subparsers.add_parser('commit', help='Commit changes to current branch')
    commit_parser.add_argument('files', nargs='*', help='Files to commit')
    
    subparsers.add_parser('review', help='Show review dashboard')
    
    approve_parser = subparsers.add_parser('approve', help='Approve and merge a branch')
    approve_parser.add_argument('branch', help='Branch name')
    approve_parser.add_argument('--comment', help='Approval comment')
    
    reject_parser = subparsers.add_parser('reject', help='Reject a branch')
    reject_parser.add_argument('branch', help='Branch name')
    reject_parser.add_argument('--reason', required=True, help='Rejection reason')
    reject_parser.add_argument('--keep-branch', action='store_true', help='Keep branch after rejection')
    
    request_changes_parser = subparsers.add_parser('request-changes', help='Request changes on a branch')
    request_changes_parser.add_argument('branch', help='Branch name')
    request_changes_parser.add_argument('--comment', required=True, help='Comment for changes')
    
    unapprove_parser = subparsers.add_parser('unapprove', help='Unapprove a merged branch')
    unapprove_parser.add_argument('branch', help='Branch name')
    unapprove_parser.add_argument('--cascade', action='store_true', help='Revert all dependent branches')
    
    subparsers.add_parser('status', help='Show workflow status')
    
    subparsers.add_parser('phase-next', help='Advance to next phase')
    
    subparsers.add_parser('history', help='Show review history')
    
    # Pipeline update commands
    check_updates_parser = subparsers.add_parser('check-updates', help='Check for pipeline updates')
    
    update_parser = subparsers.add_parser('update', help='Update pipeline to new version')
    update_parser.add_argument('--to', help='Target version')
    update_parser.add_argument('--dry-run', action='store_true', help='Preview changes without applying')
    
    rollback_parser = subparsers.add_parser('rollback', help='Rollback pipeline to previous version')
    rollback_parser.add_argument('--to', required=True, help='Target version')
    rollback_parser.add_argument('--backup', help='Restore from specific backup')
    
    versions_parser = subparsers.add_parser('versions', help='List available pipeline versions')
    
    backups_parser = subparsers.add_parser('backups', help='List available backups')
    backups_parser.add_argument('--delete', help='Delete specific backup')
    backups_parser.add_argument('--cleanup', type=int, help='Delete old backups keeping N most recent')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 0
    
    git_flow = GitFlow()
    
    if args.command == 'start':
        code, output = git_flow.start_workflow(args.feature)
    elif args.command == 'commit':
        code, output = git_flow.commit(args.files if args.files else [])
    elif args.command == 'review':
        code, output = git_flow.review()
    elif args.command == 'approve':
        code, output = git_flow.review_approve(args.branch, args.comment)
    elif args.command == 'reject':
        code, output = git_flow.review_reject(args.branch, args.reason, args.keep_branch)
    elif args.command == 'request-changes':
        code, output = git_flow.review_request_changes(args.branch, args.comment)
    elif args.command == 'unapprove':
        code, output = git_flow.unapprove(args.branch, args.cascade)
    elif args.command == 'status':
        code, output = git_flow.status()
    elif args.command == 'phase-next':
        code, output = git_flow.phase_next()
    elif args.command == 'history':
        code, output = git_flow.history()
    elif args.command == 'check-updates':
        has_updates, latest = git_flow.pipeline_update_manager.check_for_updates()
        if has_updates:
            code, output = 0, f'Update available: {latest}\nCurrent version: {git_flow.pipeline_update_manager.get_current_version()}'
        else:
            code, output = 0, f'No updates available. Current version: {git_flow.pipeline_update_manager.get_current_version()}'
    elif args.command == 'update':
        target_version = args.to or git_flow.pipeline_update_manager.list_versions()[-1]
        state = git_flow.workflow_state.to_dict() if git_flow.workflow_state else {}
        code, output = git_flow.pipeline_update_manager.update_to_version(target_version, state, args.dry_run)
    elif args.command == 'rollback':
        state = git_flow.workflow_state.to_dict() if git_flow.workflow_state else {}
        code, output = git_flow.pipeline_update_manager.rollback_to_version(args.to, state, args.backup)
    elif args.command == 'versions':
        versions = git_flow.pipeline_update_manager.list_versions()
        current = git_flow.pipeline_update_manager.get_current_version()
        output_lines = ['Available versions:']
        for v in versions:
            marker = ' (current)' if v == current else ''
            output_lines.append(f'  - {v}{marker}')
        code, output = 0, '\n'.join(output_lines)
    elif args.command == 'backups':
        if args.delete:
            success = git_flow.pipeline_update_manager.backup_manager.delete_backup(args.delete)
            if success:
                code, output = 0, f'Deleted backup: {args.delete}'
            else:
                code, output = 1, f'Failed to delete backup: {args.delete}'
        elif args.cleanup:
            deleted = git_flow.pipeline_update_manager.backup_manager.cleanup_old_backups(args.cleanup)
            code, output = 0, f'Cleaned up {deleted} old backups'
        else:
            backups = git_flow.pipeline_update_manager.backup_manager.list_backups()
            output_lines = ['Available backups:']
            for backup in backups:
                output_lines.append(f"  - {backup['backup_id']}")
                output_lines.append(f"    Version: {backup.get('state_version', 'unknown')}")
                output_lines.append(f"    Timestamp: {backup.get('timestamp', 'unknown')}")
            code, output = 0, '\n'.join(output_lines)
    else:
        code, output = 1, f'Unknown command: {args.command}'
    
    print(output)
    return code


if __name__ == '__main__':
    sys.exit(main())
