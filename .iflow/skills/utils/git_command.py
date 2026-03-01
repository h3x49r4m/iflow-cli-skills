#!/usr/bin/env python3
"""
Shared Git Command Utility
Provides centralized git command execution with timeout handling and error management.
"""

import subprocess
from pathlib import Path
from typing import Tuple, Optional, List
import sys


class GitCommandError(Exception):
    """Exception raised when a git command fails."""
    def __init__(self, message: str, returncode: int, stderr: str = ""):
        self.message = message
        self.returncode = returncode
        self.stderr = stderr
        super().__init__(self.message)


class GitCommandTimeout(Exception):
    """Exception raised when a git command times out."""
    pass


def run_git_command(
    command: List[str],
    cwd: Optional[Path] = None,
    timeout: Optional[int] = 120,
    capture: bool = True
) -> Tuple[int, str, str]:
    """
    Execute a git command with timeout handling.
    
    Args:
        command: List of command arguments (without 'git' prefix)
        cwd: Working directory for command execution
        timeout: Timeout in seconds (default: 120)
        capture: Whether to capture stdout/stderr
    
    Returns:
        Tuple of (returncode, stdout, stderr)
    
    Raises:
        GitCommandError: If git is not found
        GitCommandTimeout: If command times out
    """
    if cwd is None:
        cwd = Path.cwd()
    
    full_command = ['git'] + command
    
    try:
        result = subprocess.run(
            full_command,
            cwd=cwd,
            capture_output=capture,
            text=not capture,
            timeout=timeout
        )
        
        if capture:
            stdout = result.stdout
            stderr = result.stderr
        else:
            stdout = ''
            stderr = ''
        
        return result.returncode, stdout, stderr
        
    except FileNotFoundError:
        raise GitCommandError(
            'Git not found in PATH. Please ensure git is installed and in your PATH.',
            1
        )
    except subprocess.TimeoutExpired:
        raise GitCommandTimeout(
            f'Git command timed out after {timeout} seconds: {" ".join(command)}'
        )
    except Exception as e:
        raise GitCommandError(
            f'Unexpected error running git command: {str(e)}',
            1
        )


def validate_git_repo(cwd: Optional[Path] = None) -> bool:
    """
    Check if current directory is a valid git repository.
    
    Args:
        cwd: Working directory to check
    
    Returns:
        True if valid git repo, False otherwise
    """
    try:
        returncode, _, _ = run_git_command(['rev-parse', '--git-dir'], cwd=cwd, timeout=10)
        return returncode == 0
    except (GitCommandError, GitCommandTimeout):
        return False


def get_current_branch(cwd: Optional[Path] = None) -> str:
    """
    Get the current branch name.
    
    Args:
        cwd: Working directory
    
    Returns:
        Current branch name or 'unknown' if error
    """
    try:
        code, stdout, _ = run_git_command(['rev-parse', '--abbrev-ref', 'HEAD'], cwd=cwd, timeout=10)
        return stdout.strip() if code == 0 else 'unknown'
    except (GitCommandError, GitCommandTimeout):
        return 'unknown'


def get_repo_root(cwd: Optional[Path] = None) -> Optional[Path]:
    """
    Get the git repository root directory.
    
    Args:
        cwd: Working directory
    
    Returns:
        Path to repo root or None if not in a git repo
    """
    try:
        code, stdout, _ = run_git_command(['rev-parse', '--show-toplevel'], cwd=cwd, timeout=10)
        if code == 0:
            return Path(stdout.strip())
        return None
    except (GitCommandError, GitCommandTimeout):
        return None


def validate_branch_name(branch_name: str) -> Tuple[bool, Optional[str]]:
    """
    Validate a git branch name according to git naming rules.
    
    Args:
        branch_name: Branch name to validate
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not branch_name:
        return False, "Branch name cannot be empty"
    
    # Git branch name validation rules
    # - Cannot begin or end with a dot
    # - Cannot contain two consecutive dots
    # - Cannot contain ~, ^, :, \, ?, *, [, space, or ASCII control characters
    # - Cannot begin or end with a slash
    # - Cannot contain consecutive slashes
    # - Cannot end with a .lock
    # - Cannot contain @{ or ..
    
    if branch_name.startswith('.') or branch_name.endswith('.'):
        return False, "Branch name cannot begin or end with a dot"
    
    if '..' in branch_name:
        return False, "Branch name cannot contain '..'"
    
    if '@{' in branch_name:
        return False, "Branch name cannot contain '@{'"
    
    forbidden_chars = ['~', '^', ':', '\\', '?', '*', '[', ' ', '\t', '\n', '\r']
    for char in forbidden_chars:
        if char in branch_name:
            return False, f"Branch name cannot contain '{char}'"
    
    if branch_name.startswith('/') or branch_name.endswith('/'):
        return False, "Branch name cannot begin or end with a slash"
    
    if '//' in branch_name:
        return False, "Branch name cannot contain consecutive slashes"
    
    if branch_name.endswith('.lock'):
        return False, "Branch name cannot end with '.lock'"
    
    return True, None


def validate_file_path(file_path: str, repo_root: Optional[Path] = None) -> Tuple[bool, Optional[str]]:
    """
    Validate a file path for security (prevent path traversal).
    
    Args:
        file_path: File path to validate
        repo_root: Repository root directory
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not file_path:
        return False, "File path cannot be empty"
    
    # Check for path traversal attempts
    if '../' in file_path or '..\\' in file_path:
        return False, "Path traversal detected"
    
    if file_path.startswith('/') or (len(file_path) > 1 and file_path[1] == ':'):
        # Absolute path - resolve and check if within repo
        try:
            path = Path(file_path).resolve()
            if repo_root:
                try:
                    path.relative_to(repo_root)
                except ValueError:
                    return False, "File path is outside repository"
        except Exception:
            return False, "Invalid file path"
    
    return True, None
