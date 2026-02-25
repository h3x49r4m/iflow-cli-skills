#!/usr/bin/env python3
"""
TDD Enforcement Skill - Implementation
Comprehensive enforcement of TDD workflow, project conventions, code conciseness, and code quality
with project-aware pattern learning and context-aware validation.
"""

import argparse
import ast
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Set, Any
from collections import defaultdict, Counter


class ProjectAnalyzer:
    """Analyzes project to extract patterns and conventions."""

    def __init__(self, repo_root: Optional[Path] = None):
        self.repo_root = repo_root or Path.cwd()
        self.patterns = {
            'naming': defaultdict(Counter),
            'structure': defaultdict(list),
            'imports': defaultdict(list),
            'functions': defaultdict(list),
            'docstrings': Counter(),
            'quality': defaultdict(int)
        }
        self._analyzed = False

    def analyze_project(self) -> None:
        """Analyze the entire project to extract patterns."""
        if self._analyzed:
            return

        print("Analyzing project patterns...")

        # Find all source files
        source_files = self._find_source_files()

        for file_path in source_files:
            self._analyze_file(file_path)

        self._analyzed = True
        print(f"Analyzed {len(source_files)} files")

    def _find_source_files(self) -> List[Path]:
        """Find all source files in the project."""
        extensions = {'.py', '.js', '.ts', '.jsx', '.tsx', '.rs', '.go', '.java'}
        files = []

        # Common source directories
        src_dirs = ['src', 'lib', 'app', 'core', 'main']

        for root, dirs, filenames in os.walk(self.repo_root):
            # Skip common directories to ignore
            dirs[:] = [d for d in dirs if d not in {'.git', '__pycache__', 'node_modules', 'target', 'venv', '.venv', 'dist', 'build', 'vendor'}]

            for filename in filenames:
                if any(filename.endswith(ext) for ext in extensions):
                    files.append(Path(root) / filename)

        return files

    def _analyze_file(self, file_path: Path) -> None:
        """Analyze a single file to extract patterns."""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            ext = file_path.suffix

            if ext == '.py':
                self._analyze_python_file(file_path, content)
            elif ext in {'.js', '.ts', '.jsx', '.tsx'}:
                self._analyze_javascript_file(file_path, content)
            # Add more language analyzers as needed

        except (IOError, UnicodeDecodeError, SyntaxError):
            pass

    def _analyze_python_file(self, file_path: Path, content: str) -> None:
        """Analyze Python file patterns."""
        try:
            tree = ast.parse(content, filename=str(file_path))

            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    # Function naming patterns
                    name_style = self._detect_naming_style(node.name)
                    self.patterns['naming']['function'][name_style] += 1

                    # Function structure
                    source_segment = ast.get_source_segment(content, node)
                    func_lines = 0
                    if source_segment and isinstance(source_segment, str):
                        func_lines = len(source_segment.split('\n'))
                    self.patterns['structure']['function_lines'].append(func_lines)
                    self.patterns['structure']['function_params'].append(len(node.args.args))

                    # Check for docstring
                    docstring = ast.get_docstring(node)
                    if docstring:
                        self.patterns['docstrings']['has_docstring'] += 1

                elif isinstance(node, ast.ClassDef):
                    name_style = self._detect_naming_style(node.name)
                    self.patterns['naming']['class'][name_style] += 1

                elif isinstance(node, ast.Constant) and isinstance(node.value, str) and len(node.value) > 1:
                    # Detect magic literals (simplified)
                    if not node.value.isupper():
                        self.patterns['quality']['string_literals'] += 1

                elif isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
                    if node.value not in {0, 1, -1}:
                        self.patterns['quality']['numeric_literals'] += 1

            # Import patterns
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        self.patterns['imports']['external'].append(alias.name)
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        if node.module.startswith('.'):
                            self.patterns['imports']['local'].append(node.module)
                        else:
                            self.patterns['imports']['external'].append(node.module)

        except SyntaxError:
            pass

    def _analyze_javascript_file(self, file_path: Path, content: str) -> None:
        """Analyze JavaScript/TypeScript file patterns (simplified)."""
        # Function naming
        func_pattern = r'function\s+([a-zA-Z_][a-zA-Z0-9_]*)|const\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*='
        for match in re.finditer(func_pattern, content):
            name = match.group(1) or match.group(2)
            if name:
                name_style = self._detect_naming_style(name)
                self.patterns['naming']['function'][name_style] += 1

        # Class naming
        class_pattern = r'class\s+([A-Z][a-zA-Z0-9]*)'
        for match in re.finditer(class_pattern, content):
            name = match.group(1)
            name_style = self._detect_naming_style(name)
            self.patterns['naming']['class'][name_style] += 1

        # Import patterns (simplified)
        import_pattern = r'import\s+.*?\s+from\s+[\'"]([^\'"]+)[\'"]'
        for match in re.finditer(import_pattern, content):
            module = match.group(1)
            if module.startswith('.') or module.startswith('/'):
                self.patterns['imports']['local'].append(module)
            else:
                self.patterns['imports']['external'].append(module)

    def _detect_naming_style(self, name: str) -> str:
        """Detect the naming style used."""
        if '_' in name and name.islower():
            return 'snake_case'
        elif '_' in name and name.isupper():
            return 'UPPER_SNAKE_CASE'
        elif name[0].isupper():
            return 'PascalCase'
        elif name[0].islower() and not '_' in name:
            return 'camelCase'
        else:
            return 'unknown'

    def get_project_patterns(self) -> Dict[str, Any]:
        """Get extracted project patterns."""
        if not self._analyzed:
            self.analyze_project()

        # Determine dominant patterns
        result = {}

        # Naming conventions
        result['function_naming'] = self.patterns['naming']['function'].most_common(1)[0][0] if self.patterns['naming']['function'] else 'snake_case'
        result['class_naming'] = self.patterns['naming']['class'].most_common(1)[0][0] if self.patterns['naming']['class'] else 'PascalCase'

        # Function structure averages
        if self.patterns['structure']['function_lines']:
            avg_lines = sum(self.patterns['structure']['function_lines']) / len(self.patterns['structure']['function_lines'])
            result['avg_function_lines'] = round(avg_lines)
        else:
            result['avg_function_lines'] = 50

        if self.patterns['structure']['function_params']:
            avg_params = sum(self.patterns['structure']['function_params']) / len(self.patterns['structure']['function_params'])
            result['avg_function_params'] = round(avg_params)
        else:
            result['avg_function_params'] = 5

        # Docstring usage
        total_functions = self.patterns['docstrings']['has_docstring']
        docstring_ratio = total_functions / max(1, len(self.patterns['structure']['function_lines']))
        result['docstring_usage'] = docstring_ratio >= 0.8

        # Import patterns
        result['import_organization'] = bool(self.patterns['imports']['external'] or self.patterns['imports']['local'])

        return result

    def check_compliance(self, file_path: Path, content: str) -> List[Dict[str, str]]:
        """Check if a file complies with project patterns."""
        violations = []
        patterns = self.get_project_patterns()

        ext = file_path.suffix

        if ext == '.py':
            violations.extend(self._check_python_compliance(file_path, content, patterns))
        elif ext in {'.js', '.ts', '.jsx', '.tsx'}:
            violations.extend(self._check_javascript_compliance(file_path, content, patterns))

        return violations

    def _check_python_compliance(self, file_path: Path, content: str, patterns: Dict[str, Any]) -> List[Dict[str, str]]:
        """Check Python file compliance with project patterns."""
        violations = []

        try:
            tree = ast.parse(content, filename=str(file_path))

            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    # Check naming
                    expected_style = patterns.get('function_naming', 'snake_case')
                    actual_style = self._detect_naming_style(node.name)

                    if actual_style != expected_style and expected_style != 'unknown':
                        violations.append({
                            'type': 'naming',
                            'severity': 'warning',
                            'message': f"Function '{node.name}' uses {actual_style} but project uses {expected_style}",
                            'line': node.lineno,
                            'file': str(file_path)
                        })

                    # Check function size
                    source_segment = ast.get_source_segment(content, node)
                    if source_segment and isinstance(source_segment, str):
                        func_lines = len(source_segment.split('\n'))
                    else:
                        func_lines = 0
                    avg_lines = patterns.get('avg_function_lines', 50)
                    if func_lines > avg_lines * 1.5:
                        violations.append({
                            'type': 'structure',
                            'severity': 'warning',
                            'message': f"Function '{node.name}' is {func_lines} lines (project avg: {avg_lines})",
                            'line': node.lineno,
                            'file': str(file_path)
                        })

                    # Check parameters
                    num_params = len(node.args.args)
                    avg_params = patterns.get('avg_function_params', 5)
                    if num_params > avg_params + 2:
                        violations.append({
                            'type': 'structure',
                            'severity': 'warning',
                            'message': f"Function '{node.name}' has {num_params} parameters (project avg: {avg_params})",
                            'line': node.lineno,
                            'file': str(file_path)
                        })

                    # Check docstring
                    if patterns.get('docstring_usage', False):
                        has_docstring = ast.get_docstring(node) is not None
                        if not has_docstring and not node.name.startswith('_'):
                            violations.append({
                                'type': 'documentation',
                                'severity': 'info',
                                'message': f"Function '{node.name}' is missing docstring (project uses docstrings)",
                                'line': node.lineno,
                                'file': str(file_path)
                            })

        except SyntaxError:
            violations.append({
                'type': 'syntax',
                'severity': 'error',
                'message': f"Syntax error in file",
                'file': str(file_path)
            })

        # Check refactoring principles: duplicate code and verbose patterns
        # Check for duplicate code (simple heuristic)
        lines = content.split('\n')
        line_counts = {}
        for line in lines:
            stripped = line.strip()
            if len(stripped) > 20 and not stripped.startswith('#'):
                line_counts[stripped] = line_counts.get(stripped, 0) + 1
        
        for line, count in line_counts.items():
            if count > 2:
                violations.append({
                    'type': 'duplicate_code',
                    'severity': 'warning',
                    'message': f'Duplicate code detected (appears {count} times)',
                    'file': str(file_path),
                    'suggestion': 'Extract to a shared function or constant'
                })
                break  # Only report first occurrence
        
        # Check for verbose patterns
        verbose_patterns = [
            (r'for\s+\w+\s+in\s+range\(len\([^)]+\)\):', 'Use enumerate() or direct iteration'),
            (r'if\s+\w+\s+==\s+True:', 'Use "if value:" instead'),
            (r'if\s+\w+\s+!=\s+True:', 'Use "if not value:" instead'),
        ]
        
        for pattern, suggestion in verbose_patterns:
            if re.search(pattern, content):
                violations.append({
                    'type': 'verbose_code',
                    'severity': 'info',
                    'message': 'Verbose pattern detected',
                    'file': str(file_path),
                    'suggestion': suggestion
                })

        return violations

    def _check_javascript_compliance(self, file_path: Path, content: str, patterns: Dict[str, Any]) -> List[Dict[str, str]]:
        """Check JavaScript/TypeScript file compliance with project patterns."""
        violations = []

        # Check function naming
        func_pattern = r'function\s+([a-zA-Z_][a-zA-Z0-9_]*)|const\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*(?:async\s+)?\(.*?\)\s*=>'
        for match in re.finditer(func_pattern, content):
            name = match.group(1) or match.group(2)
            if name:
                expected_style = patterns.get('function_naming', 'camelCase')
                actual_style = self._detect_naming_style(name)

                if actual_style != expected_style and expected_style != 'unknown':
                    violations.append({
                        'type': 'naming',
                        'severity': 'warning',
                        'message': f"Function '{name}' uses {actual_style} but project uses {expected_style}",
                        'file': str(file_path)
                    })

        return violations


class TDDEnforce:
    """Main TDD enforcement class with project awareness."""

    def __init__(self, repo_root: Optional[Path] = None):
        self.repo_root = repo_root or Path.cwd()
        self.config_file = self.repo_root / '.iflow' / 'skills' / 'tdd-enforce' / 'config.json'
        self.analyzer = ProjectAnalyzer(repo_root)
        self.load_config()

    def load_config(self):
        """Load configuration from config file."""
        self.config = {
            'tdd': {
                'enforceTestFirst': True,
                'requireTestFailure': True,
                'coverageThresholds': {'lines': 90, 'branches': 80}
            },
            'recursionDetection': {'enabled': True},
            'loopBounding': {'enabled': True},
            'conventions': {
                'naming': {'enforceSnakeCase': True, 'enforcePascalCase': True},
                'structure': {'maxFunctionLines': 50, 'maxParameters': 5}
            },
            'projectAware': {
                'enabled': True,
                'learnPatterns': True,
                'adaptRules': True
            }
        }

        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    user_config = json.load(f)
                    self._merge_config(user_config)
            except (json.JSONDecodeError, IOError):
                pass

    def _merge_config(self, user_config: Dict):
        """Merge user config with defaults."""
        def merge_dict(base, update):
            for key, value in update.items():
                if key in base and isinstance(base[key], dict) and isinstance(value, dict):
                    merge_dict(base[key], value)
                else:
                    base[key] = value

        merge_dict(self.config, user_config)

    def check_file(self, file_path: Path) -> Tuple[int, List[Dict[str, str]]]:
        """Check a single file for TDD and convention compliance."""
        violations = []

        if not file_path.exists():
            return 0, []

        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except IOError:
            return 0, []

        # Check for test file
        is_test_file = self._is_test_file(file_path)

        # Project-aware compliance check
        if self.config.get('projectAware', {}).get('enabled', True):
            self.analyzer.analyze_project()
            violations.extend(self.analyzer.check_compliance(file_path, content))

        # Standard TDD checks
        if not is_test_file:
            # Check if corresponding test file exists
            test_file = self._find_test_file(file_path)
            if not test_file or not test_file.exists():
                violations.append({
                    'type': 'tdd',
                    'severity': 'error',
                    'message': f"Implementation file '{file_path.name}' has no corresponding test file",
                    'file': str(file_path)
                })

            # Check for recursion
            if self.config.get('recursionDetection', {}).get('enabled', True):
                violations.extend(self._check_recursion(file_path, content))

            # Check for infinite loops
            if self.config.get('loopBounding', {}).get('enabled', True):
                violations.extend(self._check_loops(file_path, content))

        return len(violations), violations

    def _is_test_file(self, file_path: Path) -> bool:
        """Check if file is a test file."""
        name = file_path.name.lower()
        return 'test' in name or file_path.stem.endswith('_test') or file_path.parent.name == 'tests'

    def _find_test_file(self, file_path: Path) -> Optional[Path]:
        """Find corresponding test file for implementation file."""
        stem = file_path.stem
        ext = file_path.suffix

        # Common test file patterns
        test_patterns = [
            file_path.parent / f"test_{stem}{ext}",
            file_path.parent / f"{stem}_test{ext}",
            file_path.parent.parent / 'tests' / f"test_{stem}{ext}",
            file_path.parent.parent / 'tests' / f"{stem}_test{ext}",
        ]

        for pattern in test_patterns:
            if pattern.exists():
                return pattern

        return None

    def _check_recursion(self, file_path: Path, content: str) -> List[Dict[str, str]]:
        """Check for recursive functions."""
        violations = []

        if file_path.suffix == '.py':
            try:
                tree = ast.parse(content, filename=str(file_path))

                for node in ast.walk(tree):
                    if isinstance(node, ast.FunctionDef):
                        func_name = node.name
                        # Check if function calls itself
                        for call in ast.walk(node):
                            if isinstance(call, ast.Call):
                                if isinstance(call.func, ast.Name) and call.func.id == func_name:
                                    violations.append({
                                        'type': 'recursion',
                                        'severity': 'error',
                                        'message': f"Recursive function '{func_name}' detected",
                                        'line': node.lineno,
                                        'file': str(file_path)
                                    })
                                    break
            except SyntaxError:
                pass

        return violations

    def _check_loops(self, file_path: Path, content: str) -> List[Dict[str, str]]:
        """Check for infinite loops."""
        violations = []

        # Common infinite loop patterns
        patterns = [
            r'while\s*\(\s*True\s*\)',
            r'while\s*\(\s*1\s*\)',
            r'for\s*\(\s*;\s*;\s*\)',
            r'while\s*\(\s*true\s*\)',
        ]

        for pattern in patterns:
            for match in re.finditer(pattern, content, re.IGNORECASE):
                line_num = content[:match.start()].count('\n') + 1
                violations.append({
                    'type': 'loop',
                    'severity': 'error',
                    'message': f"Potential infinite loop detected: {match.group()}",
                    'line': line_num,
                    'file': str(file_path)
                })

        return violations

    def check_staged_files(self) -> Tuple[int, List[Dict[str, str]]]:
        """Check all staged files for compliance."""
        try:
            result = subprocess.run(
                ['git', 'diff', '--name-only', '--cached'],
                cwd=self.repo_root,
                capture_output=True,
                text=True
            )
        except (FileNotFoundError, subprocess.SubprocessError):
            return 0, []

        if result.returncode != 0:
            return 0, []

        staged_files = result.stdout.strip().split('\n') if result.stdout.strip() else []
        all_violations = []

        for file_path in staged_files:
            full_path = self.repo_root / file_path
            if full_path.exists() and not full_path.is_dir():
                _, violations = self.check_file(full_path)
                all_violations.extend(violations)

        return len(all_violations), all_violations

    def generate_report(self, violations: List[Dict[str, str]]) -> str:
        """Generate a compliance report."""
        lines = ['TDD Compliance Report', '=' * 40, '']

        if not violations:
            lines.append('✓ All checks passed!')
            return '\n'.join(lines)

        # Group by severity
        by_severity = defaultdict(list)
        for v in violations:
            by_severity[v['severity']].append(v)

        # Summary
        error_count = len(by_severity.get('error', []))
        warning_count = len(by_severity.get('warning', []))
        info_count = len(by_severity.get('info', []))

        lines.append(f'Violations: {len(violations)} total')
        lines.append(f'  Errors: {error_count}')
        lines.append(f'  Warnings: {warning_count}')
        lines.append(f'  Info: {info_count}')
        lines.append('')

        # Project patterns
        if self.config.get('projectAware', {}).get('enabled', True):
            patterns = self.analyzer.get_project_patterns()
            lines.append('Detected Project Patterns:')
            lines.append(f'  Function naming: {patterns.get("function_naming", "unknown")}')
            lines.append(f'  Class naming: {patterns.get("class_naming", "unknown")}')
            lines.append(f'  Avg function size: {patterns.get("avg_function_lines", "N/A")} lines')
            lines.append(f'  Docstring usage: {"Yes" if patterns.get("docstring_usage") else "No"}')
            lines.append('')

        # Violations by type
        by_type = defaultdict(list)
        for v in violations:
            by_type[v['type']].append(v)

        for vtype, type_violations in sorted(by_type.items()):
            lines.append(f'{vtype.upper()} VIOLATIONS ({len(type_violations)})')
            lines.append('-' * 40)
            for v in type_violations[:10]:  # Limit to 10 per type
                line_info = f"{v['file']}"
                if 'line' in v:
                    line_info += f":{v['line']}"
                lines.append(f"  [{v['severity'].upper()}] {v['message']}")
                lines.append(f"      Location: {line_info}")
            if len(type_violations) > 10:
                lines.append(f"  ... and {len(type_violations) - 10} more")
            lines.append('')

        return '\n'.join(lines)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='TDD Enforcement Skill',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument('files', nargs='*', help='Files to check (default: staged files)')
    parser.add_argument('--project-aware', action='store_true', default=True,
                       help='Enable project-aware pattern learning')
    parser.add_argument('--output', choices=['text', 'json'], default='text',
                       help='Output format')

    args = parser.parse_args()

    tdd = TDDEnforce()

    # Check files
    if args.files:
        all_violations = []
        for file_path in args.files:
            _, violations = tdd.check_file(Path(file_path))
            all_violations.extend(violations)
    else:
        _, all_violations = tdd.check_staged_files()

    # Generate report
    if args.output == 'json':
        print(json.dumps({
            'violations': all_violations,
            'count': len(all_violations),
            'patterns': tdd.analyzer.get_project_patterns()
        }, indent=2))
    else:
        print(tdd.generate_report(all_violations))

    # Exit code based on violations
    error_count = sum(1 for v in all_violations if v['severity'] == 'error')
    sys.exit(1 if error_count > 0 else 0)


if __name__ == '__main__':
    sys.exit(main())