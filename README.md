# Azure DevSecOps Demo Application

A deliberately small Flask application used to demonstrate a production-oriented
DevSecOps CI/CD platform.

## Application Endpoints

| Endpoint | Purpose |
|---|---|
| `/` | Application information |
| `/health` | Health check |
| `/ready` | Readiness check |

## Technology

- Python
- Flask
- Gunicorn
- Docker

## DevSecOps Pipeline

The application will be used to demonstrate:

- Secret scanning
- SAST
- Software Composition Analysis
- Infrastructure-as-Code security scanning
- Container vulnerability scanning
- Security quality gates
- Azure OIDC authentication
- Azure Container Registry
- GitOps deployment
- Kubernetes

## Container

The application listens on port `8080`.

The production container runs as a non-root user.
