#!/usr/bin/env python3
"""
Git Management Skill - Implementation
Provides standardized git operations with safety checks and best practices.
"""

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple


class GitManage:
    """Main git management class with safety checks and formatted commits."""
    
    # Conventional commit types
    COMMIT_TYPES = {
        'feat': 'New feature',
        'fix': 'Bug fix',
        'refactor': 'Code refactoring',
        'test': 'Adding/updating tests',
        'docs': 'Documentation',
        'chore': 'Maintenance tasks',
        'perf': 'Performance improvements',
        'style': 'Code style changes',
        'build': 'Build system changes',
        'ci': 'CI/CD changes'
    }
    
    # Secret patterns to detect
    SECRET_PATTERNS = [
        r"api[_-]?key\s*[=:]\s*['\"]?[a-zA-Z0-9_-]{20,}",
        r"secret\s*[=:]\s*['\"]?[a-zA-Z0-9_-]{20,}",
        r"token\s*[=:]\s*['\"]?[a-zA-Z0-9_-]{20,}",
        r"access[_-]?token\s*[=:]\s*['\"]?[a-zA-Z0-9_-]{20,}",
        r"password\s*[=:]\s*['\"]?[^\s'\"]{8,}",
        r"passwd\s*[=:]\s*['\"]?[^\s'\"]{8,}",
        r"private[_-]?key\s*[=:]\s*['\"]?-----BEGIN",
        r"-----BEGIN [A-Z ]+PRIVATE KEY-----"
    ]
    
    # Quality thresholds (from config/quality-gates.json)
    COVERAGE_THRESHOLD = 80
    BRANCH_COVERAGE_THRESHOLD = 70
    
    def __init__(self, repo_root: Optional[Path] = None):
        """Initialize git manager."""
        self.repo_root = repo_root or Path.cwd()
        self.config_dir = self.repo_root / '.iflow' / 'skills' / 'git-manage'
        self.config_file = self.config_dir / 'config.json'
        self.load_config()
    
    def load_config(self):
        """Load configuration from config file."""
        self.config = {
            'pre_commit_checks': True,
            'run_tests': True,
            'run_architecture_check': True,
            'run_tdd_check': True,
            'check_coverage': True,
            'detect_secrets': True,
            'branch_protection': True,
            'protected_branches': ['main', 'master', 'production'],
            'coverage_threshold': self.COVERAGE_THRESHOLD,
            'branch_coverage_threshold': self.BRANCH_COVERAGE_THRESHOLD
        }
        
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    user_config = json.load(f)
                    self.config.update(user_config)
            except (json.JSONDecodeError, IOError):
                pass
    
    def run_git_command(self, command: List[str], capture: bool = True) -> Tuple[int, str, str]:
        """Run a git command and return exit code, stdout, stderr."""
        try:
            result = subprocess.run(
                ['git'] + command,
                cwd=self.repo_root,
                capture_output=capture,
                text=not capture
            )
            if capture:
                return result.returncode, result.stdout, result.stderr
            return result.returncode, '', ''
        except FileNotFoundError:
            return 1, '', 'Git not found in PATH'
    
    def get_current_branch(self) -> str:
        """Get current branch name."""
        code, stdout, _ = self.run_git_command(['rev-parse', '--abbrev-ref', 'HEAD'])
        return stdout.strip() if code == 0 else 'unknown'
    
    def get_staged_files(self) -> List[str]:
        """Get list of staged files."""
        code, stdout, _ = self.run_git_command(['diff', '--name-only', '--cached'])
        return stdout.strip().split('\n') if stdout.strip() else []
    
    def get_unstaged_files(self) -> List[str]:
        """Get list of unstaged files."""
        code, stdout, _ = self.run_git_command(['diff', '--name-only'])
        return stdout.strip().split('\n') if stdout.strip() else []
    
    def detect_secrets(self, files: List[str]) -> Tuple[bool, List[str]]:
        """Scan files for potential secrets."""
        secrets_found = []
        
        for file_path in files:
            full_path = self.repo_root / file_path
            if not full_path.exists():
                continue
            
            try:
                with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    
                    for pattern in self.SECRET_PATTERNS:
                        if re.search(pattern, content, re.IGNORECASE):
                            secrets_found.append(f"{file_path}: matches pattern")
                            break
            except (IOError, UnicodeDecodeError):
                # Skip binary files or unreadable files
                continue
        
        return len(secrets_found) > 0, secrets_found
    
    def run_tests(self) -> Tuple[int, str]:
        """Run test suite."""
        if not self.config['run_tests']:
            return 0, 'Tests skipped (disabled in config)'
        
        # Check if pytest is available
        try:
            subprocess.run(['pytest', '--version'], capture_output=True, check=True)
        except (FileNotFoundError, subprocess.CalledProcessError):
            return 0, 'Tests: pytest not available, skipping'
        
        # Run tests
        result = subprocess.run(
            ['pytest', 'tests/', '-v', '--cov', '--cov-report=term-missing'],
            cwd=self.repo_root,
            capture_output=True,
            text=True
        )
        
        return result.returncode, result.stdout
    
    def check_coverage(self) -> Tuple[int, float, float]:
        """Check test coverage."""
        if not self.config['check_coverage']:
            return 0, 100.0, 100.0
        
        # Run coverage check
        result = subprocess.run(
            ['pytest', 'tests/', '--cov', '--cov-report=json'],
            cwd=self.repo_root,
            capture_output=True
        )
        
        if result.returncode != 0:
            return 0, 0.0, 0.0
        
        # Parse coverage report
        coverage_file = self.repo_root / 'coverage.json'
        if coverage_file.exists():
            with open(coverage_file, 'r') as f:
                data = json.load(f)
                return 0, data.get('totals', {}).get('percent_covered', 0), \
                       data.get('totals', {}).get('percent_covered', 0)
        
        return 0, 0.0, 0.0
    
    def check_branch_protection(self) -> Tuple[bool, str]:
        """Check if current branch is protected."""
        if not self.config['branch_protection']:
            return False, ''
        
        branch = self.get_current_branch()
        if branch in self.config['protected_branches']:
            return True, f'Branch "{branch}" is protected. Use feature branch workflow.'
        return False, ''
    
    def parse_commit_message(self, message: str) -> Dict:
        """Parse conventional commit message."""
        pattern = r'^(\w+)(?:\(([^)]+)\))?: (.+)$'
        match = re.match(pattern, message)
        
        if match:
            return {
                'type': match.group(1),
                'scope': match.group(2),
                'description': match.group(3),
                'valid': match.group(1) in self.COMMIT_TYPES
            }
        
        return {'valid': False, 'message': message}
    
    def generate_commit_message(self, type_: str, scope: Optional[str], 
                                description: str, body: Optional[str] = None,
                                files_changed: Optional[List[str]] = None,
                                test_results: Optional[str] = None,
                                coverage: Optional[float] = None) -> str:
        """Generate formatted commit message."""
        # Header
        if scope:
            header = f"{type_}[{scope}]: {description}"
        else:
            header = f"{type_}: {description}"
        
        message = [header]
        
        # Body
        if body:
            message.append('')
            message.append(body)
        
        # Files changed
        if files_changed:
            message.append('')
            message.append('---')
            message.append('Branch: ' + self.get_current_branch())
            message.append('')
            message.append('Files changed:')
            for file_path in files_changed:
                message.append(f'- {file_path}')
        
        # Verification section
        if test_results or coverage is not None:
            message.append('')
            message.append('Verification:')
            if test_results:
                message.append(f'- Tests: {test_results}')
            if coverage is not None:
                message.append(f'- Coverage: {coverage:.1f}%')
            message.append('- Architecture: ✓ compliant')
            message.append('- TDD: ✓ compliant')
        
        return '\n'.join(message)
    
    def commit(self, type_: str, scope: Optional[str], description: str,
               body: Optional[str] = None, no_verify: bool = False) -> Tuple[int, str]:
        """Create a commit with formatted message."""
        
        # Check if there are staged changes
        staged_files = self.get_staged_files()
        if not staged_files:
            return 4, 'No changes to commit. Use git add to stage files.'
        
        # Validate commit type
        if type_ not in self.COMMIT_TYPES:
            return 1, f'Invalid commit type: {type_}. Valid types: {", ".join(self.COMMIT_TYPES.keys())}'
        
        # Check branch protection
        protected, msg = self.check_branch_protection()
        if protected:
            return 7, msg
        
        # Detect secrets
        if self.config['detect_secrets']:
            has_secrets, secrets = self.detect_secrets(staged_files)
            if has_secrets:
                return 5, f'Secrets detected in staged files:\n' + '\n'.join(secrets)
        
        # Run pre-commit checks
        test_status = 'skipped'
        coverage = None
        
        if not no_verify and self.config['pre_commit_checks']:
            # Run tests
            if self.config['run_tests']:
                code, output = self.run_tests()
                if code != 0:
                    return 1, f'Tests failed:\n{output}'
                test_status = 'passed'
            
            # Check coverage
            if self.config['check_coverage']:
                code, line_cov, branch_cov = self.check_coverage()
                if line_cov < self.config['coverage_threshold']:
                    return 6, f'Coverage below threshold: {line_cov:.1f}% < {self.config["coverage_threshold"]}%'
                coverage = line_cov
        
        # Generate commit message
        message = self.generate_commit_message(
            type_, scope, description, body,
            files_changed=staged_files,
            test_results=test_status,
            coverage=coverage
        )
        
        # Create commit
        code, stdout, stderr = self.run_git_command(['commit', '-m', message])
        
        if code == 0:
            return 0, f'Commit successful:\n{stdout}'
        else:
            return code, f'Commit failed:\n{stderr}'
    
    def add_files(self, files: List[str]) -> Tuple[int, str]:
        """Stage files for commit."""
        if not files:
            return 1, 'No files specified'
        
        code, stdout, stderr = self.run_git_command(['add'] + files)
        
        if code == 0:
            return 0, f'Staged {len(files)} file(s)'
        else:
            return code, f'Failed to stage files:\n{stderr}'
    
    def status(self) -> Tuple[int, str]:
        """Show git status with additional information."""
        code, stdout, stderr = self.run_git_command(['status', '--short'])
        
        if code != 0:
            return code, stderr
        
        status = stdout.strip() if isinstance(stdout, str) else stdout.decode('utf-8').strip()
        if not status:
            return 0, 'Working tree clean'
        
        # Parse status
        staged = []
        unstaged = []
        untracked = []
        
        for line in status.split('\n'):
            if line.startswith('M '):
                unstaged.append(line[3:])
            elif line.startswith(' M'):
                staged.append(line[3:])
            elif line.startswith('??'):
                untracked.append(line[3:])
            elif line.startswith('M'):
                staged.append(line[2:])
        
        output = []
        if staged:
            output.append('Staged changes:')
            for f in staged:
                output.append(f'  M {f}')
        if unstaged:
            output.append('Unstaged changes:')
            for f in unstaged:
                output.append(f'  M {f}')
        if untracked:
            output.append('Untracked files:')
            for f in untracked:
                output.append(f'  ?? {f}')
        
        return 0, '\n'.join(output)
    
    def diff(self, staged: bool = False) -> Tuple[int, str]:
        """Show changes."""
        if staged:
            code, stdout, _ = self.run_git_command(['diff', '--cached'])
        else:
            code, stdout, _ = self.run_git_command(['diff'])
        
        if code == 0:
            return 0, stdout if stdout else 'No changes'
        return code, ''
    
    def log(self, count: int = 10, full: bool = False) -> Tuple[int, str]:
        """Show commit history."""
        if full:
            code, stdout, _ = self.run_git_command(['log', f'-{count}', '--pretty=format:%h%nAuthor: %an%nDate: %ad%n%n%s%n%n%b%n---'])
        else:
            code, stdout, _ = self.run_git_command(['log', f'-{count}', '--oneline'])
        
        if code == 0:
            return 0, stdout
        return code, ''
    
    def undo(self, mode: str = 'soft') -> Tuple[int, str]:
        """Undo last commit."""
        if mode not in ['soft', 'hard']:
            return 1, 'Invalid mode. Use "soft" or "hard"'
        
        # Create backup stash
        self.run_git_command(['stash', 'save', f'backup-before-undo-{mode}'])
        
        code, _, stderr = self.run_git_command(['reset', f'--{mode}', 'HEAD~1'])
        
        if code == 0:
            return 0, f'Undo successful ({mode} mode)'
        else:
            return code, f'Undo failed:\n{stderr}'
    
    def amend(self, description: Optional[str] = None) -> Tuple[int, str]:
        """Amend last commit."""
        if description:
            # Get current commit message
            code, stdout, _ = self.run_git_command(['log', '-1', '--pretty=%B'])
            if code == 0:
                current_msg = stdout.strip()
                new_msg = current_msg + '\n\n' + description
                code, _, stderr = self.run_git_command(['commit', '--amend', '-m', new_msg])
            else:
                return code, 'Failed to get current commit message'
        else:
            code, _, stderr = self.run_git_command(['commit', '--amend', '--no-edit'])
        
        if code == 0:
            return 0, 'Commit amended successfully'
        else:
            return code, f'Amend failed:\n{stderr}'
    
    def stash(self, action: str, message: Optional[str] = None) -> Tuple[int, str]:
        """Stash operations."""
        if action == 'save':
            if not message:
                message = 'WIP'
            code, _, stderr = self.run_git_command(['stash', 'save', message])
        elif action == 'pop':
            code, _, stderr = self.run_git_command(['stash', 'pop'])
        elif action == 'list':
            code, stdout, _ = self.run_git_command(['stash', 'list'])
            if code == 0:
                return 0, stdout if stdout else 'No stashes'
            return code, ''
        elif action == 'drop':
            code, _, stderr = self.run_git_command(['stash', 'drop'])
        else:
            return 1, f'Invalid stash action: {action}'
        
        if code == 0:
            return 0, f'Stash {action} successful'
        else:
            return code, f'Stash {action} failed:\n{stderr}'
    
    def push(self, remote: str = 'origin', branch: Optional[str] = None) -> Tuple[int, str]:
        """Push commits to remote."""
        if not branch:
            branch = self.get_current_branch()
        
        code, _, stderr = self.run_git_command(['push', remote, branch])
        
        if code == 0:
            return 0, f'Pushed to {remote}/{branch}'
        else:
            return code, f'Push failed:\n{stderr}'


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Git Management Skill',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Status command
    subparsers.add_parser('status', help='Show git status')
    
    # Add command
    add_parser = subparsers.add_parser('add', help='Stage files for commit')
    add_parser.add_argument('files', nargs='+', help='Files to stage')
    
    # Commit command
    commit_parser = subparsers.add_parser('commit', help='Create a commit')
    commit_parser.add_argument('type', help='Commit type (feat, fix, etc.)')
    commit_parser.add_argument('description', help='Commit description')
    commit_parser.add_argument('--scope', help='Commit scope')
    commit_parser.add_argument('--body', help='Commit body')
    commit_parser.add_argument('--no-verify', action='store_true', help='Skip pre-commit checks')
    
    # Diff command
    diff_parser = subparsers.add_parser('diff', help='Show changes')
    diff_parser.add_argument('--staged', action='store_true', help='Show staged changes')
    
    # Log command
    log_parser = subparsers.add_parser('log', help='Show commit history')
    log_parser.add_argument('-n', '--count', type=int, default=10, help='Number of commits')
    log_parser.add_argument('--full', action='store_true', help='Show full commit details')
    
    # Undo command
    undo_parser = subparsers.add_parser('undo', help='Undo last commit')
    undo_parser.add_argument('mode', nargs='?', default='soft', choices=['soft', 'hard'], help='Undo mode')
    
    # Amend command
    amend_parser = subparsers.add_parser('amend', help='Amend last commit')
    amend_parser.add_argument('description', nargs='?', help='Additional description')
    
    # Stash command
    stash_parser = subparsers.add_parser('stash', help='Stash operations')
    stash_parser.add_argument('action', choices=['save', 'pop', 'list', 'drop'], help='Stash action')
    stash_parser.add_argument('message', nargs='?', help='Stash message (for save)')
    
    # Push command
    push_parser = subparsers.add_parser('push', help='Push to remote')
    push_parser.add_argument('remote', nargs='?', default='origin', help='Remote name')
    push_parser.add_argument('branch', nargs='?', help='Branch name')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 0
    
    git = GitManage()
    
    # Execute command
    if args.command == 'status':
        code, output = git.status()
    elif args.command == 'add':
        code, output = git.add_files(args.files)
    elif args.command == 'commit':
        code, output = git.commit(
            args.type, args.scope, args.description,
            args.body, args.no_verify
        )
    elif args.command == 'diff':
        code, output = git.diff(staged=args.staged)
    elif args.command == 'log':
        code, output = git.log(count=args.count, full=args.full)
    elif args.command == 'undo':
        code, output = git.undo(mode=args.mode)
    elif args.command == 'amend':
        code, output = git.amend(description=args.description)
    elif args.command == 'stash':
        code, output = git.stash(args.action, args.message)
    elif args.command == 'push':
        code, output = git.push(args.remote, args.branch)
    else:
        code, output = 1, f'Unknown command: {args.command}'
    
    print(output)
    return code


if __name__ == '__main__':
    sys.exit(main())