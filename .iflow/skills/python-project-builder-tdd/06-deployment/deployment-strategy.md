# Deployment Strategy Guide

## Purpose
This guide explains different deployment strategies for Python projects and how to implement them.

## Deployment Strategies

### 1. Direct Deployment
Deploy directly to production environment.

**Pros**:
- Simple and fast
- No infrastructure complexity

**Cons**:
- Downtime during deployment
- Risk of breaking production
- No rollback mechanism

**When to Use**:
- Small projects
- Low traffic applications
- Internal tools

---

### 2. Blue-Green Deployment
Maintain two identical production environments (blue and green).

**Pros**:
- Zero downtime
- Instant rollback
- Easy testing

**Cons**:
- Double infrastructure cost
- Complex configuration
- Database migration challenges

**When to Use**:
- High availability required
- Frequent deployments
- Mission-critical applications

---

### 3. Canary Deployment
Gradually roll out new version to subset of users.

**Pros**:
- Risk mitigation
- Gradual exposure
- Easy rollback

**Cons**:
- Complex implementation
- Longer deployment time
- Monitoring required

**When to Use**:
- Large user base
- High-risk deployments
- A/B testing

---

### 4. Rolling Deployment
Replace instances one at a time.

**Pros**:
- Partial availability maintained
- Cost-effective
- Simple to implement

**Cons**:
- Slower deployment
- Multiple versions running
- Potential for inconsistencies

**When to Use**:
- Auto-scaling environments
- Containerized applications
- Multi-instance deployments

---

## Deployment Environments

### Development Environment
- **Purpose**: Local development and testing
- **Configuration**: Local settings, mock data
- **Access**: Developer only
- **Deployment**: Manual, on-demand

### Staging Environment
- **Purpose**: Pre-production testing
- **Configuration**: Production-like settings
- **Access**: Development team, QA
- **Deployment**: Automated on merge to develop

### Production Environment
- **Purpose**: Live application
- **Configuration**: Production settings
- **Access**: End users
- **Deployment**: Automated on merge to main

## Deployment Checklist

### Pre-Deployment
- [ ] All tests passing
- [ ] Code reviewed and approved
- [ ] Documentation updated
- [ ] Version number updated
- [ ] Changelog updated
- [ ] Configuration reviewed
- [ ] Backup created
- [ ] Rollback plan defined

### Deployment
- [ ] Dependencies installed
- [ ] Database migrations run
- [ ] Static files collected
- [ ] Cache cleared
- [ ] Services restarted
- [ ] Health checks pass

### Post-Deployment
- [ ] Application verified
- [ ] Monitoring checked
- [ ] Error logs reviewed
- [ ] Performance validated
- [ ] User feedback collected
- [ ] Documentation updated

## Deployment Configuration

### Environment Variables

```bash
# .env.example
# Application
APP_NAME=my-project
APP_ENV=production
APP_VERSION=0.1.0
DEBUG=false

# Server
HOST=0.0.0.0
PORT=8000
WORKERS=4

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
DATABASE_POOL_SIZE=20

# Redis (if applicable)
REDIS_URL=redis://localhost:6379/0

# Security
SECRET_KEY=your-secret-key
ALLOWED_ORIGINS=https://example.com

# Logging
LOG_LEVEL=INFO
LOG_FORMAT=json

# External Services
API_KEY=your-api-key
WEBHOOK_URL=https://example.com/webhook
```

### Configuration Management

```python
# src/config.py
import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Application settings."""
    
    # Application
    app_name: str = os.getenv("APP_NAME", "my-project")
    app_env: str = os.getenv("APP_ENV", "development")
    app_version: str = os.getenv("APP_VERSION", "0.1.0")
    debug: bool = os.getenv("DEBUG", "false").lower() == "true"
    
    # Server
    host: str = os.getenv("HOST", "0.0.0.0")
    port: int = int(os.getenv("PORT", "8000"))
    workers: int = int(os.getenv("WORKERS", "4"))
    
    # Database
    database_url: str = os.getenv("DATABASE_URL")
    database_pool_size: int = int(os.getenv("DATABASE_POOL_SIZE", "20"))
    
    # Security
    secret_key: str = os.getenv("SECRET_KEY")
    allowed_origins: str = os.getenv("ALLOWED_ORIGINS", "*")
    
    # Logging
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    log_format: str = os.getenv("LOG_FORMAT", "json")
    
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
```

## Deployment Methods

### Method 1: Docker Deployment

#### Dockerfile
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen --no-dev

# Copy application code
COPY src/ ./src/

# Expose port
EXPOSE 8000

# Run application
CMD ["uv", "run", "uvicorn", "my_project.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

#### docker-compose.yml
```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/myproject
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      - db
      - redis
    restart: unless-stopped

  db:
    image: postgres:15
    environment:
      - POSTGRES_DB=myproject
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: unless-stopped

  redis:
    image: redis:7
    restart: unless-stopped

volumes:
  postgres_data:
```

#### Deploy with Docker
```bash
# Build image
docker build -t my-project:0.1.0 .

# Run container
docker run -d -p 8000:8000 --env-file .env my-project:0.1.0

# Run with docker-compose
docker-compose up -d

# View logs
docker-compose logs -f

# Stop
docker-compose down
```

---

### Method 2: Cloud Platform Deployment

#### Deploy to AWS (Elastic Beanstalk)

```bash
# Install AWS CLI
pip install awsebcli

# Initialize
eb init -p python-3.11 my-project

# Create environment
eb create production

# Deploy
eb deploy

# View logs
eb logs

# Open application
eb open
```

#### Deploy to Google Cloud (App Engine)

```yaml
# app.yaml
runtime: python311
entrypoint: uvicorn my_project.main:app --host 0.0.0.0 --port $PORT
env_variables:
  DATABASE_URL: ${DATABASE_URL}
  SECRET_KEY: ${SECRET_KEY}

handlers:
- url: /.*
  script: auto
  secure: always
```

```bash
# Deploy
gcloud app deploy

# View logs
gcloud app logs tail
```

#### Deploy to Azure (App Service)

```bash
# Create resource group
az group create --name my-project --location eastus

# Create app service plan
az appservice plan create --name my-project-plan --resource-group my-project --sku B1

# Create web app
az webapp create --name my-project-app --resource-group my-project --plan my-project-plan

# Deploy
az webapp up --name my-project-app --resource-group my-project
```

---

### Method 3: Kubernetes Deployment

#### deployment.yaml
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-project
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-project
  template:
    metadata:
      labels:
        app: my-project
    spec:
      containers:
      - name: my-project
        image: my-project:0.1.0
        ports:
        - containerPort: 8000
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: my-project-secrets
              key: database-url
        - name: SECRET_KEY
          valueFrom:
            secretKeyRef:
              name: my-project-secrets
              key: secret-key
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 5
          periodSeconds: 5
---
apiVersion: v1
kind: Service
metadata:
  name: my-project
spec:
  selector:
    app: my-project
  ports:
  - port: 80
    targetPort: 8000
  type: LoadBalancer
```

#### Deploy to Kubernetes
```bash
# Build and push image
docker build -t my-project:0.1.0 .
docker tag my-project:0.1.0 registry.example.com/my-project:0.1.0
docker push registry.example.com/my-project:0.1.0

# Deploy
kubectl apply -f deployment.yaml

# Check status
kubectl get pods
kubectl logs -f deployment/my-project

# Scale
kubectl scale deployment my-project --replicas=5
```

---

## Database Migrations

### Using Alembic

```bash
# Install alembic
uv add alembic

# Initialize alembic
uv run alembic init alembic

# Create migration
uv run alembic revision --autogenerate -m "Initial migration"

# Run migration
uv run alembic upgrade head

# Rollback
uv run alembic downgrade -1

# View migration history
uv run alembic history
```

### Migration in Deployment

```bash
#!/bin/bash
# deploy.sh

# Backup database
pg_dump $DATABASE_URL > backup_$(date +%Y%m%d_%H%M%S).sql

# Run migrations
uv run alembic upgrade head

# Restart application
systemctl restart my-project

# Verify health
curl http://localhost:8000/health
```

## Health Checks

### Health Endpoint

```python
# src/health.py
from fastapi import APIRouter
from src.config import settings
from sqlalchemy import text

router = APIRouter()

@router.get("/health")
async def health_check():
    """Health check endpoint."""
    checks = {
        "status": "healthy",
        "version": settings.app_version,
        "environment": settings.app_env,
    }
    
    # Check database
    try:
        from src.database import engine
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        checks["database"] = "healthy"
    except Exception as e:
        checks["status"] = "unhealthy"
        checks["database"] = f"unhealthy: {str(e)}"
    
    # Check cache (if applicable)
    try:
        from src.cache import cache
        await cache.ping()
        checks["cache"] = "healthy"
    except Exception as e:
        checks["status"] = "unhealthy"
        checks["cache"] = f"unhealthy: {str(e)}"
    
    status_code = 200 if checks["status"] == "healthy" else 503
    return checks, status_code
```

## Monitoring and Logging

### Structured Logging

```python
# src/logging.py
import logging
import json
from src.config import settings

class JSONFormatter(logging.Formatter):
    """JSON log formatter."""
    
    def format(self, record):
        log_data = {
            "timestamp": self.formatTime(record),
            "level": record.levelname,
            "message": record.getMessage(),
            "logger": record.name,
        }
        
        if hasattr(record, "user_id"):
            log_data["user_id"] = record.user_id
        
        if hasattr(record, "request_id"):
            log_data["request_id"] = record.request_id
        
        return json.dumps(log_data)

def setup_logging():
    """Setup logging configuration."""
    handler = logging.StreamHandler()
    
    if settings.log_format == "json":
        handler.setFormatter(JSONFormatter())
    else:
        handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
    
    root_logger = logging.getLogger()
    root_logger.setLevel(getattr(logging, settings.log_level.upper()))
    root_logger.addHandler(handler)
```

## Rollback Strategy

### Quick Rollback

```bash
#!/bin/bash
# rollback.sh

# Get previous version
PREVIOUS_VERSION=$(ls -t dist/ | head -2 | tail -1)

# Stop current version
systemctl stop my-project

# Install previous version
pip install dist/$PREVIOUS_VERSION

# Start application
systemctl start my-project

# Verify
curl http://localhost:8000/health
```

### Database Rollback

```bash
# Rollback migration
uv run alembic downgrade -1

# Restore backup (if needed)
psql $DATABASE_URL < backup_20260203_100000.sql
```

## Deployment Commands Reference

```bash
# Docker
docker build -t my-project:0.1.0 .
docker run -d -p 8000:8000 my-project:0.1.0

# Kubernetes
kubectl apply -f deployment.yaml
kubectl get pods
kubectl logs -f deployment/my-project

# AWS EB
eb deploy
eb logs
eb open

# Google Cloud
gcloud app deploy
gcloud app logs tail

# Azure
az webapp up --name my-project-app

# Health check
curl http://localhost:8000/health

# Database migration
uv run alembic upgrade head
uv run alembic downgrade -1
```