# Discovery Workflow

## Overview

The discovery phase analyzes the project structure, identifies the project type, detects the technology stack, and prepares for feature extraction.

## Process

### 1. Locate Project Root

**Steps:**
1. Identify current working directory
2. Validate it's a valid project directory (has at least one of: package.json, requirements.txt, Cargo.toml, go.mod, pom.xml, etc.)
3. Record project root path

**Tools:**
- `list_directory` - Scan directory contents
- `read_file` - Read project metadata files

### 2. Detect Project Type

**Detection Logic:**

| Project Type | Detection Criteria |
|--------------|-------------------|
| **Web Application** | package.json (React/Vue/Angular), index.html, public/, webpack.config.js, vite.config.js, next.config.js |
| **CLI Tool** | package.json with `bin` field, setup.py entry points, Cargo.toml with `[[bin]]`, clap/argparse usage |
| **Library** | package.json without bin/dev scripts, pyproject.toml with `[project]` (not scripts), src/lib/ structure, library-focused config |
| **Mobile App** | ios/ and android/ directories, react-native.config.js, pubspec.yaml (Flutter), App.tsx (React Native) |
| **Desktop App** | electron/ directory, tauri.conf.json, electron-builder config |
| **Other** | Custom or hybrid project structures |

**Tools:**
- `glob` - Find indicator files
- `read_file` - Analyze configuration
- `list_directory` - Check directory structure

### 3. Identify Technology Stack

**Detection by File Type:**

| Technology | Indicator Files | Detected Info |
|------------|-----------------|---------------|
| **Node.js/JavaScript** | package.json, yarn.lock, pnpm-lock.yaml | Runtime, package manager, dependencies |
| **TypeScript** | tsconfig.json, .ts files | TypeScript version, compiler options |
| **Python** | requirements.txt, pyproject.toml, setup.py, Pipfile | Runtime version, dependencies |
| **Rust** | Cargo.toml, Cargo.lock | Rust version, dependencies |
| **Go** | go.mod, go.sum | Go version, dependencies |
| **Java** | pom.xml, build.gradle, build.gradle.kts | Java version, build tool |
| **Ruby** | Gemfile, Gemfile.lock | Ruby version, dependencies |
| **PHP** | composer.json | PHP version, dependencies |
| **C#/.NET** | .csproj, package.json, .NET CLI files | .NET version, dependencies |

**Framework Detection:**

| Framework | Indicators |
|-----------|------------|
| **React** | "react" in dependencies, .jsx/.tsx files, create-react-app structure |
| **Vue** | "vue" in dependencies, .vue files, vue.config.js |
| **Angular** | "angular" in dependencies, angular.json, .component.ts files |
| **Next.js** | "next" in dependencies, next.config.js, pages/ or app/ directory |
| **Nuxt** | "nuxt" in dependencies, nuxt.config.ts, pages/ directory |
| **Express** | "express" in dependencies, server.js/index.js with express usage |
| **Django** | "django" in requirements, manage.py, settings.py |
| **Flask** | "flask" in requirements, app.py/__init__.py with flask usage |
| **Rails** | "rails" in Gemfile, config/application.rb, db/migrate/ |
| **Spring Boot** | "spring-boot" in pom.xml/build.gradle, @SpringBootApplication |
| **FastAPI** | "fastapi" in requirements, uvicorn usage |

**Tools:**
- `read_file` - Parse configuration files
- `search_file_content` - Search for framework usage patterns
- `glob` - Find framework-specific files

### 4. Analyze Project Structure

**Key Directories to Examine:**

| Directory | Purpose | What to Look For |
|-----------|---------|------------------|
| `src/` | Source code | Modules, components, services |
| `lib/` | Library code | Exposed APIs, utilities |
| `app/` | Application code | Main application logic |
| `tests/`, `test/`, `__tests__/` | Test files | Feature indicators, test coverage |
| `components/` | UI components (web apps) | Feature names, props |
| `pages/`, `views/` | Pages/routes (web apps) | Route names, page features |
| `routes/`, `api/` | API routes (web apps) | Endpoint names, operations |
| `cli/`, `bin/` | CLI commands | Command names, options |
| `models/`, `entities/` | Data models | Entities, relationships |
| `services/` | Business logic | Service names, operations |
| `config/` | Configuration | Environment settings, feature flags |
| `docs/`, `doc/` | Documentation | Feature lists, user guides |

**Tools:**
- `list_directory` - Scan directory structure
- `glob` - Find specific file patterns
- `read_file` - Analyze file contents

### 5. Read Documentation

**Documentation Sources:**

| File | Purpose | Extractable Information |
|------|---------|------------------------|
| `README.md` | Project overview | Features, usage, setup |
| `README.rst` | Project overview | Features, usage, setup |
| `CHANGELOG.md` | Version history | Feature additions, changes |
| `docs/` | Detailed docs | Feature descriptions, guides |
| `CONTRIBUTING.md` | Contribution guide | Development practices |
| `ARCHITECTURE.md` | Architecture | System design, components |
| `API.md` | API documentation | Endpoints, operations |
| `USER_GUIDE.md` | User guide | Feature usage, workflows |
| `FEATURES.md` | Feature list | Detailed feature descriptions |

**Tools:**
- `read_file` - Read documentation files
- `search_file_content` - Search for feature keywords

### 6. Identify Build and Test Commands

**Package Manager Detection:**

| Package Manager | Lock File | Install Command | Test Command |
|----------------|-----------|-----------------|--------------|
| **npm** | package-lock.json | `npm install` | `npm test` |
| **yarn** | yarn.lock | `yarn install` | `yarn test` |
| **pnpm** | pnpm-lock.yaml | `pnpm install` | `pnpm test` |
| **pip** | requirements.txt | `pip install -r requirements.txt` | `pytest` |
| **poetry** | poetry.lock | `poetry install` | `poetry run pytest` |
| **cargo** | Cargo.lock | `cargo fetch` | `cargo test` |
| **go** | go.sum | `go mod download` | `go test` |
| **gradle** | - | `./gradlew build` | `./gradlew test` |
| **mvn** | - | `mvn install` | `mvn test` |

**Extract from package.json (Node.js):**
```json
{
  "scripts": {
    "start": "...",
    "dev": "...",
    "build": "...",
    "test": "...",
    "test:watch": "..."
  }
}
```

**Extract from pyproject.toml (Python):**
```toml
[project.scripts]
[tool.pytest.ini_options]
[tool.poetry.scripts]
```

**Extract from Cargo.toml (Rust):**
```toml
[package]
[[bin]]

[dev-dependencies]
```

**Tools:**
- `read_file` - Parse configuration files
- `search_file_content` - Search for script sections

### 7. Summarize Discovery

**Output Format:**

```
[DISCOVERY] Project Analysis Complete
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📁 Project Root: /path/to/project

🏷️  Project Type: <web-app|cli|library|mobile-app|desktop-app|other>

🔧 Technology Stack:
  - Runtime: <Node.js, Python, Rust, Go, etc.>
  - Language: <JavaScript, TypeScript, Python, etc.>
  - Framework: <React, Vue, Django, Express, etc.>
  - Package Manager: <npm, yarn, poetry, cargo, etc.>

📂 Key Directories:
  - src/ - Source code
  - tests/ - Test files
  - ...

📚 Documentation Found:
  ✓ README.md
  ✓ docs/
  ✗ No API documentation

🏗️  Build Commands:
  - Install: <command>
  - Start: <command>
  - Build: <command>
  - Test: <command>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Tools:**
- Read-only operations (no file modifications)

## State Persistence

After discovery, save initial state to `.state/evaluation.md`:

```markdown
# Evaluation State

Project: <project-name>
Started: <timestamp>
Last Updated: <timestamp>

## Metadata
Type: <project-type>
Stack: <technologies>
Root: <project-root-path>

## Build Commands
Install: <command>
Start: <command>
Build: <command>
Test: <command>

## Feature Checklist
[Generated in next phase]

## Issues
[Generated during testing]

## Progress
Total Features: 0
Tested: 0
Passed: 0
Failed: 0
Partial: 0
Skipped: 0
```

## Exit Conditions

**Success:**
- Project type detected
- Technology stack identified
- At least one documentation file found
- Build commands identified (or inferred)

**Failure:**
- No valid project detected (no config files found)
- Cannot determine project type
- Cannot identify technology stack

## Next Steps

After successful discovery, proceed to:
1. Feature Extraction Workflow
2. Generate feature checklist
3. Begin testing guidance