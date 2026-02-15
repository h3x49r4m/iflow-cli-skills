# Testing Guidance Workflow

## Overview

The testing guidance phase provides users with structured, project-specific instructions for testing each feature systematically. It presents test scenarios, testing instructions, and collects results.

## Process

### 1. Present Feature for Testing

**Feature Display Format:**

```
🧪 Testing Feature <ID>: <Feature Name>

📖 Feature Description:
  <Detailed description from documentation or inferred from code>

📂 Category: <Category Name>
🔗 Location: <File path or component name>

🎯 Test Scenarios:
  1. Happy Path: <scenario description>
  2. Validation: <scenario description>
  3. Edge Case: <scenario description>
  4. Error Handling: <scenario description>

📋 Testing Instructions:
  <Project-specific testing steps>

💬 After testing, report results:
   - "evaluator pass feature <ID>" if all scenarios work correctly
   - "evaluator fail feature <ID> [details]" if any issues found
   - "evaluator partial feature <ID> [details]" if some scenarios fail
   - "evaluator skip feature <ID> [reason]" to skip this feature

Example responses:
  "evaluator pass feature 1"
  "evaluator fail feature 1: validation not working for invalid email"
  "evaluator partial feature 1: works on desktop, fails on mobile"
  "evaluator skip feature 1: feature not yet implemented"
```

### 2. Generate Test Scenarios

**Scenario Types:**

| Scenario Type | Purpose | Examples |
|---------------|---------|----------|
| **Happy Path** | Verify normal operation | Valid inputs, expected behavior |
| **Validation** | Verify input validation | Invalid formats, missing fields |
| **Edge Cases** | Verify boundary conditions | Empty inputs, maximum values |
| **Error Handling** | Verify error responses | Network errors, server errors |
| **Security** | Verify security measures | Unauthorized access, XSS prevention |
| **Performance** | Verify performance | Large datasets, concurrent users |

**Scenario Generation by Feature Type:**

#### User Registration
```
1. Happy Path: Register with valid email and strong password
2. Validation: Register with invalid email format
3. Validation: Register with weak password (< 8 chars)
4. Duplicate: Register with already existing email
5. Security: Verify password is hashed (not stored in plain text)
```

#### Data Search
```
1. Happy Path: Search with valid query string
2. Empty: Search with empty query (show all or error)
3. No Results: Search with non-existent term
4. Special Characters: Search with special characters
5. Case Sensitivity: Search with different case variations
```

#### File Upload
```
1. Happy Path: Upload valid file within size limit
2. Size Limit: Upload file exceeding max size
3. Invalid Type: Upload unsupported file type
4. Empty File: Upload empty (0-byte) file
5. Network: Test with slow/interrupted connection
```

#### API Endpoint
```
1. Happy Path: Valid request with correct parameters
2. Unauthorized: Request without authentication
3. Invalid Params: Request with invalid parameters
4. Not Found: Request for non-existent resource
5. Rate Limit: Exceed rate limit (if applicable)
```

### 3. Provide Testing Instructions

**Instructions by Project Type:**

#### Web Application
```
📋 Testing Instructions:

1. Start the application:
   npm run dev
   (or: python manage.py runserver, cargo run, etc.)

2. Navigate to the feature:
   Open browser to: http://localhost:3000/<route>
   (or follow navigation menu to: <Feature Name>)

3. Test each scenario:
   a) Fill out the form/fields
   b) Click the submit/action button
   c) Observe the response/behavior
   d) Verify expected outcome

4. Check for:
   - Correct behavior
   - Error messages (if applicable)
   - Loading states
   - Success notifications
   - Data persistence (if applicable)

5. Test on different browsers (optional):
   - Chrome, Firefox, Safari
   - Mobile browsers (if responsive)

💡 Tips:
   - Use browser DevTools to check network requests
   - Check console for JavaScript errors
   - Verify form validation feedback
```

#### CLI Tool
```
📋 Testing Instructions:

1. Navigate to project directory:
   cd /path/to/project

2. Run the command:
   ./myapp <command> [options]
   (or: npm run cli <command>, python -m myapp <command>)

3. Test each scenario:
   a) Provide valid inputs
   b) Provide invalid inputs
   c) Omit required parameters
   d) Test with flags/options

4. Check:
   - Output format (stdout)
   - Error messages (stderr)
   - Exit codes (0 = success, non-zero = error)
   - Help text

5. Verify:
   - Correct behavior for valid inputs
   - Appropriate error handling
   - Clear error messages

💡 Tips:
   - Use --help flag to see available options
   - Check exit codes with: echo $?
   - Capture output: ./myapp <cmd> > output.txt
```

#### Library
```
📋 Testing Instructions:

1. Create a test script:
   Create file: test_<feature>.js/py/rs

2. Import the library:
   const mylib = require('./src/mylib');
   (or: from mylib import MyLib)

3. Test each scenario:
   a) Call the function with valid inputs
   b) Call with invalid inputs
   c) Test edge cases
   d) Verify return values

4. Verify:
   - Correct return values
   - Proper error handling
   - Side effects (if any)
   - Performance (if applicable)

5. Run the test script:
   node test_<feature>.js
   (or: python test_<feature>.py)

💡 Tips:
   - Use console.log/print to inspect values
   - Test with various input types
   - Check documentation for expected behavior
```

#### Mobile App
```
📋 Testing Instructions:

1. Launch the mobile app:
   - iOS: Open in Simulator or device
   - Android: Open in Emulator or device
   - React Native: npm run ios / npm run android

2. Navigate to the feature:
   Follow app navigation to: <Feature Name>

3. Test each scenario:
   a) Tap buttons/interactions
   b) Fill out forms
   c) Test gestures (swipe, pinch, etc.)
   d) Test rotation (portrait/landscape)

4. Check:
   - UI rendering
   - Touch responsiveness
   - Loading states
   - Error handling
   - Network requests

5. Test on different screen sizes (if applicable):
   - Small phones
   - Large phones
   - Tablets

💡 Tips:
   - Use device/emulator debugging tools
   - Check network requests in DevTools
   - Test with poor network conditions
   - Test with app in background
```

### 4. Collect Test Results

**Result Types:**

| Result | Meaning | When to Use |
|--------|---------|-------------|
| **pass** | All scenarios work correctly | Feature fully functional |
| **fail** | Feature not working | Critical issues, feature broken |
| **partial** | Some scenarios fail | Edge cases, specific issues |
| **skip** | Feature not tested | Not implemented, not applicable |

**Result Format:**

```
User: evaluator pass feature 1

Evaluator:
  ✅ Feature 1: User Registration - PASSED

  📊 Progress: 1/20 features tested (5%)
  ✅ Passed: 1
  ❌ Failed: 0
  ⚠️ Partial: 0
  🚫 Skipped: 0

  📋 Next: Feature 2: User Login
     Say "evaluator test feature 2" to continue

  📁 State saved to: .state/evaluation.md
```

```
User: evaluator fail feature 3: email service not configured, no password reset emails sent

Evaluator:
  ❌ Feature 3: Password Reset - FAILED

  📝 Issue recorded:
     - Email service not configured
     - Users cannot receive password reset links

  🔴 Severity: CRITICAL

  📍 Location: src/services/email.js:45

  📊 Progress: 3/20 features tested (15%)
  ✅ Passed: 2
  ❌ Failed: 1
  ⚠️ Partial: 0
  🚫 Skipped: 0

  📋 Next: Feature 4: Profile Management
     Say "evaluator test feature 4" to continue

  📁 State saved to: .state/evaluation.md
```

```
User: evaluator partial feature 5: works on desktop, but logout button not clickable on mobile

Evaluator:
  ⚠️ Feature 5: User Logout - PARTIAL

  📝 Issues recorded:
     - Logout button not clickable on mobile devices
     - Mobile menu not closing after logout

  🟠 Severity: HIGH

  📍 Location: src/components/Navbar.js:34, src/components/MobileMenu.js:12

  📊 Progress: 5/20 features tested (25%)
  ✅ Passed: 3
  ❌ Failed: 1
  ⚠️ Partial: 1
  🚫 Skipped: 0

  📋 Next: Feature 6: Email Verification
     Say "evaluator test feature 6" to continue

  📁 State saved to: .state/evaluation.md
```

```
User: evaluator skip feature 10: feature not yet implemented according to documentation

Evaluator:
  🚫 Feature 10: Bulk Operations - SKIPPED

  📝 Reason: Feature not yet implemented

  📊 Progress: 10/20 features tested (50%)
  ✅ Passed: 7
  ❌ Failed: 2
  ⚠️ Partial: 1
  🚫 Skipped: 1

  📋 Next: Feature 11: Data Validation
     Say "evaluator test feature 11" to continue

  📁 State saved to: .state/evaluation.md
```

### 5. Determine Issue Severity

**Severity Criteria:**

| Severity | Definition | Examples |
|----------|------------|----------|
| **Critical** | Feature completely broken, security issue, data loss risk | Crash on startup, auth bypass, data corruption |
| **High** | Major functionality broken, significant usability issue | Core feature not working, critical path blocked |
| **Medium** | Feature partially working, minor usability issue | Edge case failure, incorrect error messages |
| **Low** | Cosmetic issues, minor enhancements | Spacing issues, inconsistent styling |

**Severity Assignment Logic:**

```
1. Check for security issues → Critical
2. Check for data loss/corruption → Critical
3. Check for crashes/fatal errors → Critical
4. Check for core functionality broken → High
5. Check for critical usability issues → High
6. Check for partial functionality → Medium
7. Check for edge cases → Medium
8. Check for cosmetic issues → Low
```

### 6. Extract Issue Location

**Location Extraction:**

When user reports issues, attempt to extract location information:

```
From user input: "evaluator fail feature 3: email service not configured in src/services/email.js"

Extracted:
  Feature: 3
  Issue: Email service not configured
  Location: src/services/email.js

From user input: "evaluator partial feature 5: logout button issue in Navbar component"

Extracted:
  Feature: 5
  Issue: Logout button issue
  Location: src/components/Navbar.js (inferred)
```

### 7. Update State File

After each test result, update `.state/evaluation.md`:

```markdown
# Evaluation State

Project: <project-name>
Started: <timestamp>
Last Updated: <timestamp>

## Metadata
Type: <project-type>
Stack: <technologies>

## Feature Checklist
| ID | Feature | Category | Status | Result | Details |
|----|---------|----------|--------|--------|---------|
| 1  | Feature 1 | Category | tested | pass   | -      |
| 2  | Feature 2 | Category | tested | pass   | -      |
| 3  | Feature 3 | Category | tested | fail   | Email not configured (src/services/email.js:45) |
| 4  | Feature 4 | Category | ⬜ Untested | - | - |
| 5  | Feature 5 | Category | tested | partial | Mobile issue (src/components/Navbar.js:34) |

## Issues
| ID | Severity | Feature | Description | Location |
|----|----------|---------|-------------|----------|
| 1  | critical | 3       | Email service not configured | src/services/email.js:45 |
| 2  | high     | 5       | Logout button not clickable on mobile | src/components/Navbar.js:34 |

## Progress
Total Features: 20
Tested: 5 (25%)
Passed: 3
Failed: 1
Partial: 1
Skipped: 0
```

### 8. Provide Progress Feedback

After each test, show progress:

```
📊 Evaluation Progress
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Total Features: 20
Tested: 5 (25%)

Status Breakdown:
  ✅ Passed: 3 (15%)
  ❌ Failed: 1 (5%)
  ⚠️ Partial: 1 (5%)
  🚫 Skipped: 0 (0%)

Issues Found:
  🔴 Critical: 1
  🟠 High: 0
  🟡 Medium: 0
  🟢 Low: 0

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Next: Feature 6: <Feature Name>
Say "evaluator test feature 6" to continue
Or "evaluator generate report" to generate report now
```

## Testing Best Practices

### For Users

1. **Test systematically**: Follow scenarios in order
2. **Document issues**: Be specific about what failed and why
3. **Test edge cases**: Don't just test happy paths
4. **Check logs**: Look at console/server logs for errors
5. **Test repeatedly**: Ensure consistent behavior
6. **Use DevTools**: Browser/CLI debugging tools are helpful

### For the Skill

1. **Clear instructions**: Provide step-by-step guidance
2. **Relevant scenarios**: Only include applicable scenarios
3. **Context-aware**: Tailor instructions to project type
4. **Progress tracking**: Keep user informed of progress
5. **Issue categorization**: Help prioritize fixes
6. **State persistence**: Allow resuming across sessions

## Exit Conditions

**Success:**
- Test result recorded
- State file updated
- Progress displayed
- Next feature suggested

**Warning:**
- Issue reported without location info
- Vague issue description

**Failure:**
- Invalid feature ID
- State file update failed

## Next Steps

After testing all features (or at any checkpoint), proceed to:
1. Report Generation Workflow
2. Generate comprehensive evaluation report
3. Provide prioritized recommendations