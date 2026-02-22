# Constant Extraction Workflow

Workflow for identifying and extracting magic numbers and strings into named constants.

## Overview

This workflow detects hardcoded literals in code and suggests extracting them into named constants with meaningful names to improve code readability and maintainability.

## Steps

### 1. Literal Detection

**Goal**: Identify all magic literals in the codebase.

**Actions**:
- For each source file:
  - Read file content using `read_file`
  - Use regex patterns to find:
    - Numeric literals (integers, floats, scientific notation)
    - String literals (single quotes, double quotes, template literals)
    - Boolean literals (true, false)
  - Exclude literals in:
    - Comments and documentation
    - Test files and test data
    - Configuration files
    - Already defined as constants
  - Store with metadata (file, line, context)

**Output**: List of detected literals with locations.

### 2. Context Analysis

**Goal**: Analyze the context of each literal to understand its purpose.

**Actions**:
For each detected literal:
- Examine surrounding code (3-5 lines before and after)
- Identify usage pattern (comparison, calculation, API call, etc.)
- Determine semantic meaning (timeout, buffer size, error code, etc.)
- Check if literal appears multiple times across codebase
- Note any related literals (e.g., 100 and 200 might be related)

**Output**: Annotated literals with semantic context.

### 3. Frequency Analysis

**Goal**: Group repeated literals and calculate their frequency.

**Actions**:
- Group identical literals across all files
- Count occurrences for each literal
- Identify literal values that appear frequently
- Calculate distribution across files and functions

**Output**: Frequency statistics for each literal value.

### 4. Constant Naming Suggestion

**Goal**: Suggest appropriate names for extracted constants.

**Actions**:
For each literal (or group of repeated literals):
- Analyze semantic meaning from context
- Generate candidate constant names following conventions:
  - UPPER_SNAKE_CASE for constants
  - Descriptive and self-documenting
  - Include units when applicable (e.g., MAX_RETRIES, TIMEOUT_MS)
- Check for existing similar constants to avoid conflicts
- Prioritize names that explain the "why" not just the "what"

**Output**: Suggested constant names for each literal.

### 5. Extraction Location Suggestion

**Goal**: Determine where to define the extracted constants.

**Actions**:
For each constant:
- Analyze scope of usage:
  - Local to single function → function-level constant
  - Used within single file → file-level constant
  - Used across multiple files → module/package-level constant
  - Used across entire project → global config/constants file
- Suggest appropriate location (top of file, constants module, config file)
- Consider language-specific conventions

**Output**: Recommended location for each constant.

### 6. Priority Scoring

**Goal**: Score constants by extraction value.

**Actions**:
- Calculate impact based on:
  - Frequency of occurrence
  - Importance (affects behavior vs. cosmetic)
  - Clarity improvement (obvious vs. cryptic value)
- Calculate effort based on:
  - Number of occurrences to replace
  - Number of files affected
  - Complexity of determining appropriate scope
- Compute priority score

**Output**: Prioritized list of constants to extract.

## Detection Patterns

### High Priority Literals

- Numbers that appear 3+ times
- String messages that appear 2+ times
- Magic numbers without obvious meaning (42, 3.14159, 1024)
- Error codes and status codes
- Timeout values and retry counts
- Configuration values (buffer sizes, limits)

### Medium Priority Literals

- Numbers that appear 2 times
- Single occurrence but cryptic values
- API endpoint URLs and paths
- File paths and directory names

### Low Priority Literals

- Obvious values (0, 1, -1 for simple operations)
- String literals for logging/debugging
- Test data and mock values
- One-time use values with clear context

## Output Format

```json
{
  "literal_groups": [
    {
      "value": string,
      "type": "number" | "string" | "boolean",
      "occurrences": number,
      "files_affected": number,
      "severity": "high" | "medium" | "low",
      "locations": [
        {
          "file": string,
          "line": number,
          "context": string
        }
      ],
      "suggested_name": string,
      "suggested_location": {
        "file": string,
        "line": number,
        "scope": "function" | "file" | "module" | "global"
      },
      "semantic_meaning": string,
      "before_example": string,
      "after_example": string,
      "impact_score": number,
      "effort_score": number,
      "priority_score": number
    }
  ]
}
```

## Language-Specific Patterns

### JavaScript/TypeScript

```javascript
// Before
if (status === 200 && timeout < 5000) {
  retry(3);
}

// After
const HTTP_STATUS_OK = 200;
const DEFAULT_TIMEOUT_MS = 5000;
const MAX_RETRIES = 3;

if (status === HTTP_STATUS_OK && timeout < DEFAULT_TIMEOUT_MS) {
  retry(MAX_RETRIES);
}
```

### Python

```python
# Before
if size > 1024 and retries < 3:
    return False

# After
MAX_SIZE_BYTES = 1024
MAX_RETRIES = 3

if size > MAX_SIZE_BYTES and retries < MAX_RETRIES:
    return False
```

### Java

```java
// Before
if (buffer.length > 4096 && attempts > 5) {
    return -1;
}

// After
private static final int BUFFER_SIZE = 4096;
private static final int MAX_ATTEMPTS = 5;

if (buffer.length > BUFFER_SIZE && attempts > MAX_ATTEMPTS) {
    return -1;
}
```

## Integration

This workflow is called by:
- `code-analysis.md` as part of comprehensive analysis

## Safety Considerations

- Ensure constant extraction doesn't change semantics
- Verify that literal values are truly constant (not calculated)
- Check for edge cases where literal might need to vary
- Consider whether value should be configurable
- Maintain backward compatibility