# Task Manager DevOps Project

This project implements a Django-based CRUD task manager that is containerized with Docker, deployed to Kubernetes, and validated with a load test.

## Repository structure
- `taskproject/` — Django project configuration
- `tasks/` — app logic, URLs, model, and health endpoint
- `Dockerfile` — multi-stage production container build
- `docker-compose.yml` — local container orchestration with Postgres + Django
- `k8s/` — Kubernetes manifests for deployment, autoscaling, ingress, and Postgres
- `k6-api-test.js` / `loadtest.js` — load-testing scripts

## Assumptions
- Python version: 3.12
- Django version: 4.2.x
- PostgreSQL is used as the application database
- Container ports: Django app on `3000`, PostgreSQL on `5432`
- The app is expected to expose `/health/` for health checks and readiness/liveness probes

## Run locally with Docker Compose
```bash
docker compose up --build
```

Verify:
```bash
curl -i http://127.0.0.1:3000/health/
curl -s http://127.0.0.1:3000/tasks
```

## Database migration
```bash
DATABASE_URL=postgres://postgres:password@localhost:5432/tasksdb python3 manage.py migrate
```

## Kubernetes notes
- The application deployment uses a `Deployment` with `readinessProbe` and `livenessProbe` pointed at `/health/`.
- A `Service` exposes the app internally and can be reached through the cluster network.
- The app can be validated on Minikube with `kubectl get pods`, `kubectl get svc`, and curl against the service URL.

## Load testing
```bash
k6 run k6-api-test.js
```

This project is intended to satisfy the DevOps examination assignment and keeps the original CRUD behavior while adding the required container and Kubernetes deployment configuration.
