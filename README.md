# AWS EKS GitOps DevOps Platform — Application Phase

This repository contains the application delivery layer for the AWS EKS GitOps DevOps Platform.

## Planned scope

- Microservices source code
- Dockerfiles
- GitHub Actions CI workflows
- Kubernetes manifests
- Argo CD application definitions

## CI/CD model

- **CI:** GitHub Actions
- **Registry:** Amazon ECR
- **CD:** Argo CD
- **Platform:** Amazon EKS
- **Secrets:** HashiCorp Vault

## Initial structure

```text
services/
k8s/
argocd/
.github/workflows/
```

# 🚀 Phase 1 — CI Setup & Containerization (Completed)

In this phase, we implemented the **Continuous Integration (CI)** pipeline for our GitOps-based DevOps platform.

The goal of this phase was to:
- Containerize the application
- Build Docker images automatically
- Push images to AWS ECR
- Establish a production-style CI workflow

---

## ✅ What Was Implemented

### 1. Frontend Application (Initial Service)
- Created a simple Flask application
- Defined dependencies
- Prepared it for containerization

### 2. Dockerization
- Created a `Dockerfile` for the frontend service
- Ensured the application can run inside a container

### 3. Amazon ECR Setup
- Created ECR repository:
**frontend**
  - Used as the container registry for the application

### 4. GitHub Actions CI Pipeline
- Created workflow: `.github/workflows/ci.yml`
- Pipeline automatically:
- Builds Docker image
- Authenticates to AWS
- Pushes image to ECR

### 5. Secure Authentication
- Configured GitHub Secrets:
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`

---

## 📁 Repository Structure (After Push)

```text
eks-gitops-platform/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── services/
│   └── frontend/
│       ├── app.py
│       ├── requirements.txt
│       └── Dockerfile
│
├── k8s/
│   └── base/
│
├── argocd/
│
└── README.md
```

## CI Pipeline Flow
- On every push to main:
- Code is checked out
- AWS credentials are loaded from secrets
- Docker image is built
- Image is tagged for ECR
- Image is pushed to ECR

<img width="1470" height="885" alt="Screenshot 2026-03-19 at 22 15 43" src="https://github.com/user-attachments/assets/1c23cc03-3bd2-42ad-89be-28c7134e3c73" />

<img width="2940" height="1912" alt="image" src="https://github.com/user-attachments/assets/a4c4b26b-a52a-4f74-aebc-4ab15a5cf9a7" />

# 🚀 Phase 2 — Kubernetes Deployment (Completed)

In this phase, we deployed the frontend container image from Amazon ECR to the Amazon EKS cluster.

## ✅ What was implemented

- Created Kubernetes `Deployment` for the frontend application
- Configured `replicas: 2` for basic redundancy
- Created Kubernetes `Service` of type `LoadBalancer`
- Exposed the application publicly through an AWS load balancer
- Verified pods are running successfully
- Verified the service received an external endpoint

## Kubernetes Manifests Added

### `k8s/base/deployment.yaml`
Defines the frontend deployment:
- image source: Amazon ECR
- 2 replicas
- container port: 5000

### `k8s/base/service.yaml`
Defines the frontend service:
- type: `LoadBalancer`
- public access on port 80
- forwards traffic to container port 5000

## Commands Executed

```bash
kubectl apply -f k8s/base/
kubectl get pods
kubectl get svc
```
<img width="2940" height="1912" alt="image" src="https://github.com/user-attachments/assets/935d1a3e-751e-41be-8314-a573d3c73c8e" />

**Public Access**

The application is exposed through the AWS load balancer DNS name created by Kubernetes

<img width="2940" height="1912" alt="image" src="https://github.com/user-attachments/assets/415d6bbe-c69f-48a9-91f7-9869480f4ada" />
<img width="2940" height="1912" alt="image" src="https://github.com/user-attachments/assets/20a88c66-b75b-4232-8637-a7f852c63b48" />
<img width="2940" height="1912" alt="image" src="https://github.com/user-attachments/assets/b86ae22f-eb0f-4a65-aef0-159637fe0352" />

**Key Outcome**
- We now have a working application running on EKS with:
- automated image build and push
- live deployment on Kubernetes
- public endpoint through AWS LoadBalancer

## 🚀 Phase 3 — GitOps Deployment with ArgoCD (Completed)

In this phase, we transitioned from manual Kubernetes deployments to a **GitOps-based continuous deployment model using ArgoCD**.

---

### 🎯 Objective

- Eliminate manual `kubectl apply`
- Use GitHub as the single source of truth
- Enable automatic synchronization between Git and Kubernetes

---

### ✅ What Was Implemented

#### 1. ArgoCD Installation
- Installed ArgoCD in the EKS cluster
- Created dedicated namespace: `argocd`
- Verified all ArgoCD components are running
<img width="2940" height="1912" alt="image" src="https://github.com/user-attachments/assets/47236d18-3f8a-4079-b010-b50384af375f" />

#### 2. ArgoCD UI Exposure
- Exposed ArgoCD server using `LoadBalancer`
- Accessed UI via public AWS ELB

#### 3. Secure Login
- Retrieved admin password from Kubernetes secret
- Logged into ArgoCD dashboard
<img width="2940" height="1912" alt="image" src="https://github.com/user-attachments/assets/f08680a7-b728-49fd-a85a-9e5e3f3b2d72" />
 
#### 4. GitOps Application Setup
- Connected ArgoCD to GitHub repository
- Configured application to watch:
**k8s/base**
  - Enabled automated sync:
- Auto-deploy
- Self-heal
- Prune old resources

#### 5. Application Deployment via GitOps
- ArgoCD pulled manifests from GitHub
- Deployed frontend application automatically
- Verified application is:
- Healthy ✅
- Synced ✅

---

### ⚙️ ArgoCD Application Configuration

- **Repository:** GitHub (eks-gitops-platform)
- **Branch:** main
- **Path:** k8s/base
- **Cluster:** in-cluster
- **Namespace:** default

---

<img width="1470" height="886" alt="Screenshot 2026-03-20 at 08 22 28" src="https://github.com/user-attachments/assets/2133aa80-0365-42d5-84c3-380ded25354b" />



### 🔄 GitOps Workflow

```text
Developer → Git Push → GitHub → ArgoCD → Kubernetes (EKS)
```
----

## 🚀 Phase 4 — Automated Image Updates (Full GitOps CI/CD)

In this phase, we moved from semi-automated deployments to a fully automated GitOps pipeline where application changes trigger builds and deployments without manual intervention.

---

### 🎯 Objective

- Remove manual image tag updates in Kubernetes manifests  
- Use commit SHA as the image version  
- Achieve full CI/CD + GitOps automation  

---

### ⚙️ What Was Implemented

#### 1. Commit-Based Image Tagging

- Docker images are now tagged using:**${GITHUB_SHA}**

- Each deployment is uniquely tied to a Git commit

---

#### 2. CI Pipeline Enhancement

Updated GitHub Actions to:

- Build Docker image  
- Tag image with commit SHA  
- Push image to Amazon ECR  

---

#### 3. Automatic Manifest Update

-CI dynamically updates:**k8s/base/deployment.yaml**
- Replacing `REPLACE_TAG` with `${GITHUB_SHA}`

---

#### 4. GitOps Automation

- CI commits updated manifest back to GitHub  
- ArgoCD detects the change  
- Automatically syncs and deploys to EKS  

---

### 🔄 Full Workflow
Developer → Git Push → GitHub Actions (CI)
- → Build Docker Image
- → Push to ECR
- → Update deployment.yaml
- → Push to GitHub
- → ArgoCD detects change
- → Deploy to EKS

---

### ✅ Verification

- GitHub Actions pipeline succeeds  
- New image appears in ECR with commit SHA tag  
- ArgoCD shows Synced and Healthy  
- Pods update automatically in Kubernetes  

---


<img width="2940" height="1912" alt="image" src="https://github.com/user-attachments/assets/ebd1bdac-491e-4fca-80dd-3b9fe4bfaa27" />
<img width="2940" height="1912" alt="image" src="https://github.com/user-attachments/assets/dfb52c39-2a45-4f12-acbd-0d15739ce5b4" />

### 🚀 Outcome

- Fully automated CI pipeline  
- Automatic image versioning  
- Git-driven deployments via ArgoCD  
- No manual kubectl usage required  

---

### 🧠 Key Learning

- ArgoCD watches Git, not container registries  
- Image updates must be reflected in Git manifests  
- Git becomes the single source of truth  




