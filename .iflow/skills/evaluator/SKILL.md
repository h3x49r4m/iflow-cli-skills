---
name: evaluator
description: Guides users through systematic, feature-by-feature testing and evaluation of any project with comprehensive reporting
version: 1.0.0
category: quality-assurance
---

# Evaluator Skill

Guides users through systematic, feature-by-feature testing and evaluation of any project with comprehensive reporting.

## Purpose

Provides a structured, user-guided approach to thoroughly test and evaluate any project - web applications, CLI tools, libraries, mobile apps, or any other software project. The skill discovers features, guides testing, tracks progress, and generates comprehensive evaluation reports.

## Agent Configuration

**Agent Type:** `evaluator-agent`

**Available Tools:**
- `read_file` - Read project files for analysis (README, config, tests, source code)
- `list_directory` - Explore project structure
- `glob` - Find specific file types (tests, configs, feature files)
- `search_file_content` - Search for feature indicators, test patterns, documentation
- `web_search` - Look up public project documentation
- `web_fetch` - Fetch reference documentation
- `image_read` - Analyze screenshots provided by user for issue documentation

**Excluded Tools:**
- No file modification tools (write_file, replace, xml_escape)
- No system command tools (run_shell_command)

**Note:** The skill only writes to `.state/evaluation.md` and `.state/evaluation-report.md` for state persistence and report generation.

## Behavior

- Read and analyze project structure and documentation
- Extract and organize feature list from multiple sources
- Guide user through systematic testing of each feature
- Track testing progress and results
- Generate comprehensive evaluation reports
- Never modify project files or execute project commands

## Usage

### Start Evaluation
```
evaluator start
```

Initiates project evaluation:
1. Discovers project structure and technology stack
2. Extracts features from documentation, tests, and code
3. Generates feature checklist
4. Saves state to `.state/evaluation.md`
5. Presents first feature for testing

### Test Specific Feature
```
evaluator test feature <number>
```

Guides user through testing a specific feature:
- Shows feature description
- Provides test scenarios (happy path, edge cases, error handling)
- Offers testing instructions based on project type
- Collects test results (pass/fail/partial with details)

### Automated Testing
```
evaluator test auto [--parallel] [--coverage]
```

Runs automated tests for all features:
- `--parallel`: Run tests in parallel for faster execution
- `--coverage`: Generate coverage report alongside results

**Automated Test Execution:**
- Discovers existing test files for each feature
- Runs test suite automatically
- Captures test results and coverage data
- Generates pass/fail status without manual intervention

### Skip Feature
```
evaluator skip feature <number> [reason]
```

Marks a feature as skipped with optional reason.

### Report Result
```
evaluator pass feature <number>
evaluator fail feature <number> [details]
evaluator partial feature <number> [details]
```

Records test result for a feature:
- **pass**: All scenarios work correctly
- **fail**: Feature not working (provide details)
- **partial**: Some scenarios fail (provide details)

### View Status
```
evaluator status
evaluator show checklist
```

Shows current evaluation progress and feature checklist.

### Generate Report
```
evaluator generate report
```

Creates comprehensive evaluation report in `.state/evaluation-report.md`:
- Executive summary
- Feature test results
- Issues discovered (with severity levels)
- Quality metrics
- Prioritized recommendations

### Resume Evaluation
```
evaluator resume
```

Resumes evaluation from saved state in `.state/evaluation.md`.

### List Issues
```
evaluator list issues
evaluator list issues [critical|high|medium|low]
```

Shows discovered issues, optionally filtered by severity.

## Workflow

### Phase 1: Discovery
```
[DISCOVERY] Analyzing project structure...
  ✓ Found: package.json / requirements.txt / Cargo.toml
  ✓ Found: README.md / docs/
  ✓ Found: src/ / lib/ / app/
  ✓ Found: tests/ / __tests__ / test/
  ✓ Found: config files
  ✓ Project type detected: <web-app|cli|library|mobile-app|other>
  ✓ Technology stack: <detected frameworks, languages>
```

**Discovery Process:**
1. Identify project root and structure
2. Detect project type based on file patterns
3. Identify technology stack from config files
4. Parse README and documentation for feature lists
5. Analyze test files for feature indicators
6. Scan source code for modules, components, endpoints

### Phase 2: Feature Extraction
```
[FEATURE EXTRACTION] Building feature checklist...
  ✓ Extracted 15 features from documentation
  ✓ Identified 12 features from test files
  ✓ Found 8 UI components / 6 API endpoints / 4 CLI commands
  Total features to test: 25

[CHECKLIST] Feature Test Checklist
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 CORE FEATURES (5)
  ⬜ Feature 1: <name> - Status: ⬜ Untested
  ⬜ Feature 2: <name> - Status: ⬜ Untested
  ...

📋 <CATEGORY> (N)
  ⬜ Feature X: <name> - Status: ⬜ Untested
  ...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Feature Sources:**
- **Documentation**: README, docs/, inline documentation
- **Test Files**: Test names, test descriptions
- **Code Structure**: Modules, components, API endpoints, CLI commands
- **Config Files**: Routes, commands, plugins
- **User Stories**: If available

**Feature Organization:**
- Core Features (essential functionality)
- Authentication/Authorization
- Data Management (CRUD operations)
- UI/UX Features
- Integration Features
- Advanced Features

### Phase 3: Testing Guidance
```
🧪 Testing Feature 1: <Feature Name>

📖 Feature Description:
  <Description from documentation or inferred from code>

🎯 Test Scenarios:
  1. Happy Path: <scenario description>
  2. Validation: <scenario description>
  3. Edge Case: <scenario description>
  4. Error Handling: <scenario description>

📋 Testing Instructions:
  <Project-specific testing steps>
  <Examples: start server, navigate URL, run command, etc.>

💬 After testing, report results:
   - "pass" if all scenarios work correctly
   - "fail [details]" if any issues found
   - "partial [details]" if some scenarios fail

Example responses:
  "evaluator pass feature 1"
  "evaluator fail feature 1: validation not working for invalid input"
  "evaluator partial feature 1: works on desktop, fails on mobile"
```

**Testing Templates by Project Type:**

**Web Application:**
1. Start application: `<start command>`
2. Navigate to: `<URL or route>`
3. Interact with: `<UI elements>`
4. Observe: `<expected behavior>`
5. Test scenarios: `<happy path, validation, errors>`

**CLI Tool:**
1. Run command: `<command syntax>`
2. Provide input: `<stdin or arguments>`
3. Check output: `<stdout, stderr>`
4. Verify exit code: `<expected code>`
5. Test scenarios: `<valid input, invalid input, edge cases>`

**Library:**
1. Import library: `<import statement>`
2. Create test script: `<sample code>`
3. Call functions: `<with various inputs>`
4. Verify results: `<expected outputs>`
5. Test scenarios: `<normal usage, edge cases, error handling>`

**Mobile App:**
1. Launch application
2. Navigate to feature: `<screen path>`
3. Interact with: `<UI elements>`
4. Test scenarios: `<happy path, gestures, rotation, network conditions>`

### Phase 4: State Tracking
```
📁 State saved to: .state/evaluation.md

Contents:
- Project metadata (name, type, stack)
- Feature checklist with statuses
- Test results and observations
- Issues discovered (with severity)
- Testing progress
- Timestamps
```

**State File Structure:**
```markdown
# Evaluation State

Project: <project-name>
Started: <timestamp>
Last Updated: <timestamp>

## Metadata
Type: <web-app|cli|library|mobile-app|other>
Stack: <technologies>

## Feature Checklist
| ID | Feature | Category | Status | Result | Details |
|----|---------|----------|--------|--------|---------|
| 1  | <name>  | <cat>    | tested | pass   | -      |
| 2  | <name>  | <cat>    | tested | fail   | <issue> |
| 3  | <name>  | <cat>    | skipped| -      | <reason> |

## Issues
| ID | Severity | Feature | Description | Location |
|----|----------|---------|-------------|----------|
| 1  | critical | <name>  | <desc>      | <file:line> |

## Progress
Total Features: <N>
Tested: <X> (<Y>%)
Passed: <A>
Failed: <B>
Partial: <C>
Skipped: <D>
```

### Phase 5: Report Generation
```
📊 PROJECT EVALUATION REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Project: <project-name>
Evaluated: <date>
Features Tested: <X>/<N> (<Y>%)

EXECUTIVE SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Overall Status: <emoji> <STATUS>
Critical Issues: <N>
High Priority Issues: <N>
Medium Priority Issues: <N>

FEATURE TEST RESULTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ PASSED (<count>/<total>)
  • Feature 1
  • Feature 2
  ...

❌ FAILED (<count>/<total>)
  • Feature X - <reason>
  • Feature Y - <reason>
  ...

⚠️ PARTIAL (<count>/<total>)
  • Feature A - <reason>
  • Feature B - <reason>
  ...

⬜ SKIPPED (<count>/<total>)
  • Feature M - <reason>
  • Feature N - <reason>
  ...

ISSUES DISCOVERED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔴 CRITICAL (<count>)
  1. <Issue> - <location>

🟠 HIGH PRIORITY (<count>)
  1. <Issue> - <location>

🟡 MEDIUM PRIORITY (<count>)
  1. <Issue> - <location>

🟢 LOW PRIORITY (<count>)
  1. <Issue> - <location>

QUALITY METRICS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Feature Completeness: <X>% (<tested>/<total> features tested)
Test Coverage: <Y>% (existing tests cover <n>/<total> features)
Reliability: <Z>% (<passed>/<tested> features fully working)
UX Assessment: <W>% (based on partial/fail results)

RECOMMENDATIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎯 IMMEDIATE (This Sprint)
  1. <priority issue>
  2. <priority issue>

📅 SHORT-TERM (Next Sprint)
  1. <issue>
  2. <issue>

🔮 LONG-TERM (Future)
  1. <improvement>
  2. <improvement>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📁 Report saved to: .state/evaluation-report.md
📁 State saved to: .state/evaluation.md
```

## Project Type Detection

The skill automatically detects project type based on file patterns:

| Project Type | Indicators |
|--------------|------------|
| **Web Application** | package.json with React/Vue/Angular, index.html, public/, webpack.config.js, vite.config.js |
| **CLI Tool** | package.json with bin field, setup.py entry points, Cargo.toml with [[bin]], CLI arguments parser |
| **Library** | package.json without bin/dev scripts, pyproject.toml with library configuration, src/lib/ structure |
| **Mobile App** | ios/, android/ directories, React Native configs, Flutter project structure |
| **Desktop App** | Electron config, Tauri config, desktop-specific dependencies |
| **Other** | Custom project structures |

## Technology Stack Detection

| Technology | Config Files |
|------------|--------------|
| **Node.js/JavaScript** | package.json, yarn.lock, pnpm-lock.yaml |
| **Python** | requirements.txt, pyproject.toml, setup.py, Pipfile |
| **Rust** | Cargo.toml, Cargo.lock |
| **Go** | go.mod, go.sum |
| **Java** | pom.xml, build.gradle |
| **Ruby** | Gemfile, Gemfile.lock |
| **PHP** | composer.json |
| **C#/.NET** | .csproj, package.json |
| **Frameworks**: React, Vue, Angular, Django, Flask, Express, Rails, etc. |

## Issue Severity Levels

| Severity | Definition | Examples | Triage Priority |
|----------|------------|----------|-----------------|
| **Critical** | Feature completely broken, security issue, data loss risk | Crash on startup, authentication bypass, data corruption | P0 - Immediate (24h) |
| **High** | Major functionality broken, significant usability issue | Core feature not working, critical path blocked | P1 - Urgent (72h) |
| **Medium** | Feature partially working, minor usability issue | Edge case failure, incorrect error messages | P2 - High (1 week) |
| **Low** | Cosmetic issues, minor enhancements | Spacing issues, inconsistent styling | P3 - Normal (next sprint) |

## Severity-Based Triage Workflow

### Automatic Issue Creation
```
evaluator triage create-issues
```

Creates GitHub issues for discovered problems with appropriate severity labels:
- Critical issues: `bug`, `critical`, `p0`
- High issues: `bug`, `high`, `p1`
- Medium issues: `bug`, `medium`, `p2`
- Low issues: `enhancement`, `low`, `p3`

### Triage Dashboard
```
evaluator triage dashboard
```

Shows triage status:
```
🔴 CRITICAL (2) - P0 - Must fix within 24h
   [ ] Issue #1: Authentication bypass
   [ ] Issue #2: Data corruption on delete

🟠 HIGH (5) - P1 - Must fix within 72h
   [ ] Issue #3: Core feature not working
   ...

🟡 MEDIUM (8) - P2 - High priority
   ...

🟢 LOW (12) - P3 - Normal priority
   ...
```

### Issue Assignment
```
evaluator triage assign <severity> <assignee>
```

Auto-assign issues by severity:
```
evaluator triage critical @senior-dev
evaluator triage high @team-lead
evaluator triage medium @junior-dev
```

## Quality Metrics

### Feature Completeness
```
(Total Features Tested / Total Features Found) × 100
```

### Test Coverage (Existing Tests)
```
(Features with Tests / Total Features) × 100
```

### Reliability
```
(Fully Passing Features / Tested Features) × 100
```

### UX Assessment
Qualitative assessment based on:
- Failed/partial features related to usability
- Mobile responsiveness issues
- Accessibility concerns
- Error message quality
- Overall user experience

## State Persistence

State is maintained in `.state/evaluation.md` at the **project root**:

**Critical:** State files are ALWAYS maintained at the project root (`PROJECT_ROOT/.state/`), NOT in the skill directory. The `.iflow/skills/evaluator/.state/` directory serves only as a template.

**State Update Behavior:**
- After discovery → Initial state file created
- After each test → Feature status updated
- After report generation → Report file created
- On resume → State loaded from file

## Integration with Other Skills

- **git-manage**: Could check if issues are in recent commits, validate issue locations
- **tdd-enforce**: Could validate if failing features have corresponding tests
- **dev-team**: Could be invoked to fix discovered issues after evaluation
- **talk**: Useful for discussing evaluation results and recommendations

## CI/CD Integration

### Automated Regression Testing

Add to CI pipeline for continuous evaluation:

```yaml
- name: Run Evaluator
  run: |
    iflow evaluator test auto --parallel --coverage
    iflow evaluator generate report
    # Upload report as artifact
    iflow evaluator upload report
```

### Scheduled Evaluations

Run evaluator on schedule to detect regressions:

```yaml
# .github/workflows/nightly-evaluation.yml
name: Nightly Evaluation
on:
  schedule:
    - cron: '0 2 * * *'  # 2 AM daily

jobs:
  evaluate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run full evaluation
        run: |
          iflow evaluator test auto --parallel --coverage
          iflow evaluator generate report
      - name: Upload report
        uses: actions/upload-artifact@v3
        with:
          name: evaluation-report
          path: .state/evaluation-report.md
```

### Issue Tracking Integration

Automatically create issues for discovered problems:

```yaml
- name: Create Issues
  run: |
    iflow evaluator list issues critical | xargs -I {} gh issue create --title "{}" --body "Auto-detected by evaluator"
```

## Exit Codes

- `0` - Evaluation completed successfully
- `1` - Evaluation in progress
- `2` - No state file found (use `evaluator start`)
- `3` - Invalid feature number
- `4` - Report generation failed

## Best Practices

1. **Start with discovery**: Always run `evaluator start` to initialize evaluation
2. **Test systematically**: Follow feature order, don't skip unless necessary
3. **Document issues**: Provide clear details for failed/partial features
4. **Generate reports early**: Run `evaluator generate report` at any checkpoint
5. **Resume when needed**: Use `evaluator resume` to continue across sessions
6. **Prioritize fixes**: Focus on critical and high-priority issues first

## Example Session

```
User: evaluator start

Evaluator:
  🔍 Starting Project Evaluation...

  [DISCOVERY] Analyzing project structure...
    ✓ Found: package.json
    ✓ Found: README.md
    ✓ Found: src/ directory
    ✓ Found: tests/ directory
    ✓ Project type: Web Application (React + Node.js)
    ✓ Technology stack: React, Express, MongoDB

  [FEATURE EXTRACTION] Building feature checklist...
    ✓ Extracted 12 features from documentation
    ✓ Identified 8 features from test files
    Total features to test: 20

  [CHECKLIST] Feature Test Checklist
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  📋 CORE FEATURES (4)
    ⬜ Feature 1: User Registration
    ⬜ Feature 2: User Login
    ⬜ Feature 3: Password Reset
    ⬜ Feature 4: Profile Management

  📋 DATA MANAGEMENT (6)
    ⬜ Feature 5: Create Data Entry
    ⬜ Feature 6: Edit Data Entry
    ⬜ Feature 7: Delete Data Entry
    ⬜ Feature 8: Search Data
    ⬜ Feature 9: Filter Data
    ⬜ Feature 10: Export Data

  [... more features ...]

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  💬 Ready to start testing!
     Say "evaluator test feature 1" or "start" to begin with Feature 1
     Say "evaluator skip feature 1" to mark as skipped
     Say "evaluator show checklist" to view full status
     Say "evaluator generate report" at any time

  📁 State saved to: .state/evaluation.md

User: evaluator test feature 1

Evaluator:
  🧪 Testing Feature 1: User Registration

  📖 Feature Description:
    Allows new users to create an account with email and password.

  🎯 Test Scenarios:
    1. Happy Path: Register with valid email and password
    2. Validation: Register with invalid email format
    3. Validation: Register with weak password (< 8 chars)
    4. Duplicate: Register with already existing email

  📋 Testing Instructions:
    1. Start the application: npm run dev
    2. Navigate to http://localhost:3000/register
    3. Fill out the registration form
    4. Test each scenario above

  💬 After testing, report results:
     - "evaluator pass feature 1" if all scenarios work correctly
     - "evaluator fail feature 1 [details]" if any issues found
     - "evaluator partial feature 1 [details]" if some scenarios fail

User: evaluator pass feature 1

Evaluator:
  ✅ Feature 1: User Registration - PASSED

  📊 Progress: 1/20 features tested (5%)
  📋 Next: Feature 2: User Login
     Say "evaluator test feature 2" to continue

  📁 State saved to: .state/evaluation.md

User: evaluator test feature 3

Evaluator:
  🧪 Testing Feature 3: Password Reset

  📖 Feature Description:
    Allows users to reset their password via email.

  🎯 Test Scenarios:
    1. Happy Path: Request password reset with valid email
    2. Validation: Request with non-existent email
    3. Link: Use valid reset link
    4. Expired: Use expired reset link

  📋 Testing Instructions:
    1. Navigate to http://localhost:3000/forgot-password
    2. Enter email and submit
    3. Check email for reset link
    4. Test each scenario above

  💬 After testing, report results:
     - "evaluator pass feature 3" if all scenarios work correctly
     - "evaluator fail feature 3 [details]" if any issues found
     - "evaluator partial feature 3 [details]" if some scenarios fail

User: evaluator fail feature 3: email not being sent, no reset link received

Evaluator:
  ❌ Feature 3: Password Reset - FAILED

  📝 Issue recorded:
     - Email service not configured or not working
     - Users cannot receive password reset links

  🔴 Severity: CRITICAL

  📊 Progress: 3/20 features tested (15%)
     ✅ Passed: 2
     ❌ Failed: 1

  📋 Next: Feature 4: Profile Management
     Say "evaluator test feature 4" to continue

  📁 State saved to: .state/evaluation.md

User: evaluator generate report

Evaluator:
  📊 PROJECT EVALUATION REPORT
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Project: my-web-app
  Evaluated: 2026-02-15
  Features Tested: 3/20 (15%)

  EXECUTIVE SUMMARY
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Overall Status: ⚠️ NEEDS IMPROVEMENT
  Critical Issues: 1
  High Priority Issues: 0
  Medium Priority Issues: 0

  FEATURE TEST RESULTS
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✅ PASSED (2/20)
    • User Registration
    • User Login

  ❌ FAILED (1/20)
    • Password Reset - Email service not configured

  ⬜ SKIPPED (17/20)
    • 17 features not yet tested

  ISSUES DISCOVERED
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  🔴 CRITICAL (1)
    1. Password Reset: Email service not configured (src/services/email.js)

  RECOMMENDATIONS
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  🎯 IMMEDIATE (This Sprint)
    1. Configure email service for password reset

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  📁 Report saved to: .state/evaluation-report.md
  📁 State saved to: .state/evaluation.md
```

## File Structure

```
.iflow/skills/
└── evaluator/
    ├── SKILL.md
    ├── workflows/
    │   ├── discovery.md          # How to analyze a new project
    │   ├── feature-extraction.md # How to build feature checklist
    │   ├── testing-guidance.md   # How to guide user testing
    │   └── reporting.md          # How to generate reports
    └── .state/
        └── .gitkeep
```

## Implementation Notes

The evaluator skill uses:
- File system tools (read_file, list_directory, glob) for project analysis
- Search tools (search_file_content) for feature and test pattern detection
- Web tools (web_search, web_fetch) for public project documentation
- State management in `.state/evaluation.md` for progress tracking
- Template-based report generation in `.state/evaluation-report.md`
- Project type detection heuristics based on file patterns
- Technology stack detection from configuration files
- Severity-based issue categorization
- Quality metrics calculation