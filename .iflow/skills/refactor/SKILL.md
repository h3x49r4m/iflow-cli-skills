# Refactor Skill

Automated code refactoring and improvement skill that analyzes codebases to identify and suggest refactoring opportunities.

## Purpose

This skill systematically reviews codebases to identify code quality issues and provide actionable refactoring suggestions. It helps maintain clean, maintainable, and efficient code by detecting common anti-patterns and suggesting improvements.

## Capabilities

### Code Quality Analysis

1. **Duplicate Code Detection**
   - Identifies identical or similar code blocks across the project
   - Suggests extraction into reusable functions/methods
   - Calculates similarity scores for duplicate identification

2. **Magic Number/String Extraction**
   - Detects hardcoded literals (numbers, strings) in code
   - Suggests creating named constants with meaningful names
   - Prioritizes frequently repeated literals

3. **Function/Method Decomposition**
   - Identifies overly long functions (configurable threshold)
   - Analyzes cyclomatic complexity
   - Suggests breaking down into smaller, single-responsibility units

4. **Naming Convention Improvements**
   - Detects poor variable/function names (single letters, abbreviations)
   - Identifies inconsistent naming patterns
   - Suggests descriptive, self-documenting names

5. **Dead Code Elimination**
   - Finds unused imports across the codebase
   - Identifies unused variables and parameters
   - Detects unused functions, classes, and methods

6. **Conditional Complexity Reduction**
   - Simplifies deeply nested if/else statements
   - Suggests guard clauses and early returns
   - Recommends switch/case or pattern matching alternatives

7. **Loop Optimization**
   - Identifies inefficient loop patterns
   - Suggests more idiomatic alternatives (e.g., map/filter/reduce)
   - Detects nested loops that could be optimized

8. **Type Safety Improvements**
   - Identifies opportunities for type inference
   - Suggests explicit type annotations where beneficial
   - Detects any type inconsistencies

9. **Code Smell Detection**
   - God Functions: overly large functions with too many responsibilities
   - Feature Envy: functions that use another object's data more than their own
   - Data Clumps: variables that appear together frequently
   - Primitive Obsession: using primitives instead of domain objects

10. **Import Organization**
    - Sorts imports alphabetically and by group (stdlib, third-party, local)
    - Removes duplicate imports
    - Identifies unused imports

## Workflow Integration

This skill integrates with other iFlow CLI tools and agents:

- Uses **explore-agent** for initial codebase understanding and structure analysis
- Uses **general-purpose** agent for applying refactoring suggestions
- Leverages **search_file_content** and **glob** for pattern matching
- Utilizes **read_file** and **replace** for code modifications

## Usage

The refactor skill can be invoked when you need to:

- Improve code maintainability and readability
- Reduce technical debt in a codebase
- Prepare code for new features by cleaning up existing code
- Ensure consistent coding standards across a project
- Identify and eliminate code duplication
- Optimize performance through refactoring

## Configuration

Refactoring behavior can be customized through configuration files in `config/`:

- `refactor-rules.json`: Overall refactoring rules and priorities
- `language-patterns.json`: Language-specific patterns and anti-patterns
- `thresholds.json`: Configurable thresholds (function length, complexity scores, etc.)

## Workflows

Detailed workflows for each refactoring capability are located in `workflows/`:

- `code-analysis.md`: Main codebase analysis workflow
- `duplicate-detection.md`: Duplicate code identification workflow
- `constant-extraction.md`: Magic literal extraction workflow
- `function-decomposition.md`: Function splitting workflow
- `dead-code-elimination.md`: Unused code removal workflow
- `complexity-reduction.md`: Conditional simplification workflow
- `refactoring-report.md`: Report generation workflow

## State Management

Persistent state is maintained in `.state/` for:

- Analysis results and findings
- Previous refactor suggestions and their status
- Project-specific patterns and exceptions
- Historical refactoring data for trend analysis

## Safety

This skill prioritizes safe, incremental refactoring:

- Provides before/after code examples for review
- Highlights potential risks and dependencies
- Groups related refactorings to avoid breaking changes
- Allows selective application of suggestions
- Maintains backward compatibility where possible