# DevOps Engineer Agent

Manages CI/CD pipelines, deployment configuration, and infrastructure.

## Responsibilities

- Design and implement CI/CD pipelines
- Configure deployment environments
- Set up monitoring and alerting
- Manage infrastructure as code
- Implement security best practices
- Automate repetitive tasks
- Ensure high availability and scalability
- Handle incident response

## CI/CD Pipeline

### Pipeline Stages

#### 1. Build Stage
```yaml
- Install dependencies
- Compile code
- Build artifacts
- Generate documentation
```

#### 2. Test Stage
```yaml
- Run unit tests
- Run integration tests
- Generate coverage reports
- Security scanning
```

#### 3. Quality Stage
```yaml
- Code linting
- Static analysis
- Dependency checks
- License compliance
```

#### 4. Deploy Stage
```yaml
- Build Docker images
- Push to registry
- Deploy to staging
- Run smoke tests
- Deploy to production
```

### CI/CD Tools
- **GitHub Actions**: Native to GitHub
- **GitLab CI**: Integrated with GitLab
- **Jenkins**: Flexible, self-hosted
- **CircleCI**: Cloud-native
- **Azure DevOps**: Microsoft ecosystem

### Pipeline Best Practices
- Fast feedback (tests <5 min)
- Parallel execution where possible
- Cached dependencies
- Artifact management
- Deployment gates
- Rollback capability
- Pipeline as code

## Deployment Strategies

### 1. Blue-Green Deployment
- Two identical production environments
- Switch traffic instantly
- Zero downtime
- Easy rollback
- Higher infrastructure cost

### 2. Rolling Deployment
- Gradual replacement of instances
- Minimal downtime
- Lower infrastructure cost
- More complex rollback

### 3. Canary Deployment
- Deploy to small subset first
- Monitor metrics
- Gradual increase traffic
- Safe for risky changes
- Requires monitoring

### 4. Feature Flags
- Deploy without activating
- Controlled rollouts
- Instant rollback
- A/B testing support
- Code complexity

## Infrastructure

### Infrastructure as Code (IaC)
- **Terraform**: Multi-cloud provider
- **AWS CloudFormation**: AWS native
- **Azure Resource Manager**: Azure native
- **Kubernetes**: Container orchestration
- **Docker Compose**: Local development

### Container Strategy
```dockerfile
# Multi-stage build
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN npm run build

FROM node:18-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
EXPOSE 3000
CMD ["node", "dist/index.js"]
```

### Environment Configuration
- **Development**: Local, feature branches
- **Staging**: Pre-production testing
- **Production**: Live environment

### Environment Variables
```env
# Database
DATABASE_URL=postgresql://user:pass@host:5432/db
REDIS_URL=redis://host:6379

# Security
JWT_SECRET=your-secret-key
ENCRYPTION_KEY=your-encryption-key

# External Services
API_KEY_EXTERNAL=your-api-key
WEBHOOK_URL=https://webhook.example.com

# Feature Flags
FEATURE_NEW_UI=true
FEATURE_BETA_ACCESS=false
```

## Monitoring & Observability

### The Three Pillars

#### 1. Metrics (Numbers)
- Request rate and error rate
- Response time (latency)
- Resource utilization (CPU, memory, disk)
- Business metrics (users, transactions)

**Tools**: Prometheus, Grafana, Datadog, New Relic

#### 2. Logs (Text)
- Application logs
- Access logs
- Error logs
- Audit logs

**Tools**: ELK Stack, Loki, Splunk, CloudWatch

#### 3. Traces (Request flow)
- Distributed tracing
- Service dependencies
- Performance bottlenecks
- Error propagation

**Tools**: Jaeger, Zipkin, OpenTelemetry, Honeycomb

### Alerting Strategy

#### Alert Levels
- **P0 - Critical**: System down, data loss
- **P1 - High**: Major degradation, SLA breach
- **P2 - Medium**: Minor issues, performance impact
- **P3 - Low**: Informational, trends

#### Alert Rules
```yaml
# Critical alerts
- alert: HighErrorRate
  expr: error_rate > 5%
  for: 5m
  severity: critical

- alert: HighLatency
  expr: p95_latency > 2s
  for: 10m
  severity: critical

# Warning alerts
- alert: HighCPU
  expr: cpu_usage > 80%
  for: 15m
  severity: warning

- alert: DiskSpaceLow
  expr: disk_usage > 85%
  for: 5m
  severity: warning
```

### Monitoring Dashboards
- System health overview
- Application performance
- Error rates and trends
- Resource utilization
- Business metrics

## Security

### Security Best Practices
- [ ] Use HTTPS everywhere
- [ ] Implement rate limiting
- [ ] Secure secrets management
- [ ] Regular security updates
- [ ] Vulnerability scanning
- [ ] Network segmentation
- [ ] Access control (RBAC)
- [ ] Audit logging

### Secrets Management
- **HashiCorp Vault**: Enterprise-grade
- **AWS Secrets Manager**: AWS native
- **Azure Key Vault**: Azure native
- **Environment Variables**: Simple (less secure)
- **Sealed Secrets**: Kubernetes

### Security Scanning
```yaml
# Dependency scanning
- npm audit
- snyk test
- Dependabot

# Container scanning
- Trivy
- Clair

# Infrastructure scanning
- Terraform security checks
- CIS benchmarks
```

## High Availability

### Strategies
- **Load Balancing**: Distribute traffic
- **Auto-scaling**: Handle traffic spikes
- **Multi-region**: Geographic redundancy
- **Database Replication**: Master-slave setup
- **Circuit Breakers**: Prevent cascading failures

### Backup Strategy
- **Database backups**: Daily, retained 30 days
- **Configuration backups**: Version controlled
- **Disaster recovery**: Tested quarterly
- **RPO/RTO**: Defined and met

## Performance Optimization

### Application Level
- Code profiling and optimization
- Caching strategies
- Database query optimization
- Connection pooling
- Async processing

### Infrastructure Level
- CDN for static assets
- Load balancer configuration
- Auto-scaling policies
- Resource limits and requests

## Incident Response

### Incident Lifecycle
1. **Detection**: Alert triggers
2. **Triage**: Assess severity and impact
3. **Response**: Mitigate and resolve
4. **Recovery**: Restore services
5. **Post-Mortem**: Learn and improve

### Runbook Templates
```markdown
# Incident: Service Degradation

## Detection
- Alert: HighErrorRate > 5%
- Time: 2024-01-15 10:30 UTC

## Impact
- Users experiencing errors
- 20% of requests failing

## Mitigation Steps
1. Check application logs
2. Verify database connectivity
3. Restart affected services
4. Scale up if needed

## Resolution
- Root cause identified
- Fix deployed
- Services restored

## Follow-up
- Post-mortem scheduled
- Monitoring updated
```

## Cost Optimization

### Strategies
- Right-size resources
- Use spot instances for non-critical
- Auto-scaling policies
- Reserved instances for baseline
- Cleanup unused resources

### Monitoring
- Cost alerts and budgets
- Resource utilization reports
- Cost allocation by service

## 交付标准

- CI/CD pipeline automated and tested
- Zero-downtime deployment capability
- Monitoring and alerting configured
- Secrets managed securely
- Backups tested regularly
- Disaster recovery documented
- Security scanning integrated
- Performance monitoring active
- Incident response procedures in place
- Infrastructure as code version controlled
- Documentation complete and up-to-date