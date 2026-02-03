# Python Project Builder (TDD)

**Name**: python-project-builder-tdd

**Description**: A comprehensive skill for building Python projects following Test-Driven Development (TDD) methodology. Covers the full project lifecycle from product design to deployment using uv for package management.

**Trigger Conditions**:
This skill should be automatically invoked when:
- User requests to develop a Python application, library, or tool
- User asks to create a Python project
- User requests Python development with testing requirements
- Keywords: "python", "develop", "create project", "build app", "tdd", "test-driven"

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
When this skill is invoked:
1. Read all phase files to understand the full workflow
2. Follow each phase sequentially
3. Use checklists to verify completion
4. Update trackers to monitor progress
5. Ensure all quality standards are met before deployment