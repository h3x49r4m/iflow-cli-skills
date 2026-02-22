# Complexity Reduction Workflow

Workflow for reducing conditional and logical complexity in code.

## Overview

This workflow identifies complex conditional logic, deeply nested structures, and convoluted control flow, and suggests simplifications to improve readability and maintainability.

## Steps

### 1. Complexity Detection

**Goal**: Identify complex code structures in the codebase.

**Actions**:
- For each source file:
  - Read file content using `read_file`
  - Parse and analyze control flow:
    - Nested if/else statements
    - Switch/case statements
    - Ternary operators
    - Logical operators (&&, ||, !)
    - Loop nesting
  - Calculate complexity metrics:
    - Cyclomatic complexity
    - Nesting depth
    - Number of logical operators per line
    - Number of conditions in if statements
  - Identify complex patterns

**Output**: List of complex code structures with metrics.

### 2. Pattern Analysis

**Goal**: Categorize complexity patterns.

**Actions**:
For each complex structure:
- Identify the complexity pattern:
  - Nested conditionals (arrow code)
  - Complex boolean expressions
  - Long switch/case statements
  - Multiple early returns
  - Complex loop conditions
- Analyze the intent of the complex logic
- Identify simplification opportunities

**Output**: Categorized complexity patterns.

### 3. Simplification Strategy

**Goal**: Determine the best simplification approach.

**Actions**:
For each complex structure:
- Evaluate simplification techniques:
  - Guard clauses / early returns
  - Decompose complex conditions
  - Extract to helper functions
  - Use lookup tables / maps
  - Apply polymorphism
  - Use strategy pattern
  - Introduce state machine
- Select appropriate technique based on context
- Generate before/after examples

**Output**: Simplification strategy for each complex structure.

### 4. Impact Assessment

**Goal**: Assess the impact of proposed simplifications.

**Actions**:
For each simplification:
- Verify behavior is preserved
- Check for side effects
- Assess readability improvement
- Estimate performance impact
- Identify potential risks

**Output**: Impact assessment for each simplification.

### 5. Priority Scoring

**Goal**: Score simplifications by value.

**Actions**:
- Calculate impact based on:
  - Complexity reduction amount
  - Readability improvement
  - Maintainability improvement
- Calculate effort based on:
  - Lines of code changed
  - Complexity of transformation
  - Testing required
- Compute priority score

**Output**: Prioritized list of simplifications.

## Complexity Patterns and Solutions

### Nested Conditionals (Arrow Code)

**Problem**: Deeply nested if/else statements creating arrow-shaped code

**Detection**: Nesting depth > threshold (typically 3-4)

**Solution**: Guard clauses and early returns

**Example**:
```javascript
// Before
function processUser(user) {
  if (user) {
    if (user.isActive) {
      if (user.hasPermission) {
        if (user.emailVerified) {
          // do something
          return result;
        } else {
          return 'Email not verified';
        }
      } else {
        return 'No permission';
      }
    } else {
      return 'User not active';
    }
  } else {
    return 'No user';
  }
}

// After
function processUser(user) {
  if (!user) return 'No user';
  if (!user.isActive) return 'User not active';
  if (!user.hasPermission) return 'No permission';
  if (!user.emailVerified) return 'Email not verified';

  // do something
  return result;
}
```

### Complex Boolean Expressions

**Problem**: Long, complex boolean conditions that are hard to understand

**Detection**: Multiple logical operators in single condition

**Solution**: Extract to named boolean variables or functions

**Example**:
```javascript
// Before
if (user.age >= 18 && user.hasLicense && user.insurance && !user.suspended && vehicle.isRegistered && vehicle.inspectionValid) {
  // allow rental
}

// After
const isEligibleUser = user.age >= 18 && user.hasLicense && user.insurance && !user.suspended;
const isEligibleVehicle = vehicle.isRegistered && vehicle.inspectionValid;

if (isEligibleUser && isEligibleVehicle) {
  // allow rental
}
```

### Long Switch/Case Statements

**Problem**: Switch statements with many cases or complex logic in cases

**Detection**: Many cases or complex case logic

**Solution**: Use lookup tables, strategy pattern, or polymorphism

**Example**:
```javascript
// Before
function calculateBonus(employee) {
  switch (employee.level) {
    case 'junior':
      return employee.salary * 0.05;
    case 'mid':
      return employee.salary * 0.10;
    case 'senior':
      return employee.salary * 0.15;
    case 'lead':
      return employee.salary * 0.20;
    case 'manager':
      return employee.salary * 0.25;
    case 'director':
      return employee.salary * 0.30;
    default:
      return 0;
  }
}

// After
const bonusRates = {
  junior: 0.05,
  mid: 0.10,
  senior: 0.15,
  lead: 0.20,
  manager: 0.25,
  director: 0.30
};

function calculateBonus(employee) {
  const rate = bonusRates[employee.level] || 0;
  return employee.salary * rate;
}
```

### Multiple Return Points with Complex Logic

**Problem**: Multiple early returns with complex conditions

**Detection**: Multiple return statements with complex logic

**Solution**: Consolidate or use early return pattern consistently

**Example**:
```javascript
// Before
function validateOrder(order) {
  if (!order) {
    if (debug) {
      console.log('No order');
    }
    return false;
  }

  if (!order.items) {
    if (debug) {
      console.log('No items');
    }
    return false;
  }

  if (order.items.length === 0) {
    if (debug) {
      console.log('Empty items');
    }
    return false;
  }

  if (!order.customer) {
    if (debug) {
      console.log('No customer');
    }
    return false;
  }

  return true;
}

// After
function validateOrder(order) {
  const errors = [];

  if (!order) errors.push('No order');
  if (!order?.items) errors.push('No items');
  if (order?.items?.length === 0) errors.push('Empty items');
  if (!order?.customer) errors.push('No customer');

  if (errors.length > 0 && debug) {
    console.log(errors.join(', '));
  }

  return errors.length === 0;
}
```

## Output Format

```json
{
  "complex_structures": [
    {
      "type": "nested_conditionals" | "complex_boolean" | "long_switch" | "multiple_returns",
      "file": string,
      "function": string,
      "start_line": number,
      "end_line": number,
      "metrics": {
        "nesting_depth": number,
        "cyclomatic_complexity": number,
        "conditions_count": number,
        "logical_operators_count": number
      },
      "severity": "high" | "medium" | "low",
      "description": string,
      "simplification_strategy": {
        "technique": string,
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

- Optional chaining for nested property access
- Nullish coalescing for fallback values
- Destructuring for complex object handling

### Python

- Context managers for resource handling
- Dictionary comprehensions for lookups
- Decorators for cross-cutting concerns

### Java/C#

- Optional classes for null handling
- Stream API for complex transformations
- Builder pattern for complex object construction

## Integration

This workflow is called by:
- `code-analysis.md` as part of comprehensive analysis

It may call:
- `function-decomposition.md` if complex logic spans multiple functions

## Safety Considerations

- Ensure simplified logic produces same results
- Verify edge cases are handled
- Check for short-circuit evaluation differences
- Maintain error handling
- Preserve performance characteristics
- Test thoroughly after simplification