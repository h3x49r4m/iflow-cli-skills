---
name: talk
description: A conversation-only skill for discussing ideas, brainstorming, getting advice, and exploring concepts without any file modifications or system changes
version: 1.0.0
category: conversation
---

# talk

A conversation-only skill for discussing ideas, brainstorming, getting advice, and exploring concepts without any file modifications or system changes.

## Purpose

Pure conversational interaction - talk, discuss, analyze, explore. Nothing gets written or modified.

## Usage

```
talk [mode] [topic]
```

### Discussion Modes

#### Brainstorming
```
talk brainstorm "new feature ideas for X"
```
Structured brainstorming session:
- Divergent thinking phase (generate ideas)
- Convergent thinking phase (evaluate and prioritize)
- Idea capture and categorization

#### Code Review Discussion
```
talk review <file> [line-range]
```
Focused code review discussion:
- Identify potential issues
- Suggest improvements
- Discuss tradeoffs
- Provide alternative approaches

#### Architecture Discussion
```
talk architecture "component X design"
```
Architecture-focused discussion:
- Design patterns evaluation
- Technology stack considerations
- Scalability and performance
- Maintainability analysis

#### Problem Solving
```
talk solve <problem-description>
```
Structured problem-solving:
- Problem definition
- Root cause analysis
- Solution exploration
- Implementation planning

## Agent Configuration

**Agent Type:** `talk-agent`

**Available Tools:**
- `read_file` - read code/files for discussion
- `glob` - find files to discuss
- `search_file_content` - search to discuss
- `list_directory` - explore structure to discuss
- `web_search` - research for discussion
- `web_fetch` - look up references for discussion
- `image_read` - analyze images for discussion

**Excluded Tools:**
- No file modification tools (write_file, replace, xml_escape)
- No system command tools (run_shell_command)

## Behavior

- Read and analyze for discussion purposes only
- Never write, replace, or run commands
- Pure conversational output: insights, analysis, recommendations

## Context Persistence

### Session Memory
```
talk remember <key> <value>
```
Store information for future discussions:
```
talk remember project-stack "React, Node.js, PostgreSQL"
talk remember team-preferences "TypeScript strict mode enabled"
```

### Recall Context
```
talk recall [key]
```
Retrieve stored information:
```
talk recall project-stack
# Output: React, Node.js, PostgreSQL

talk recall
# Output: All stored context
```

### Export Discussion
```
talk export <filename>
```
Save current discussion to file:
```
talk export architecture-discussion.md
```

## Structured Discussion Frameworks

### SWOT Analysis
```
talk swot "project X"
```
Analyzes Strengths, Weaknesses, Opportunities, Threats:
- **Strengths**: Internal advantages
- **Weaknesses**: Internal limitations
- **Opportunities**: External possibilities
- **Threats**: External risks

### Pros/Cons Evaluation
```
talk pros-cons "use library X vs Y"
```
Structured comparison:
- Lists advantages of each option
- Identifies disadvantages
- Provides recommendation

### Decision Matrix
```
talk decide "option A vs B vs C" --criteria "cost, complexity, performance"
```
Weighted decision framework:
- Define evaluation criteria
- Score each option
- Calculate weighted scores
- Provide recommendation

### Root Cause Analysis (5 Whys)
```
talk 5-whys <problem>
```
Systematic root cause investigation:
- Ask "why?" five times
- Identify underlying cause
- Propose solutions

### Risk Assessment
```
talk risk-assess "feature X"
```
Evaluates potential risks:
- Identify risk categories (technical, business, operational)
- Assess likelihood and impact
- Propose mitigation strategies

## Usage

When invoked, the agent reads, searches, analyzes, and discusses - nothing gets written to disk.