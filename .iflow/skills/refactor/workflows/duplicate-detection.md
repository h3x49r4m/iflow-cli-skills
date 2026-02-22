# Duplicate Code Detection Workflow

Workflow for identifying and suggesting fixes for duplicate code blocks.

## Overview

This workflow systematically identifies duplicate or highly similar code blocks across the codebase and suggests extraction into reusable functions, methods, or classes.

## Steps

### 1. Code Block Extraction

**Goal**: Extract candidate code blocks from source files.

**Actions**:
- For each source file:
  - Read file content using `read_file`
  - Parse into code blocks (functions, methods, loops, conditionals)
  - Normalize blocks (remove whitespace, comments, variable names where appropriate)
  - Store with metadata (file, line numbers, block type)

**Output**: List of normalized code blocks with source location.

### 2. Similarity Calculation

**Goal**: Calculate similarity scores between all pairs of code blocks.

**Actions**:
- Compare each block against all others
- Use string similarity algorithms (e.g., Levenshtein distance, Jaccard similarity)
- Consider structural similarity (control flow, nesting level)
- Apply language-specific normalization rules

**Output**: Matrix of similarity scores between code blocks.

### 3. Duplicate Grouping

**Goal**: Group similar blocks into duplicate clusters.

**Actions**:
- Apply similarity threshold from `config/thresholds.json`
- Use clustering algorithm to group similar blocks
- Identify representative block for each cluster
- Calculate cluster size and distribution

**Output**: Groups of duplicate code blocks.

### 4. Analysis and Suggestion Generation

**Goal**: Analyze each duplicate cluster and generate refactoring suggestions.

**Actions**:
For each duplicate cluster:
- Extract common pattern and variable parts
- Identify parameterizable elements
- Suggest extraction location (utility file, common module)
- Determine appropriate function/method signature
- Generate before/after code examples
- Estimate impact and effort

**Output**: Detailed refactoring suggestions for each duplicate cluster.

### 5. Priority Scoring

**Goal**: Score duplicate clusters by refactoring value.

**Actions**:
- Calculate impact based on:
  - Number of duplicates (cluster size)
  - Total lines of duplicated code
  - Frequency of changes (if git history available)
- Calculate effort based on:
  - Complexity of extracting common logic
  - Number of parameters needed
  - Number of files affected
- Compute priority score

**Output**: Prioritized list of duplicate clusters.

## Detection Strategies

### Exact Duplicates

- Identical code blocks (excluding comments and whitespace)
- Highest priority for refactoring
- Easy to extract into shared function

### Near Duplicates

- Similar structure with minor differences:
  - Different variable names
  - Slightly different logic
  - Different constants
- Requires parameterization
- Moderate priority

### Structural Duplicates

- Similar control flow and logic structure
- May have different implementations of sub-operations
- Requires abstraction/interfaces
- Lower priority

## Output Format

```json
{
  "duplicate_clusters": [
    {
      "cluster_id": string,
      "similarity_score": number,
      "block_count": number,
      "total_lines": number,
      "severity": "high" | "medium" | "low",
      "locations": [
        {
          "file": string,
          "start_line": number,
          "end_line": number,
          "function": string
        }
      ],
      "common_pattern": string,
      "differences": [
        {
          "type": "variable" | "constant" | "logic",
          "description": string
        }
      ],
      "suggestion": {
        "extract_to": string,
        "function_name": string,
        "parameters": [string],
        "before_example": string,
        "after_example": string
      },
      "impact_score": number,
      "effort_score": number,
      "priority_score": number
    }
  ]
}
```

## Language-Specific Considerations

### JavaScript/TypeScript

- Detect duplicate callback functions
- Identify repeated promise chains
- Look for similar event handlers

### Python

- Detect duplicate list comprehensions
- Identify repeated decorator patterns
- Look for similar context managers

### Java/C#

- Detect duplicate method implementations
- Identify repeated exception handling
- Look for similar factory patterns

## Integration

This workflow is called by:
- `code-analysis.md` as part of comprehensive analysis

It may call:
- `function-decomposition.md` if duplicates are within large functions

## Safety Considerations

- Verify that extraction doesn't change behavior
- Check for side effects and dependencies
- Ensure parameter extraction doesn't lose information
- Consider performance impact of function calls
- Maintain backward compatibility