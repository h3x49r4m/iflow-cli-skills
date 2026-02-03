# Python Project Builder (TDD)

**Name**: python-project-builder-tdd

**Description**: A comprehensive skill for building Python projects following Test-Driven Development (TDD) methodology. Covers the full project lifecycle from product design to deployment using uv for package management.

**Trigger Conditions**:
This skill should be automatically invoked when:
- User requests to develop a Python application, library, or tool
- User asks to create a Python project
- User requests Python development with testing requirements
- User asks to "continue", "resume", or "continue working on" a project
- Keywords: "python", "develop", "create project", "build app", "tdd", "test-driven", "continue", "resume"

**Workflow Phases**:
1. **Planning** (01-planning/) - Feature breakdown, dependency mapping, effort estimation
2. **Architecture** (02-architecture/) - Module design, interface design, data flow
3. **Development** (03-development/) - TDD workflow, feature implementation, code standards
4. **Testing** (04-testing/) - Test strategy, coverage requirements, edge cases
5. **Quality Assurance** (05-quality-assurance/) - Feature verification, integration checks, performance validation
6. **Deployment** (06-deployment/) - Build process, deployment strategies

**Project Setup**:
- Use `uv` for package management
- Standard structure: `src/` for source code, `tests/` for tests
- Use `pytest` as the testing framework
- Follow TDD: Write tests first, then implement

**Tracking**:
- Track features in `FEATURES.md`
- Track test coverage in `test-coverage-tracker.md`
- Track bugs/issues in `bug-tracker.md`

**Key Commands**:
- `uv init` - Initialize project
- `uv add pytest` - Add pytest dependency
- `uv run pytest` - Run tests
- `uv run pytest --cov` - Run tests with coverage
- `uv build` - Build project

**Quality Standards**:
- Minimum 80% test coverage per feature
- All features must pass acceptance criteria
- Integration tests required for feature interactions
- Edge cases must be identified and tested

**Instructions**:

### When Starting a New Project:
1. Initialize project state in `.state/` directory
2. Create `project-state.md` with project information
3. Follow each phase sequentially
4. Use checklists to verify completion
5. Update trackers to monitor progress
6. Ensure all quality standards are met before deployment

### When Resuming an Existing Project:
1. **Check for Existing State**: Look for `.state/` directory
2. **Read Project State**: Load `project-state.md` to understand current status
3. **Read Current Feature**: Load `current-feature.md` to see what's being worked on
4. **Read Next Steps**: Load `next-steps.md` to see what to do next
5. **Check Checkpoints**: Review `checkpoints/` for any saved progress
6. **Resume Work**: Continue from the last checkpoint or next step
7. **Update State**: Update state files as progress is made

### State Persistence:
- **Project State**: `.state/project-state.md` - Overall project status
- **Current Feature**: `.state/current-feature.md` - Feature being worked on
- **Completed Checklist**: `.state/completed-checklist.md` - What's been done
- **Next Steps**: `.state/next-steps.md` - What to do next
- **Checkpoints**: `.state/checkpoints/` - Phase-specific checkpoints
- **Context**: `.state/context/` - Saved context and decisions

### Session Management:
- **Start Session**: Create session entry in `completed-checklist.md`
- **Save Checkpoint**: Save progress before pausing
- **Update Next Steps**: Update `next-steps.md` before ending
- **Document Context**: Save important context in `context/`
- **Clear Handoff**: Provide clear resume instructions

### Resume Commands:
- "continue working on [project]" - Resume project work
- "resume [feature]" - Resume specific feature
- "what's next?" - Show next steps
- "show progress" - Display project progress
- "pause" - Save current state and pause