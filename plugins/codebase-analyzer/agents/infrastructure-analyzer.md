# Infrastructure Analyzer

Analyze infrastructure and generate an infrastructure skill.

## Instructions

Explore the codebase to understand:
- Containerization (Docker)
- CI/CD pipelines
- Deployment configuration
- Environment management
- Cloud services used
- Monitoring/logging setup

Look for:
- Dockerfile, docker-compose
- CI config (.github/workflows, .gitlab-ci, etc.)
- Deployment scripts
- Environment files
- Infrastructure as code (Terraform, Pulumi, etc.)

Create the folder `.claude/skills/infrastructure/` and generate `SKILL.md` inside it:

```markdown
---
name: infrastructure
description: Explains this project's infrastructure, deployment, and DevOps setup
---

# Infrastructure Guide

## Containerization
[Docker setup and usage]

## CI/CD
[Pipeline configuration and stages]

## Deployment
[How to deploy]

## Environments
[Environment configuration]

## Monitoring
[Logging and monitoring setup]
```

Return a summary of the infrastructure findings.
