# Function Decomposition Workflow

Workflow for identifying and decomposing overly long or complex functions.

## Overview

This workflow identifies functions that are too long, complex, or have too many responsibilities, and suggests breaking them down into smaller, focused functions.

## Steps

### 1. Function Detection

**Goal**: Identify all functions/methods in the codebase.

**Actions**:
- For each source file:
  - Read file content using `read_file`
  - Parse to extract function/method definitions
  - Collect metadata:
    - Function name and signature
    - Start and end line numbers
    - Parameters and return type
    - Visibility modifiers (if applicable)
    - Class/module context

**Output**: List of all functions with metadata.

### 2. Size Analysis

**Goal**: Measure function size and complexity.

**Actions**:
For each function:
- Calculate line count (excluding comments and blank lines)
- Calculate cyclomatic complexity (number of decision points)
- Calculate maximum nesting depth
- Count number of parameters
- Count number of local variables
- Count number of return statements
- Measure cognitive complexity

**Output**: Complexity metrics for each function.

### 3. Threshold Comparison

**Goal**: Compare metrics against configured thresholds.

**Actions**:
- Load thresholds from `config/thresholds.json`
- Compare each function's metrics against thresholds:
  - Lines of code > threshold → candidate for splitting
  - Cyclomatic complexity > threshold → candidate for simplification
  - Nesting depth > threshold → candidate for flattening
  - Parameter count > threshold → candidate for parameter object
- Flag functions exceeding multiple thresholds as high priority

**Output**: List of functions exceeding thresholds.

### 4. Responsibility Analysis

**Goal**: Identify functions with multiple responsibilities.

**Actions**:
For each flagged function:
- Analyze code structure and control flow
- Identify distinct logical sections:
  - Input validation
  - Data transformation
  - Business logic
  - Error handling
  - Logging
  - I/O operations
- Check for "God Function" anti-patterns
- Identify feature envy (using other objects' data extensively)

**Output**: Responsibility breakdown for each function.

### 5. Decomposition Strategy

**Goal**: Determine how to decompose each function.

**Actions**:
For each function requiring decomposition:
- Identify natural split points:
  - Logical sections with clear boundaries
  - Repeated code patterns
  - Independent operations
- Suggest extraction points:
  - Extract validation logic → validateXxx() functions
  - Extract data transformation → transformXxx() functions
  - Extract business logic → processXxx() functions
  - Extract error handling → handleXxxError() functions
- Determine appropriate function signatures
- Plan data flow between extracted functions
- Generate before/after code examples

**Output**: Detailed decomposition plan for each function.

### 6. Priority Scoring

**Goal**: Score functions by refactoring value.

**Actions**:
- Calculate impact based on:
  - Number of thresholds exceeded
  - How much each threshold is exceeded
  - Frequency of function calls
  - Test coverage (if available)
- Calculate effort based on:
  - Number of functions to extract
  - Complexity of data flow between functions
  - Number of parameters to manage
- Compute priority score

**Output**: Prioritized list of functions to decompose.

## Decomposition Patterns

### Extract Method

**When**: Function has a section of code that can be grouped logically

**Pattern**:
```javascript
// Before
function processOrder(order) {
  // validate
  if (!order.id) throw new Error('No ID');
  if (!order.items || order.items.length === 0) throw new Error('No items');

  // transform
  const items = order.items.map(item => ({
    ...item,
    total: item.price * item.quantity
  }));

  // process
  const result = calculate(items);

  return result;
}

// After
function processOrder(order) {
  validateOrder(order);
  const items = transformOrderItems(order.items);
  const result = calculate(items);
  return result;
}

function validateOrder(order) {
  if (!order.id) throw new Error('No ID');
  if (!order.items || order.items.length === 0) throw new Error('No items');
}

function transformOrderItems(items) {
  return items.map(item => ({
    ...item,
    total: item.price * item.quantity
  }));
}
```

### Replace Conditional with Polymorphism

**When**: Function has complex conditional logic based on type

**Pattern**:
```javascript
// Before
function calculateArea(shape) {
  if (shape.type === 'circle') {
    return Math.PI * shape.radius * shape.radius;
  } else if (shape.type === 'rectangle') {
    return shape.width * shape.height;
  } else if (shape.type === 'triangle') {
    return 0.5 * shape.base * shape.height;
  }
}

// After
class Circle {
  calculateArea() {
    return Math.PI * this.radius * this.radius;
  }
}

class Rectangle {
  calculateArea() {
    return this.width * this.height;
  }
}

class Triangle {
  calculateArea() {
    return 0.5 * this.base * this.height;
  }
}
```

### Introduce Parameter Object

**When**: Function has too many parameters (parameter clump)

**Pattern**:
```javascript
// Before
function createUser(name, email, age, address, phone, country) {
  // implementation
}

// After
function createUser(userConfig) {
  // implementation
}

const config = {
  name, email, age, address, phone, country
};
createUser(config);
```

## Output Format

```json
{
  "complex_functions": [
    {
      "file": string,
      "function_name": string,
      "start_line": number,
      "end_line": number,
      "metrics": {
        "line_count": number,
        "cyclomatic_complexity": number,
        "nesting_depth": number,
        "parameter_count": number,
        "return_count": number
      },
      "thresholds_exceeded": [string],
      "severity": "high" | "medium" | "low",
      "responsibilities": [
        {
          "type": string,
          "start_line": number,
          "end_line": number,
          "description": string
        }
      ],
      "decomposition_plan": {
        "suggested_functions": [
          {
            "name": string,
            "extract_from": [number, number],
            "parameters": [string],
            "return_type": string
          }
        ],
        "refactored_example": string
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

- Extract callback functions
- Break down promise chains
- Extract reducer logic

### Python

- Extract generator expressions
- Split list comprehensions
- Extract context managers

### Java/C#

- Extract private helper methods
- Break down switch statements
- Extract validation to validator classes

## Integration

This workflow is called by:
- `code-analysis.md` as part of comprehensive analysis

It may call:
- `complexity-reduction.md` if conditionals are complex

## Safety Considerations

- Ensure extracted functions maintain same behavior
- Verify data flow between functions
- Check for side effects and state mutations
- Maintain error handling
- Preserve performance characteristics
- Ensure test coverage exists before refactoring