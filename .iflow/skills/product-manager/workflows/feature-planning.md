# Feature Planning Workflow

## Objective
Plan and prioritize features based on requirements.

## Steps

1. **Analyze Requirements**
   - Read `project-spec.md`
   - Understand all requirements and constraints
   - Identify dependencies between features

2. **Prioritize Features**
   - Use MoSCoW method (Must have, Should have, Could have, Won't have)
   - Or use RICE scoring (Reach, Impact, Confidence, Effort)
   - Consider business value and technical complexity

3. **Create User Stories**
   - Write user stories in INVEST format:
     - **I**ndependent
     - **N**egotiable
     - **V**aluable
     - **E**stimable
     - **S**mall
     - **T**estable
   - Format: "As a [user], I want [feature], so that [benefit]"

4. **Define Acceptance Criteria**
   - Clear criteria for each user story
   - Testable and measurable
   - Edge cases and error conditions

5. **Create Feature Roadmap**
   - Sequence features by priority and dependencies
   - Define release milestones
   - Estimate effort for each feature

6. **Document Everything**
   - Update `project-spec.md` with prioritized features and user stories
   - Include acceptance criteria for each story

## Output
- Updated `project-spec.md` with prioritized features and user stories
- Commit changes using git-manage
- Updated `pipeline-status.md` with completion status