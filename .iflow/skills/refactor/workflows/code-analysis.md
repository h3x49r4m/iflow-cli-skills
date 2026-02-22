# Code Analysis Workflow

Main workflow for comprehensive codebase analysis and refactoring opportunity identification.

## Overview

This workflow performs a systematic analysis of the codebase to identify refactoring opportunities across multiple dimensions. It serves as the entry point for all refactoring activities.

## Steps

### 1. Project Structure Discovery

**Goal**: Understand the project structure and identify target files.

**Actions**:
- Use `list_directory` to explore the root and subdirectories
- Use `glob` to find all source code files based on common extensions
- Identify programming languages used in the project
- Exclude build artifacts, node_modules, .git, and other non-source directories

**Output**: List of all source files organized by language and directory.

### 2. Language-Specific Pattern Loading

**Goal**: Load refactoring patterns and rules for detected languages.

**Actions**:
- Read `config/language-patterns.json`
- Extract patterns for detected languages
- Load language-specific anti-patterns and best practices

**Output**: Language-specific refactoring rules and patterns.

### 3. Threshold Configuration

**Goal**: Load configurable thresholds for refactoring decisions.

**Actions**:
- Read `config/thresholds.json`
- Extract thresholds for:
  - Maximum function length (lines)
  - Maximum cyclomatic complexity
  - Maximum nesting depth
  - Maximum parameter count
  - Minimum similarity score for duplicates

**Output**: Threshold values for refactoring criteria.

### 4. File-by-File Analysis

**Goal**: Analyze each source file for refactoring opportunities.

**Actions**:
- For each source file:
  - Read file content using `read_file`
  - Apply language-specific pattern matching
  - Check against configured thresholds
  - Identify all refactoring opportunities
  - Calculate severity and impact scores

**Output**: Detailed analysis results per file with refactoring suggestions.

### 5. Cross-File Analysis

**Goal**: Identify issues that require analyzing multiple files.

**Actions**:
- **Duplicate Detection**:
  - Use `search_file_content` with regex patterns for common code structures
  - Compare similar blocks across files
  - Calculate similarity scores
- **Dead Code Detection**:
  - Track all function/class definitions
  - Search for usages across all files
  - Identify unused definitions
- **Import Analysis**:
  - Collect all imports from all files
  - Check for unused imports
  - Identify duplicate imports

**Output**: Cross-file refactoring opportunities.

### 6. Prioritization and Scoring

**Goal**: Prioritize refactoring suggestions by impact and effort.

**Actions**:
- For each refactoring opportunity:
  - Calculate impact score (maintainability, performance, readability)
  - Estimate effort required (lines changed, files affected)
  - Calculate priority score = impact / effort
  - Group related refactorings together

**Output**: Prioritized list of refactoring suggestions with scores.

### 7. Report Generation

**Goal**: Generate comprehensive refactoring report.

**Actions**:
- Organize findings by category (duplication, complexity, naming, etc.)
- Include file locations and line numbers
- Provide before/after code examples
- Highlight high-priority items
- Note potential risks and dependencies

**Output**: Structured refactoring report (see `refactoring-report.md`).

## Integration Points

This workflow calls other specialized workflows:

- `duplicate-detection.md` for detailed duplicate code analysis
- `constant-extraction.md` for magic literal identification
- `function-decomposition.md` for complex function analysis
- `dead-code-elimination.md` for unused code detection
- `complexity-reduction.md` for conditional simplification

## Output Format

Analysis results should be structured as:

```json
{
  "summary": {
    "total_files_analyzed": number,
    "total_opportunities": number,
    "high_priority": number,
    "medium_priority": number,
    "low_priority": number
  },
  "by_category": {
    "duplicate_code": { ... },
    "magic_literals": { ... },
    "long_functions": { ... },
    "poor_naming": { ... },
    "dead_code": { ... },
    "complex_conditionals": { ... },
    "code_smells": { ... }
  },
  "detailed_findings": [
    {
      "category": string,
      "file": string,
      "line": number,
      "severity": "high" | "medium" | "low",
      "description": string,
      "suggestion": string,
      "before": string,
      "after": string,
      "impact_score": number,
      "effort_score": number,
      "priority_score": number
    }
  ]
}
```

## Next Steps

After completing this workflow:

1. Review the generated refactoring report
2. Select high-priority items for immediate action
3. Use specialized workflows for detailed analysis of specific categories
4. Apply refactoring suggestions using appropriate tools
5. Verify changes don't break existing functionality