# Dev-Team Automated Workflow Implementation

## Configuration Management

All thresholds, constants, and configuration values are externalized to avoid hardcoding:

### config/quality-gates.json
```json
{
  "thresholds": {
    "coverage": {
      "lines": 80,
      "branches": 70,
      "functions": 75
    },
    "security": {
      "maxVulnerabilities": 0
    },
    "architecture": {
      "maxCriticalViolations": 0
    }
  },
  "remediation": {
    "testSuite": "Fix failing tests before proceeding",
    "coverageThresholds": "Increase test coverage to meet thresholds",
    "tddCompliance": "Ensure test-first workflow is followed",
    "architecture": "Fix critical architecture violations",
    "security": "Address security vulnerabilities",
    "accessibility": "Fix accessibility issues to meet WCAG 2.1 AA"
  }
}
```

### config/project.json
```json
{
  "techStackPreferences": {
    "web": {
      "frontend": "React",
      "backend": "Node.js",
      "styling": "Bootstrap"
    },
    "cli": {
      "language": "Python"
    }
  },
  "defaults": {
    "port": 3000,
    "timeout": 30000,
    "retries": 3
  }
}
```

## Core Orchestration Logic

### 1. Auto-Initialize Project State

When project requirements are received:

```typescript
async function initializeProject(requirements: string): Promise<ProjectSpec> {
  // Extract project type (web, mobile, cli, library, game)
  const projectType = detectProjectType(requirements)

  // Parse features and constraints
  const features = extractFeatures(requirements)
  const constraints = extractConstraints(requirements)

  // Load project configuration
  const projectConfig = loadConfig('config/project.json')

  // Generate tech stack recommendation (data-driven, not hardcoded)
  const techStack = recommendTechStack(projectType, features, constraints, projectConfig)

  // Create project specification
  const spec: ProjectSpec = {
    status: 'initialized',
    type: projectType,
    requirements: requirements,
    features: features,
    constraints: constraints,
    techStack: techStack,
    scope: estimateScope(features),
    deliverables: generateDeliverables(features)
  }

  // Persist to state file
  await writeStateFile('project-spec.md', spec)

  return spec
}
```

### 2. Auto-Breakdown Tasks

```typescript
async function breakdownTasks(spec: ProjectSpec): Promise<Task[]> {
  const tasks: Task[] = []
  
  // Break down by feature
  for (const feature of spec.features) {
    const featureTasks = generateFeatureTasks(feature, spec.techStack)
    tasks.push(...featureTasks)
  }
  
  // Add infrastructure tasks
  const infraTasks = generateInfrastructureTasks(spec.techStack)
  tasks.push(...infraTasks)
  
  // Add quality assurance tasks
  const qaTasks = generateQATasks(spec.features)
  tasks.push(...qaTasks)
  
  // Set dependencies
  setTaskDependencies(tasks)
  
  // Set priorities
  setTaskPriorities(tasks)
  
  // Persist to state file
  await writeStateFile('sprint-planner.md', { tasks, status: 'planned' })
  
  return tasks
}
```

### 3. Agent Dispatcher

```typescript
class AgentDispatcher {
  private agents: Map<string, Agent> = new Map()
  
  constructor() {
    this.agents.set('frontend', new FrontendDeveloperAgent())
    this.agents.set('backend', new BackendDeveloperAgent())
    this.agents.set('qa', new QAEngineerAgent())
    this.agents.set('tech-lead', new TechLeadAgent())
    this.agents.set('devops', new DevOpsEngineerAgent())
    this.agents.set('project-manager', new ProjectManagerAgent())
  }
  
  async dispatch(task: Task): Promise<TaskResult> {
    const agentType = this.determineAgentType(task)
    const agent = this.agents.get(agentType)
    
    if (!agent) {
      throw new Error(`No agent found for task type: ${agentType}`)
    }
    
    // Execute task with TDD cycle enforcement
    const result = await this.executeWithTDD(task, agent)
    
    // Verify quality gates
    await this.verifyQualityGates(task, result)
    
    // Commit with git-manage format
    await this.commitWithGitManage(task, result)
    
    // Update progress
    await this.updateProgress(task)
    
    return result
  }
  
  private async executeWithTDD(task: Task, agent: Agent): Promise<TaskResult> {
    // RED Phase: Write failing test
    await this.enforceRedPhase(task, agent)
    
    // GREEN Phase: Write minimal implementation
    await this.enforceGreenPhase(task, agent)
    
    // Enforce Simplicity First principle
    await this.enforceSimplicityFirst(task)
    
    // REFACTOR Phase: Improve code quality
    await this.enforceRefactorPhase(task, agent)
    
    // Verify tests still pass after refactoring
    const testResult = await runTest(task.testFile)
    if (testResult.status !== 'passed') {
      throw new Error('TDD violation: Refactoring broke tests - tests must still pass after refactoring')
    }
    
    // Validate clean code standards
    await this.validateCleanCode(task)
    
    return task.result
  }
  
  private async enforceRedPhase(task: Task, agent: Agent): Promise<void> {
    // Check if test file exists
    const testExists = await checkTestFile(task)
    if (!testExists) {
      // Agent must write test first
      await agent.writeTest(task)
    }
    
    // Run test to ensure it fails (red phase)
    const testResult = await runTest(task.testFile)
    if (testResult.status !== 'failed') {
      throw new Error('TDD violation: Test must fail before implementation (RED phase)')
    }
    
    // Store initial test state for green phase validation
    task.initialTestLines = await getFileLineCount(task.testFile)
  }
  
  private async enforceGreenPhase(task: Task, agent: Agent): Promise<void> {
    // Agent writes minimal implementation
    const implementationLinesBefore = await getImplementationLineCount(task)
    
    await agent.implementMinimal(task)
    
    const implementationLinesAfter = await getImplementationLineCount(task)
    const linesAdded = implementationLinesAfter - implementationLinesBefore
    
    // Verify minimal implementation (no over-engineering)
    if (linesAdded > task.expectedImplementationLines * 1.5) {
      throw new Error(`TDD violation: Implementation too large (${linesAdded} lines). Write minimal code to pass test only.`)
    }
    
    // Run test to ensure it passes (green phase)
    const testResult = await runTest(task.testFile)
    if (testResult.status !== 'passed') {
      throw new Error('TDD violation: Test must pass after implementation (GREEN phase)')
    }
    
    // Verify only necessary code was added (no extra features)
    const testLinesAfter = await getFileLineCount(task.testFile)
    if (testLinesAfter > task.initialTestLines * 1.2) {
      throw new Error('TDD violation: Tests were modified in GREEN phase - only implement, do not change tests')
    }
  }
  
  private async enforceRefactorPhase(task: Task, agent: Agent): Promise<void> {
    // Agent refactors code
    const codeBefore = await getImplementationCode(task)
    
    await agent.refactor(task)
    
    const codeAfter = await getImplementationCode(task)
    
    // Verify refactoring happened (code changed)
    if (codeBefore === codeAfter) {
      throw new Error('TDD violation: No refactoring performed - code must be improved after GREEN phase')
    }
    
    // Verify behavior unchanged (tests still pass)
    const testResult = await runTest(task.testFile)
    if (testResult.status !== 'passed') {
      throw new Error('TDD violation: Refactoring changed behavior - tests must still pass')
    }
    
    // Verify complexity decreased or stayed same
    const complexityBefore = await calculateComplexity(codeBefore)
    const complexityAfter = await calculateComplexity(codeAfter)
    if (complexityAfter > complexityBefore) {
      throw new Error('TDD violation: Refactoring increased complexity - refactoring should improve code quality')
    }
    
    // Verify code is cleaner (reduced duplication, better structure)
    await this.validateRefactoringQuality(codeBefore, codeAfter)
  }
  
  private async enforceSimplicityFirst(task: Task): Promise<void> {
    const qualityConfig = loadConfig('config/quality-gates.json')
    const implementationCode = await getImplementationCode(task)
    
    // Check function length (must be ≤50 lines)
    const functions = await extractFunctions(implementationCode)
    for (const func of functions) {
      if (func.length > qualityConfig.codeComplexity.maxFunctionLength) {
        throw new Error(`Simplicity First violation: Function "${func.name}" is ${func.length} lines (max: ${qualityConfig.codeComplexity.maxFunctionLength}). Break it down into smaller functions.`)
      }
    }
    
    // Check file length (must be ≤300 lines)
    const fileLines = await getFileLineCount(task.implementationFile)
    if (fileLines > qualityConfig.codeComplexity.maxFileLength) {
      throw new Error(`Simplicity First violation: File is ${fileLines} lines (max: ${qualityConfig.codeComplexity.maxFileLength}). Split into smaller modules.`)
    }
    
    // Check nesting depth (must be ≤4)
    const maxNesting = await calculateMaxNesting(implementationCode)
    if (maxNesting > qualityConfig.codeComplexity.maxNestingDepth) {
      throw new Error(`Simplicity First violation: Nesting depth is ${maxNesting} (max: ${qualityConfig.codeComplexity.maxNestingDepth}). Flatten the structure using early returns or guard clauses.`)
    }
    
    // Check cyclomatic complexity (must be ≤10)
    const complexity = await calculateComplexity(implementationCode)
    if (complexity > qualityConfig.codeComplexity.cyclomaticComplexity) {
      throw new Error(`Simplicity First violation: Cyclomatic complexity is ${complexity} (max: ${qualityConfig.codeComplexity.cyclomaticComplexity}). Simplify logic by extracting methods or reducing conditionals.`)
    }
    
    // Check for over-engineering (abstractions for single-use)
    const overEngineering = await detectOverEngineering(implementationCode)
    if (overEngineering.detected) {
      throw new Error(`Simplicity First violation: Over-engineering detected - ${overEngineering.reason}. Keep it simple: if you're using it once, don't abstract it.`)
    }
  }
  
  private async validateCleanCode(task: Task): Promise<void> {
    const implementationCode = await getImplementationCode(task)
    
    // Check DRY principle (no duplicated code blocks >3 lines)
    const duplicates = await detectCodeDuplication(implementationCode)
    if (duplicates.length > 0) {
      throw new Error(`Clean code violation: Code duplication detected. Extract repeated code into functions. Duplicates: ${duplicates.map(d => d.name).join(', ')}`)
    }
    
    // Check naming conventions (descriptive names, no abbreviations)
    const namingIssues = await validateNaming(implementationCode)
    if (namingIssues.length > 0) {
      throw new Error(`Clean code violation: Poor naming detected. Use descriptive names: ${namingIssues.join(', ')}`)
    }
    
    // Check single responsibility (functions do one thing)
    const srpViolations = await validateSingleResponsibility(implementationCode)
    if (srpViolations.length > 0) {
      throw new Error(`Clean code violation: Functions with multiple responsibilities detected: ${srpViolations.join(', ')}. Split into separate functions.`)
    }
    
    // Check magic numbers/constants
    const magicNumbers = await detectMagicNumbers(implementationCode)
    if (magicNumbers.length > 0) {
      throw new Error(`No Hardcoding violation: Magic numbers found. Extract to named constants: ${magicNumbers.join(', ')}`)
    }
  }
  
  private async validateRefactoringQuality(codeBefore: string, codeAfter: string): Promise<void> {
    // Check if refactoring reduced duplication
    const dupBefore = await detectCodeDuplication(codeBefore)
    const dupAfter = await detectCodeDuplication(codeAfter)
    
    if (dupAfter.length > dupBefore.length) {
      throw new Error('Refactoring violation: Code duplication increased. Refactoring should reduce duplication, not increase it.')
    }
    
    // Check if function length decreased
    const funcsBefore = await extractFunctions(codeBefore)
    const funcsAfter = await extractFunctions(codeAfter)
    
    const avgLenBefore = funcsBefore.reduce((sum, f) => sum + f.length, 0) / funcsBefore.length
    const avgLenAfter = funcsAfter.reduce((sum, f) => sum + f.length, 0) / funcsAfter.length
    
    if (avgLenAfter > avgLenBefore * 1.1) {
      throw new Error('Refactoring violation: Average function length increased. Refactoring should make functions shorter, not longer.')
    }
  }
  
  private determineAgentType(task: Task): string {
    if (task.category === 'ui' || task.category === 'frontend') return 'frontend'
    if (task.category === 'api' || task.category === 'database') return 'backend'
    if (task.category === 'test') return 'qa'
    if (task.category === 'architecture') return 'tech-lead'
    if (task.category === 'infrastructure' || task.category === 'deployment') return 'devops'
    return 'project-manager'
  }
  
  private async enforceTDD(task: Task): Promise<void> {
    // Check if test exists
    const testExists = await checkTestFile(task)

    if (!testExists) {
      throw new Error('TDD violation: Test must be written before implementation')
    }

    // Run test to ensure it fails (red phase)
    const testResult = await runTest(task.testFile)
    if (testResult.status !== 'failed') {
      throw new Error('TDD violation: Test must fail before implementation')
    }

    // Proceed with implementation (green phase)
  }
  
  private async verifyQualityGates(task: Task, result: TaskResult): Promise<void> {
    // Load quality gate configuration
    const qualityConfig = loadConfig('config/quality-gates.json')

    // Run test suite
    const testResults = await runFullTestSuite()
    if (!testResults.allPassed) {
      throw new Error('Quality gate failed: Tests not passing')
    }

    // Check coverage (read thresholds from config)
    const coverage = await getCoverageReport()
    if (coverage.lines < qualityConfig.codeCoverage.lines ||
        coverage.branches < qualityConfig.codeCoverage.branches) {
      throw new Error(`Quality gate failed: Coverage below threshold (${qualityConfig.codeCoverage.lines}% lines, ${qualityConfig.codeCoverage.branches}% branches)`)
    }

    // Check TDD compliance
    const tddCompliant = await checkTDDCompliance()
    if (!tddCompliant) {
      throw new Error('Quality gate failed: TDD violation detected')
    }

    // Check code complexity (Simplicity First principle)
    const complexity = await calculateCodeComplexity(task)
    if (complexity.cyclomatic > qualityConfig.codeComplexity.cyclomaticComplexity) {
      throw new Error(`Quality gate failed: Cyclomatic complexity ${complexity.cyclomatic} exceeds threshold ${qualityConfig.codeComplexity.cyclomaticComplexity}`)
    }
    if (complexity.maxFunctionLength > qualityConfig.codeComplexity.maxFunctionLength) {
      throw new Error(`Quality gate failed: Function length ${complexity.maxFunctionLength} exceeds threshold ${qualityConfig.codeComplexity.maxFunctionLength}`)
    }
    if (complexity.maxFileLength > qualityConfig.codeComplexity.maxFileLength) {
      throw new Error(`Quality gate failed: File length ${complexity.maxFileLength} exceeds threshold ${qualityConfig.codeComplexity.maxFileLength}`)
    }
    if (complexity.maxNestingDepth > qualityConfig.codeComplexity.maxNestingDepth) {
      throw new Error(`Quality gate failed: Nesting depth ${complexity.maxNestingDepth} exceeds threshold ${qualityConfig.codeComplexity.maxNestingDepth}`)
    }

    // Check code duplication (DRY principle)
    const duplication = await calculateCodeDuplication(task)
    if (duplication.percentage > qualityConfig.architecture.maxDuplicateCodePercentage) {
      throw new Error(`Quality gate failed: Code duplication ${duplication.percentage}% exceeds threshold ${qualityConfig.architecture.maxDuplicateCodePercentage}%`)
    }

    // Security scan
    const securityScan = await runSecurityScan()
    if (securityScan.vulnerabilities.length > qualityConfig.security.maxVulnerabilities) {
      throw new Error('Quality gate failed: Security vulnerabilities found')
    }
  }
  
  private async commitWithGitManage(task: Task, result: TaskResult): Promise<void> {
    const commitMessage = generateGitManageCommit(task, result)
    await runGitCommand(['add', '.'])
    await runGitCommand(['commit', '-m', commitMessage])
  }
  
  private async updateProgress(task: Task): Promise<void> {
    task.status = 'completed'
    await updateStateFile('sprint-planner.md', { tasks: getAllTasks() })
  }
}
```

### 4. Main Orchestration Loop

```typescript
async function executeProject(requirements: string): Promise<DeliveryReport> {
  console.log('[INIT] Extracting requirements...')
  const spec = await initializeProject(requirements)
  
  console.log('[PLAN] Creating task breakdown...')
  const tasks = await breakdownTasks(spec)
  console.log(`[PLAN] ${tasks.length} tasks identified`)
  
  const dispatcher = new AgentDispatcher()
  const completedTasks: Task[] = []
  
  console.log('[EXEC] Starting development cycle...')
  
  for (const task of tasks) {
    if (task.status === 'completed') continue
    
    // Check dependencies
    if (!areDependenciesCompleted(task, completedTasks)) {
      console.log(`[WAIT] Task "${task.title}" waiting for dependencies`)
      continue
    }
    
    console.log(`[EXEC] Task ${tasks.indexOf(task) + 1}/${tasks.length}: ${task.title}`)
    
    try {
      const result = await dispatcher.dispatch(task)
      completedTasks.push(task)
      console.log(`[DONE] Task completed: ${task.title}`)
    } catch (error) {
      console.error(`[FAIL] Task failed: ${task.title}`, error)
      throw error
    }
  }
  
  console.log('[VALIDATE] Running final quality validation...')
  const validation = await runFinalValidation()
  if (!validation.passed) {
    throw new Error('Final validation failed')
  }
  
  console.log('[DEPLOY] Building production bundle...')
  await runBuild()
  
  console.log('[DEPLOY] Deploying to production...')
  await deployToProduction()
  
  console.log('[REPORT] Generating delivery report...')
  const report = await generateDeliveryReport(spec, tasks, validation)
  
  await updateStateFile('quality-metrics.md', validation.metrics)
  await updateStateFile('decisions-log.md', validation.decisions)
  
  return report
}
```

### 5. Quality Gate Enforcement

```typescript
interface QualityGate {
  name: string
  check: () => Promise<boolean>
  remediation: string
}

const qualityGates: QualityGate[] = [
  {
    name: 'Test Suite',
    check: async () => {
      const results = await runFullTestSuite()
      return results.allPassed
    },
    remediation: loadConfig('config/quality-gates.json').remediation.testSuite
  },
  {
    name: 'Coverage Thresholds',
    check: async () => {
      const config = loadConfig('config/quality-gates.json')
      const coverage = await getCoverageReport()
      return coverage.lines >= config.thresholds.coverage.lines &&
             coverage.branches >= config.thresholds.coverage.branches
    },
    remediation: loadConfig('config/quality-gates.json').remediation.coverageThresholds
  },
  {
    name: 'TDD Compliance',
    check: async () => {
      const compliant = await checkTDDCompliance()
      return compliant
    },
    remediation: loadConfig('config/quality-gates.json').remediation.tddCompliance
  },
  {
    name: 'Architecture',
    check: async () => {
      const config = loadConfig('config/quality-gates.json')
      const violations = await checkArchitectureViolations()
      return violations.critical <= config.thresholds.architecture.maxCriticalViolations
    },
    remediation: loadConfig('config/quality-gates.json').remediation.architecture
  },
  {
    name: 'Security',
    check: async () => {
      const config = loadConfig('config/quality-gates.json')
      const scan = await runSecurityScan()
      return scan.vulnerabilities.length <= config.thresholds.security.maxVulnerabilities
    },
    remediation: loadConfig('config/quality-gates.json').remediation.security
  },
  {
    name: 'Accessibility',
    check: async () => {
      const config = loadConfig('config/quality-gates.json')
      const a11y = await runAccessibilityCheck()
      return a11y.compliant
    },
    remediation: loadConfig('config/quality-gates.json').remediation.accessibility
  }
]

async function enforceQualityGates(): Promise<void> {
  for (const gate of qualityGates) {
    const passed = await gate.check()
    if (!passed) {
      throw new Error(`Quality gate "${gate.name}" failed: ${gate.remediation}`)
    }
  }
}
```

### 6. Progress Tracking

```typescript
class ProgressTracker {
  private metrics: QualityMetrics = {
    testCount: 0,
    coverage: { lines: 0, branches: 0, functions: 0 },
    defects: [],
    velocity: 0,
    buildTime: 0
  }
  
  async update(): Promise<void> {
    // Update test count
    const testResults = await runFullTestSuite()
    this.metrics.testCount = testResults.total
    
    // Update coverage
    const coverage = await getCoverageReport()
    this.metrics.coverage = coverage
    
    // Update build time
    this.metrics.buildTime = await measureBuildTime()
    
    // Persist metrics
    await updateStateFile('quality-metrics.md', this.metrics)
  }
  
  async report(): Promise<string> {
    return `
📊 Progress Report:
================
Tests: ${this.metrics.testCount} passing
Coverage: ${this.metrics.coverage.lines}% lines, ${this.metrics.coverage.branches}% branches
Defects: ${this.metrics.defects.length}
Velocity: ${this.metrics.velocity} tasks/hour
Build Time: ${this.metrics.buildTime}s
    `
  }
}
```

### 7. Completion Detection

```typescript
async function isProjectComplete(tasks: Task[]): Promise<boolean> {
  // Check all tasks completed
  const allTasksComplete = tasks.every(t => t.status === 'completed')
  if (!allTasksComplete) return false
  
  // Check all quality gates passed
  const qualityGatesPassed = await checkAllQualityGates()
  if (!qualityGatesPassed) return false
  
  // Check build successful
  const buildSuccessful = await checkBuildSuccess()
  if (!buildSuccessful) return false
  
  // Check deployment successful
  const deploymentSuccessful = await checkDeploymentSuccess()
  if (!deploymentSuccessful) return false
  
  return true
}
```

### 8. Delivery Report Generation

```typescript
async function generateDeliveryReport(
  spec: ProjectSpec,
  tasks: Task[],
  validation: ValidationResult
): Promise<DeliveryReport> {
  return {
    projectName: spec.requirements,
    completionDate: new Date().toISOString(),
    summary: {
      totalTasks: tasks.length,
      completedTasks: tasks.filter(t => t.status === 'completed').length,
      testsPassing: validation.metrics.testCount,
      coverage: validation.metrics.coverage,
      buildTime: validation.metrics.buildTime,
      totalDuration: calculateTotalDuration(tasks)
    },
    quality: {
      allGatesPassed: validation.passed,
      tddCompliant: validation.tddCompliant,
      securityScan: validation.securityScan,
      accessibility: validation.accessibility
    },
    deliverables: spec.deliverables,
    deployment: {
      url: getDeploymentUrl(),
      environment: 'production',
      healthCheck: 'passed'
    },
    recommendations: generateRecommendations(validation)
  }
}
```

## Integration Points

### TDD Enforcement Integration

```typescript
// Automatically enforce TDD for all development tasks
tdd-enforce.on('beforeImplementation', async (task: Task) => {
  if (!await hasTestFile(task)) {
    throw new Error('TDD violation: Test file must exist')
  }
  
  const testResult = await runTest(task.testFile)
  if (testResult.status !== 'failed') {
    throw new Error('TDD violation: Test must fail before implementation')
  }
})
```

### Git-Management Integration

```typescript
// Automatically use git-manage format for all commits
git-manage.on('beforeCommit', async (task: Task) => {
  const message = generateGitManageCommit(task)
  await enforceCommitFormat(message)
})
```

### QA Integration

```typescript
// Automatically run QA validation after each task
qa-engineer.on('afterTask', async (task: Task) => {
  const validation = await validateTask(task)
  if (!validation.passed) {
    throw new Error('QA validation failed')
  }
})
```

## Error Handling and Recovery

```typescript
class ErrorRecoveryHandler {
  async handle(error: Error, task: Task): Promise<void> {
    if (error.message.includes('TDD violation')) {
      await this.handleTDDViolation(task)
    } else if (error.message.includes('Quality gate')) {
      await this.handleQualityGateFailure(task)
    } else if (error.message.includes('Build failed')) {
      await this.handleBuildFailure(task)
    } else {
      await this.handleGenericError(error, task)
    }
  }
  
  private async handleTDDViolation(task: Task): Promise<void> {
    console.log(`[RECOVERY] Creating test file for: ${task.title}`)
    await generateTestFile(task)
    console.log('[RECOVERY] Please implement test and retry')
  }
  
  private async handleQualityGateFailure(task: Task): Promise<void> {
    console.log(`[RECOVERY] Quality gate failed for: ${task.title}`)
    const remediation = getRemediation(task)
    console.log(`[RECOVERY] Remediation: ${remediation}`)
  }
  
  private async handleBuildFailure(task: Task): Promise<void> {
    console.log(`[RECOVERY] Build failed for: ${task.title}`)
    const errors = await getBuildErrors()
    console.log(`[RECOVERY] Errors: ${errors.join(', ')}`)
  }
  
  private async handleGenericError(error: Error, task: Task): Promise<void> {
    console.log(`[RECOVERY] Error in task: ${task.title}`)
    console.log(`[RECOVERY] Error: ${error.message}`)
  }
}
```

## Parallel Task Execution

```typescript
async function executeParallelTasks(tasks: Task[]): Promise<void> {
  const independentTasks = findIndependentTasks(tasks)
  
  const executionGroups = groupByDependencies(independentTasks)
  
  for (const group of executionGroups) {
    console.log(`[PARALLEL] Executing ${group.length} tasks in parallel`)
    
    const results = await Promise.allSettled(
      group.map(task => executeTask(task))
    )
    
    const failures = results.filter(r => r.status === 'rejected')
    if (failures.length > 0) {
      throw new Error(`${failures.length} parallel tasks failed`)
    }
  }
}
```

## Usage Example

```typescript
// Main entry point
async function main() {
  const requirements = "Build a weather dashboard with 7-day forecast"
  
  try {
    const report = await executeProject(requirements)
    console.log('[SUCCESS] Project delivered successfully!')
    console.log(report.summary)
  } catch (error) {
    console.error('[FAILURE] Project delivery failed:', error)
    process.exit(1)
  }
}

main()
```