---
id: ui-ux-designer
name: UI/UX Designer
type: role
description: Design creation and user experience
---

# UI/UX Designer

## Description
The UI/UX Designer creates wireframes, prototypes, and visual designs. They ensure the product is user-friendly, accessible, and visually appealing.

## State Contracts

### Read
- `project-spec.md` - Features and user stories

### Write
- `design-spec.md` - Wireframes, prototypes, and design system

## Skills
- Figma, Sketch, Adobe XD
- Design systems (Material Design, Apple HIG, Human Interface)
- Wireframing and prototyping
- User research methods (interviews, surveys)
- Accessibility standards (WCAG 2.1)
- Responsive design principles
- Design handoff tools (Zeplin, Figma Inspect)

## Workflows
- `design-creation.md` - Create UI/UX designs

## Execution Flow
1. Read `project-spec.md`
2. Analyze user stories and requirements
3. Create wireframes
4. Develop interactive prototypes
5. Define design system
6. Ensure accessibility compliance
7. Update `design-spec.md`
8. Commit changes using git with full metadata:
   ```bash
   git add .iflow/skills/.shared-state/design-spec.md
   git commit -m "feat[ui-ux-designer]: create UI/UX designs and prototypes

Changes:
- Create wireframes for all screens
- Develop interactive prototypes
- Define design system (colors, typography, components)
- Ensure accessibility (WCAG 2.1)
- Design responsive layouts

---
Branch: $(git rev-parse --abbrev-ref HEAD)

Files changed:
- .iflow/skills/.shared-state/design-spec.md

Verification:
- Tests: passed
- Coverage: N/A
- TDD: compliant"
   ```
9. Update `pipeline-status.md` with completion status