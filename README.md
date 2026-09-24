# Student Feedback System 🎓

A simple open-ended Unit V project demonstrating:

- Docker
- Docker Compose
- Multi-container applications
- Container networking
- Volumes and data persistence
- Kubernetes Deployments
- Kubernetes Services
- Minikube

## Project Structure

- `frontend/` — HTML/CSS/JavaScript + Nginx
- `backend/` — Python Flask API + SQLite
- `docker-compose.yml` — runs frontend and backend together
- `kubernetes/` — Kubernetes YAML files

## Docker Compose

From the project folder:

```bash
docker compose up --build
```

Open:

```text
http://localhost:8080
```

Stop:

```bash
docker compose down
```

## Kubernetes / Minikube

Build images first:

```bash
docker build -t student-feedback-backend:latest ./backend
docker build -t student-feedback-frontend:latest ./frontend
```

Then load them into Minikube:

```bash
minikube image load student-feedback-backend:latest
minikube image load student-feedback-frontend:latest
```

Start Minikube:

```bash
minikube start
```

Apply the YAML:

```bash
kubectl apply -f kubernetes/backend-deployment.yaml
kubectl apply -f kubernetes/frontend-deployment.yaml
```

Check:

```bash
kubectl get pods
kubectl get services
kubectl get deployments
```

Open the application:

```bash
minikube service feedback-frontend
```
