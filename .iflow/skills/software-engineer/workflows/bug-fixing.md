# Bug Fixing Workflow

## Objective
Fix bugs in the application (frontend and/or backend).

## Steps

1. **Analyze the Bug**
   - Read bug report
   - Understand expected vs actual behavior
   - Identify affected components or endpoints
   - Determine root cause

2. **Reproduce the Bug**
   - Set up test environment
   - Reproduce the bug consistently
   - Document reproduction steps
   - Identify conditions that trigger the bug

3. **Locate the Issue**
   - Review relevant code
   - Check logs and error messages
   - Use debugging tools
   - Identify the exact location of the bug

4. **Write Regression Test First (TDD)**
   - Write test that reproduces the bug BEFORE fixing
   - Ensure test fails initially (RED phase)

5. **Implement the Fix (TDD)**
   - Write minimal code to make test pass (GREEN phase)
   - Ensure minimal changes
   - Follow coding standards

6. **Refactor for Clean Code (TDD)**
   - Apply SOLID principles
   - Ensure DRY (Don't Repeat Yourself)
   - Follow KISS (Keep It Simple, Stupid)
   - Keep functions under 50 lines
   - Single responsibility per function
   - Use meaningful variable and function names

7. **Test the Fix**
   - Run regression test to verify it passes
   - Test the fix locally
   - Verify the bug is resolved
   - Check for side effects
   - Run full test suite to ensure no regressions

8. **Review and Refine**
   - Review the changes
   - Ensure clean code principles followed
   - Ensure functions are short and focused
   - Ensure code quality

7. **Update Documentation**
   - Update `implementation.md` if needed
   - Update `api-docs.md` if API was affected
   - Document the bug and fix

## Output
- Bug fix implemented
- Regression tests added
- Updated documentation
- Commit changes using git-manage
- Updated `pipeline-status.md` with completion status