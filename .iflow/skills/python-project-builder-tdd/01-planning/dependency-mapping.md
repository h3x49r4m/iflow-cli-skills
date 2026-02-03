# Dependency Mapping Guide

## Purpose
This guide explains how to map feature dependencies to determine the optimal implementation order.

## Types of Dependencies

### 1. Hard Dependencies
Feature A **requires** Feature B to be implemented first.
- Feature A cannot function without Feature B
- Example: "Edit task" requires "Add task" to exist

### 2. Soft Dependencies
Feature A **benefits from** Feature B but can work independently.
- Feature A can be implemented without Feature B
- Example: "Filter tasks" benefits from "List tasks" but can be developed independently

### 3. External Dependencies
Feature requires external services, APIs, or libraries.
- Must be available during development and testing
- Example: "Send email notification" requires SMTP server or email API

## Dependency Mapping Process

### Step 1: List All Features
Create a comprehensive list of all identified features.

### Step 2: Identify Dependencies
For each feature, identify:
- What other features it depends on (internal)
- What external services it depends on (external)
- What data it requires from other features

### Step 3: Create Dependency Graph
Map relationships between features:
```
Feature A
  ├── Feature B (hard dependency)
  │   └── Feature C (hard dependency)
  └── Feature D (soft dependency)
```

### Step 4: Determine Implementation Order
Use topological sorting to determine implementation order:
1. Start with features that have no dependencies (leaf nodes)
2. Move to features whose dependencies are complete
3. Continue until all features are ordered

### Step 5: Identify Critical Path
Find the longest chain of hard dependencies - this is your critical path.
Features on the critical path determine the minimum project timeline.

### Step 6: Identify Parallel Opportunities
Find features that can be developed in parallel:
- Features with no shared dependencies
- Features that only depend on completed features

## Dependency Documentation Template

For each feature, document dependencies:

```markdown
## Feature: [Feature Name]

### Internal Dependencies (Hard)
- [ ] Feature Name (ID: F001) - Must be implemented first

### Internal Dependencies (Soft)
- [ ] Feature Name (ID: F002) - Optional, can be implemented later

### External Dependencies
- [ ] Service/API Name - Version requirements
- [ ] Library Name - Version requirements

### Blocks
- [ ] Feature Name (ID: F003) - This feature blocks Feature F003
```

## Example

**Features**:
- F001: Add task
- F002: Edit task
- F003: Delete task
- F004: Mark task complete
- F005: List tasks
- F006: Filter tasks by status

**Dependency Graph**:
```
F001: Add task (no dependencies)
F002: Edit task → depends on F001
F003: Delete task → depends on F001
F004: Mark complete → depends on F001
F005: List tasks (no dependencies)
F006: Filter tasks → depends on F005
```

**Implementation Order** (parallel opportunities):
1. F001 and F005 (can be done in parallel)
2. F002, F003, F004 (can be done in parallel after F001)
3. F006 (after F005)

**Critical Path**: F001 → F002 (or any dependent feature)

## Best Practices

1. **Minimize Dependencies**: Design features to be as independent as possible
2. **Clear Interfaces**: Define clear interfaces between features to reduce coupling
3. **Early Validation**: Validate dependencies early to avoid blocking later
4. **Mock External Dependencies**: Use mocks for external dependencies during development
5. **Document Changes**: Update dependency maps when features change

## Tools

- **Mermaid**: For visualizing dependency graphs
- **Dot/Graphviz**: For complex dependency visualizations
- **Spreadsheet**: For tracking dependencies and status