# Feature Extraction Workflow

## Overview

The feature extraction phase builds a comprehensive feature checklist from multiple sources: documentation, test files, source code structure, and configuration files.

## Process

### 1. Extract Features from Documentation

**Documentation Sources:**

| Source | File Patterns | Extraction Strategy |
|--------|---------------|---------------------|
| **README** | README.md, README.rst, README.txt | Search for "Features:", "What it does:", sections describing functionality |
| **User Guides** | docs/user-guide.md, GUIDE.md, USAGE.md | Look for feature lists, tutorials, usage examples |
| **Changelog** | CHANGELOG.md, HISTORY.md, CHANGES.md | Extract feature additions, enhancements |
| **Feature Docs** | FEATURES.md, docs/features.md | Direct feature lists |
| **API Docs** | API.md, docs/api.md | Extract API endpoints/operations as features |
| **Roadmap** | ROADMAP.md, docs/roadmap.md | Extract planned features (mark as "not implemented") |

**Extraction Techniques:**

1. **Keyword-based Extraction:**
   - Search for headers: "Features", "Functionality", "Capabilities", "What it does"
   - Look for bullet points, numbered lists
   - Find section headers describing modules or components

2. **Pattern Recognition:**
   - Verb + Noun patterns: "User registration", "Data export", "Password reset"
   - Feature indicators: "Supports...", "Provides...", "Enables..."
   - Implementation details: "Allows users to...", "Enables..."

3. **Structure Analysis:**
   - Extract from table of contents
   - Parse section hierarchies
   - Identify feature categories

**Tools:**
- `read_file` - Read documentation files
- `search_file_content` - Search for feature patterns
- `web_fetch` - Fetch public documentation (if project is open source)

**Example Output:**
```
From README.md:
  - User registration and authentication
  - Profile management
  - Data CRUD operations
  - Search and filter
  - Export to CSV/PDF
  - Notifications
```

### 2. Extract Features from Test Files

**Test File Patterns:**

| Language | Test File Patterns | Test Structure |
|----------|-------------------|----------------|
| **JavaScript/TypeScript** | **/*.test.js, **/*.spec.ts, **/__tests__/**/*.js | describe() blocks, test() names |
| **Python** | **/test_*.py, **/tests/test_*.py | test_* functions, TestCase classes |
| **Rust** | **/*_test.rs, tests/*.rs | #[test] functions |
| **Go** | **/*_test.go | Test* functions |
| **Java** | **/*Test.java, **/*Tests.java | @Test methods |
| **Ruby** | **/*_test.rb, spec/**/*_spec.rb | test methods, it blocks |

**Extraction Strategies:**

1. **Test Name Analysis:**
   - Test names often describe the feature being tested
   - Remove "test_", "should_", "it " prefixes
   - Convert to feature names

2. **Test Organization:**
   - `describe()`/`context()` blocks often group related tests by feature
   - Class names in test classes often indicate feature
   - File names can indicate feature categories

3. **Test Content Analysis:**
   - Comments in tests describing functionality
   - Assertions indicating expected behavior
   - Setup/teardown code showing feature usage

**Examples:**

| Test Name | Extracted Feature |
|-----------|-------------------|
| `test_user_registration_success` | User Registration |
| `test_password_reset_with_valid_token` | Password Reset |
| `test_data_export_to_csv` | CSV Export |
| `test_api_search_endpoint_pagination` | Search Pagination |

**Tools:**
- `glob` - Find test files
- `read_file` - Analyze test content
- `search_file_content` - Extract test patterns

**Example Output:**
```
From tests/auth_test.js:
  - User Registration
  - User Login
  - Password Reset
  - Email Verification
  - Session Management

From tests/data_test.py:
  - Create Data Entry
  - Edit Data Entry
  - Delete Data Entry
  - Data Validation
```

### 3. Extract Features from Source Code Structure

**Directory Structure Analysis:**

| Directory | Feature Indicators |
|-----------|-------------------|
| `components/` | UI component names = features |
| `pages/`, `views/` | Page names = features |
| `routes/`, `api/` | Route paths = features |
| `cli/`, `bin/` | Command names = features |
| `models/` | Entity names = features (CRUD) |
| `services/` | Service names = features |
| `hooks/` | Hook names = features |
| `utils/` | Utility names = potential features |

**Component/Module Extraction:**

1. **React/Vue Components:**
   - Component file names: `UserProfile.tsx` → User Profile
   - Component exports: named exports = features
   - PropTypes/Interface definitions: feature indicators

2. **API Routes:**
   - Route paths: `/api/users` → User Management
   - HTTP methods: GET, POST, PUT, DELETE = CRUD operations
   - Route handlers: function names = features

3. **CLI Commands:**
   - Command definitions: `cmd = new Command()` → Command feature
   - Subcommands: nested commands = sub-features
   - Option definitions: optional features

4. **Models/Entities:**
   - Model definitions: class names = entities
   - Implied features: Create, Read, Update, Delete (CRUD)

**Tools:**
- `list_directory` - Scan directory structure
- `glob` - Find specific file patterns
- `read_file` - Analyze component/route definitions
- `search_file_content` - Search for feature indicators

**Example Output:**
```
From src/components/:
  - UserProfile (User Profile Management)
  - DataTable (Data Display)
  - SearchBar (Search Functionality)
  - ExportButton (Data Export)

From src/routes/:
  - /api/users (User API)
  - /api/data (Data API)
  - /api/auth (Authentication API)

From src/cli/:
  - init (Project Initialization)
  - build (Build Command)
  - deploy (Deployment Command)
```

### 4. Extract Features from Configuration Files

**Configuration Sources:**

| Config File | Feature Indicators |
|-------------|-------------------|
| **package.json** | scripts, bin field, dependencies |
| **routes.js/ts** | Route definitions |
| **router.js/ts** | Router configuration |
| **api.yaml/json** | API endpoint definitions |
| **swagger.yaml/json** | OpenAPI specifications |
| **commands/** | CLI command definitions |
| **menu.json** | Menu/navigation features |
| **features.json** | Feature flags/toggles |

**Extraction Techniques:**

1. **Route Definitions:**
   - Express routes: `app.get('/users', ...)`
   - React Router: `<Route path="/users" />`
   - FastAPI: `@app.get("/users")`
   - Flask: `@app.route('/users')`

2. **API Specifications:**
   - OpenAPI/Swagger endpoints
   - GraphQL schema definitions
   - gRPC service definitions

3. **CLI Commands:**
   - Command definitions in config files
   - Subcommand hierarchies
   - Command aliases

4. **Feature Flags:**
   - Feature toggle configurations
   - Environment-specific features
   - Beta/experimental features

**Tools:**
- `read_file` - Parse configuration files
- `search_file_content` - Extract route/command patterns

**Example Output:**
```
From routes/userRoutes.js:
  - GET /api/users (List Users)
  - POST /api/users (Create User)
  - GET /api/users/:id (Get User)
  - PUT /api/users/:id (Update User)
  - DELETE /api/users/:id (Delete User)

From package.json (bin):
  - myapp (Main CLI)
  - myapp-init (Init Command)
  - myapp-build (Build Command)
```

### 5. Deduplicate and Merge Features

**Deduplication Strategies:**

1. **Name Normalization:**
   - Convert to lowercase
   - Remove common prefixes/suffixes
   - Standardize naming conventions

2. **Similarity Matching:**
   - Compare feature names for similarity
   - Merge duplicates with combined descriptions
   - Keep most detailed description

3. **Hierarchy Building:**
   - Group related features
   - Create parent-child relationships
   - Organize by functionality

**Example:**

```
Duplicates:
  - "User Registration"
  - "User signup"
  - "Sign up new user"

Merged: "User Registration (Sign Up)"
```

### 6. Categorize Features

**Feature Categories:**

| Category | Description | Examples |
|----------|-------------|----------|
| **Core Features** | Essential functionality | Authentication, Data Management |
| **Authentication/Authorization** | User security | Login, Registration, Permissions |
| **Data Management** | CRUD operations | Create, Read, Update, Delete |
| **Search & Filter** | Data querying | Search, Filter, Sort |
| **Export/Import** | Data transfer | CSV Export, Import |
| **UI/UX Features** | User interface | Dark Mode, Responsive Design |
| **Notifications** | User alerts | Email, Push, In-app |
| **Integrations** | External services | Third-party APIs, Webhooks |
| **Reporting** | Data visualization | Charts, Reports, Dashboards |
| **Settings/Configuration** | App settings | Preferences, Config Management |

**Categorization Logic:**

1. **Keyword-based:**
   - "login", "register", "auth" → Authentication
   - "create", "delete", "update" → Data Management
   - "search", "filter" → Search & Filter
   - "export", "import" → Export/Import

2. **Context-based:**
   - Location in file structure
   - Related features grouping
   - Documentation categorization

3. **Manual Override:**
   - Allow user to adjust categories
   - Custom categories for specific projects

### 7. Assign Feature IDs

**ID Assignment Strategy:**

```
Features are numbered sequentially:
  1, 2, 3, 4, 5, ...

Within categories, maintain sequential numbering for easy reference.
```

### 8. Generate Feature Checklist

**Checklist Structure:**

```markdown
## Feature Checklist

| ID | Feature | Category | Status | Result | Details |
|----|---------|----------|--------|--------|---------|
| 1  | Feature Name | Category | ⬜ Untested | - | - |
| 2  | Feature Name | Category | ⬜ Untested | - | - |
| 3  | Feature Name | Category | ⬜ Untested | - | - |
```

**Status Values:**
- ⬜ Untested
- ✅ Tested (Passed)
- ❌ Tested (Failed)
- ⚠️ Tested (Partial)
- 🚫 Skipped

**Example Output:**

```
[FEATURE EXTRACTION] Building feature checklist...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 CORE FEATURES (4)
  ⬜ Feature 1: User Registration
  ⬜ Feature 2: User Login
  ⬜ Feature 3: Password Reset
  ⬜ Feature 4: Profile Management

📋 AUTHENTICATION (3)
  ⬜ Feature 5: Email Verification
  ⬜ Feature 6: Two-Factor Auth
  ⬜ Feature 7: Session Management

📋 DATA MANAGEMENT (6)
  ⬜ Feature 8: Create Data Entry
  ⬜ Feature 9: Edit Data Entry
  ⬜ Feature 10: Delete Data Entry
  ⬜ Feature 11: View Data Details
  ⬜ Feature 12: Bulk Operations
  ⬜ Feature 13: Data Validation

📋 SEARCH & FILTER (3)
  ⬜ Feature 14: Basic Search
  ⬜ Feature 15: Advanced Filters
  ⬜ Feature 16: Sort Options

📋 EXPORT/IMPORT (2)
  ⬜ Feature 17: CSV Export
  ⬜ Feature 18: Data Import

📋 UI/UX FEATURES (2)
  ⬜ Feature 19: Dark Mode
  ⬜ Feature 20: Responsive Design

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ Extracted 20 features from 4 sources:
  - 12 from documentation
  - 5 from test files
  - 3 from code structure

📁 State saved to: .state/evaluation.md
```

### 9. Update State File

Save feature checklist to `.state/evaluation.md`:

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
| 1  | Feature Name | Category | ⬜ Untested | - | - |
...

## Issues
[Generated during testing]

## Progress
Total Features: <N>
Tested: 0
Passed: 0
Failed: 0
Partial: 0
Skipped: 0
```

## Exit Conditions

**Success:**
- At least 1 feature extracted
- Features categorized
- Checklist generated
- State file updated

**Warning:**
- Few features extracted (< 3)
- Many uncategorized features (> 50%)

**Failure:**
- No features extracted
- State file update failed

## Next Steps

After successful feature extraction, proceed to:
1. Testing Guidance Workflow
2. Begin systematic feature testing
3. Track results in state file