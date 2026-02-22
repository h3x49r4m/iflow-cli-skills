# Dead Code Elimination Workflow

Workflow for identifying and removing unused code from the codebase.

## Overview

This workflow identifies code that is not being used (dead code) including unused imports, variables, functions, and classes, and suggests their removal to reduce code bloat and improve maintainability.

## Steps

### 1. Code Inventory

**Goal**: Create a comprehensive inventory of all code definitions.

**Actions**:
- For each source file:
  - Read file content using `read_file`
  - Parse and collect all definitions:
    - Imports and require statements
    - Function declarations
    - Method declarations
    - Class declarations
    - Variable declarations (const, let, var)
    - Interface/Type definitions
    - Enum definitions
  - Store with metadata:
    - Definition name and type
    - File path and line number
    - Visibility (public, private, protected)
    - Scope (module, class, function)

**Output**: Complete inventory of all code definitions.

### 2. Usage Analysis

**Goal**: Track all usages of each definition across the codebase.

**Actions**:
For each definition in the inventory:
- Search for all references across all files using `search_file_content`
- Build usage graph:
  - Which files import/use each definition
  - Which functions/methods call each function
  - Which expressions reference each variable
- Count total occurrences
- Identify test files that reference the definition
- Track indirect usage (through exports, re-exports)

**Output**: Usage statistics for each definition.

### 3. Dead Code Identification

**Goal**: Identify definitions with no usages.

**Actions**:
For each definition:
- Check if usage count is zero
- Verify it's not exported (exports might be used externally)
- Check if it's part of a public API
- Verify it's not dynamically accessed (e.g., via string keys)
- Check if it's used in configuration or metadata
- Flag as dead code if truly unused

**Output**: List of unused definitions.

### 4. Unused Import Detection

**Goal**: Specifically identify unused imports.

**Actions**:
For each file:
- Collect all import statements
- For each imported symbol:
  - Search for usages within the same file
  - Check if it's re-exported
  - Verify it's not used in type annotations
- Identify import statements with no used symbols
- Check for duplicate imports

**Output**: List of unused imports per file.

### 5. Impact Analysis

**Goal**: Assess the impact of removing dead code.

**Actions**:
For each dead code candidate:
- Check if removing it breaks tests
- Verify it's not part of a public API
- Check for references in documentation
- Look for usage in build scripts or configuration
- Identify dependencies (other code that depends on it)
- Determine if it's safe to remove

**Output**: Impact assessment for each dead code candidate.

### 6. Removal Suggestions

**Goal**: Generate safe removal suggestions.

**Actions**:
For each dead code candidate:
- If safe to remove:
  - Suggest removal of entire definition
  - Update related imports if necessary
- If potentially unsafe:
  - Suggest review and manual verification
  - Note potential external usages
- Generate before/after examples
- Group related removals together

**Output**: Prioritized removal suggestions.

### 7. Priority Scoring

**Goal**: Score dead code by removal value.

**Actions**:
- Calculate impact based on:
  - Lines of code to remove
  - Number of unused imports
  - Clarity improvement
- Calculate effort based on:
  - Complexity of removal
  - Need for verification
  - Potential side effects
- Compute priority score

**Output**: Prioritized list of dead code to remove.

## Dead Code Categories

### Unused Imports

**Detection**: Import statements with no references in the file

**Priority**: High (easy to remove, clear benefit)

**Example**:
```javascript
// Before
import { useState, useEffect, useMemo } from 'react';

export function MyComponent() {
  const [state, setState] = useState(null);
  useEffect(() => {
    // ...
  }, []);
  return <div>{state}</div>;
}

// After
import { useState, useEffect } from 'react';

export function MyComponent() {
  const [state, setState] = useState(null);
  useEffect(() => {
    // ...
  }, []);
  return <div>{state}</div>;
}
```

### Unused Functions/Methods

**Detection**: Functions/methods with no calls anywhere in the codebase

**Priority**: Medium (requires verification)

**Example**:
```javascript
// Before
export function calculateTax(amount, rate) {
  return amount * rate;
}

export function calculateDiscount(amount, percentage) {
  return amount * (percentage / 100);
}

// Only calculateTax is used, calculateDiscount is unused
```

### Unused Classes

**Detection**: Classes with no instantiations or static method calls

**Priority**: Medium (requires verification)

### Unused Variables

**Detection**: Variables that are declared but never read

**Priority**: Low (might be intended for future use)

### Unused Parameters

**Detection**: Function parameters that are never used in the function body

**Priority**: Low (might be part of interface)

## Output Format

```json
{
  "dead_code": [
    {
      "type": "import" | "function" | "class" | "variable" | "parameter",
      "name": string,
      "file": string,
      "line": number,
      "severity": "high" | "medium" | "low",
      "usage_count": number,
      "is_exported": boolean,
      "is_public_api": boolean,
      "safety_assessment": {
        "safe_to_remove": boolean,
        "reasons": [string],
        "risks": [string]
      },
      "suggestion": {
        "action": "remove" | "review",
        "description": string,
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

- Check for dynamic imports
- Verify default exports vs named exports
- Check for usage in JSX
- Look for usage in template literals

### Python

- Check for __all__ exports
- Verify dunder methods
- Check for usage in decorators
- Look for usage in type hints

### Java/C#

- Check for reflection usage
- Verify public interfaces
- Check for usage in annotations
- Look for usage in configuration files

## Integration

This workflow is called by:
- `code-analysis.md` as part of comprehensive analysis

## Safety Considerations

- **False Positives**: Code might be used in ways not detectable by static analysis
- **External Usage**: Public APIs might be used by external consumers
- **Dynamic Access**: Code might be accessed via reflection or dynamic strings
- **Build-Time Usage**: Code might be used in build scripts or tooling
- **Documentation**: Code might be referenced in documentation

**Best Practices**:
- Always verify with tests before removing
- Check git history for when code was last modified
- Look for TODO or FIXME comments
- Consider the intent (might be placeholder for future features)
- Run full test suite after removal
- Consider deprecation instead of removal for public APIs