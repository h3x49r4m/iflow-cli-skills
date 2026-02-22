# Refactoring Report Workflow

Workflow for generating comprehensive refactoring reports from analysis results.

## Overview

This workflow compiles refactoring findings from all analysis workflows into a comprehensive, actionable report that developers can use to guide their refactoring efforts.

## Steps

### 1. Collect Analysis Results

**Goal**: Gather results from all refactoring analysis workflows.

**Actions**:
- Load results from:
  - `code-analysis.md` workflow
  - `duplicate-detection.md` workflow
  - `constant-extraction.md` workflow
  - `function-decomposition.md` workflow
  - `dead-code-elimination.md` workflow
  - `complexity-reduction.md` workflow
- Validate and normalize data formats
- Merge related findings
- Remove duplicates

**Output**: Consolidated set of refactoring findings.

### 2. Categorization and Grouping

**Goal**: Organize findings for easier navigation and prioritization.

**Actions**:
- Group findings by:
  - Category (duplication, complexity, naming, etc.)
  - Severity (high, medium, low)
  - File/module
  - Priority score
- Create cross-references between related findings
- Identify dependencies between refactorings

**Output**: Organized findings with cross-references.

### 3. Executive Summary

**Goal**: Create high-level summary of refactoring opportunities.

**Actions**:
- Calculate aggregate statistics:
  - Total number of findings
  - Distribution by category
  - Distribution by severity
  - Estimated total effort
  - Expected improvements
- Identify top 5-10 highest priority items
- Highlight quick wins (high impact, low effort)
- Note any critical issues

**Output**: Executive summary with key metrics.

### 4. Detailed Findings

**Goal**: Present detailed information for each refactoring opportunity.

**Actions**:
For each finding:
- Include:
  - File path and line numbers
  - Current code (before)
  - Suggested code (after)
  - Explanation of the issue
  - Description of the fix
  - Impact and effort scores
  - Priority score
  - Related findings
  - Potential risks

**Output**: Detailed documentation of each finding.

### 5. Prioritized Action Plan

**Goal**: Create actionable refactoring plan.

**Actions**:
- Sort findings by priority score
- Group into phases:
  - Phase 1: Quick wins (high impact, low effort)
  - Phase 2: Medium impact refactorings
  - Phase 3: Complex refactorings
- Identify dependencies and order
- Estimate timeline for each phase
- Recommend testing strategy

**Output**: Prioritized, phased action plan.

### 6. Risk Assessment

**Goal**: Identify and document potential risks.

**Actions**:
- For each refactoring:
  - Identify potential risks
  - Assess risk severity
  - Suggest mitigation strategies
- Document system-wide risks:
  - Breaking changes
  - Performance impacts
  - Compatibility issues
- Recommend rollback strategy

**Output**: Risk assessment with mitigation strategies.

### 7. Report Generation

**Goal**: Generate final report in appropriate format(s).

**Actions**:
- Generate reports in multiple formats:
  - Markdown (for documentation)
  - JSON (for tool integration)
  - HTML (for interactive viewing)
- Include all sections:
  - Executive summary
  - Detailed findings
  - Action plan
  - Risk assessment
  - Appendices (raw data, etc.)

**Output**: Completed refactoring reports.

## Report Structure

### Executive Summary

- Overview of codebase health
- Key metrics and statistics
- Top priority items
- Quick wins
- Estimated effort and timeline

### Findings by Category

#### Duplicate Code
- Summary of duplication issues
- List of duplicate clusters
- Impact and effort estimates

#### Magic Literals
- Summary of hardcoded values
- List of constants to extract
- Priority ranking

#### Long/Complex Functions
- Summary of complexity issues
- List of functions to decompose
- Refactoring plans

#### Poor Naming
- Summary of naming issues
- List of identifiers to rename
- Suggested new names

#### Dead Code
- Summary of unused code
- List of code to remove
- Safety assessments

#### Complex Conditionals
- Summary of complexity issues
- List of simplifications
- Before/after examples

#### Code Smells
- Summary of anti-patterns
- List of smells detected
- Refactoring suggestions

### Prioritized Action Plan

#### Phase 1: Quick Wins
- Items with highest priority scores
- Expected timeline
- Testing strategy

#### Phase 2: Medium Impact
- Medium priority items
- Dependencies and ordering
- Timeline estimates

#### Phase 3: Complex Refactorings
- Large-scale changes
- Phased approach
- Risk mitigation

### Risk Assessment

- Potential risks by category
- Mitigation strategies
- Rollback plan

### Appendices

- Raw data and metrics
- Configuration used
- Tools and versions
- Additional resources

## Output Formats

### Markdown Report

Human-readable report with sections, code blocks, and tables.

### JSON Report

Machine-readable report for integration with other tools:

```json
{
  "metadata": {
    "generated_at": string,
    "project": string,
    "version": string,
    "tool_version": string
  },
  "summary": {
    "total_findings": number,
    "by_category": { },
    "by_severity": { },
    "high_priority_count": number,
    "estimated_effort_hours": number
  },
  "findings": [
    {
      "id": string,
      "category": string,
      "severity": string,
      "priority_score": number,
      "file": string,
      "line": number,
      "description": string,
      "suggestion": string,
      "before": string,
      "after": string,
      "impact_score": number,
      "effort_score": number,
      "risks": [string],
      "dependencies": [string]
    }
  ],
  "action_plan": {
    "phases": [
      {
        "phase": number,
        "name": string,
        "items": [string],
        "estimated_effort_hours": number,
        "timeline": string
      }
    ]
  }
}
```

### HTML Report

Interactive report with:
- Filtering and sorting
- Collapsible sections
- Syntax-highlighted code
- Export capabilities

## Integration

This workflow is called by:
- Main refactoring skill after all analysis workflows complete

It uses results from:
- All other refactoring workflows

## Best Practices

- **Clarity**: Use clear, concise language
- **Actionability**: Make suggestions specific and implementable
- **Context**: Provide enough context to understand issues
- **Evidence**: Show before/after code examples
- **Prioritization**: Help developers focus on high-impact items
- **Safety**: Highlight risks and mitigation strategies
- **Flexibility**: Allow for selective implementation

## Customization

The report can be customized based on:

- Team preferences and conventions
- Project-specific priorities
- Available resources and timeline
- Risk tolerance
- Integration with existing tools and processes