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

# Phase 5 — Monitoring & Observability

## Overview

To ensure visibility into the health and performance of the Kubernetes cluster and deployed applications, a monitoring stack was implemented using **Prometheus and Grafana**.

The monitoring stack was deployed using the **kube-prometheus-stack Helm chart**, which provides a production-ready monitoring solution for Kubernetes environments.

This stack allows us to collect metrics from the cluster, visualize system performance, and prepare the platform for production-grade observability.

---

## Monitoring Architecture
```bash
Kubernetes Cluster (EKS)
│
│ Metrics
▼
Prometheus
│
│ Query
▼
Grafana
│
│ Dashboards
▼
Cluster Observability
```

Prometheus collects metrics from Kubernetes components and nodes, while Grafana visualizes these metrics through dashboards.

---

## Components Installed

The **kube-prometheus-stack** installs several components:

- **Prometheus** – collects and stores metrics
- **Grafana** – visualization dashboards
- **Alertmanager** – alert routing (planned for future configuration)
- **kube-state-metrics** – Kubernetes object metrics
- **Node Exporter** – node-level metrics

---

## Installing the Monitoring Stack

First, add the Prometheus Helm repository:

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
Install the monitoring stack:
helm install monitoring prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --create-namespace
Verify Installation

Check that the monitoring pods are running:
kubectl get pods -n monitoring
```
<img width="2940" height="1912" alt="image" src="https://github.com/user-attachments/assets/d9ef46ab-7be0-47b5-97c0-c19050c14ae8" />

 ### Accessing Grafana

Expose Grafana using a LoadBalancer service:
```bash
kubectl patch svc monitoring-grafana -n monitoring \
  -p '{"spec": {"type": "LoadBalancer"}}'
Retrieve the external address:
kubectl get svc -n monitoring
```
Access Grafana through the provided LoadBalancer DNS.

<img width="1470" height="956" alt="Screenshot 2026-03-21 at 17 21 29" src="https://github.com/user-attachments/assets/a50e943c-a237-419d-a760-7a158d5ca19c" />
### Grafana provides built-in dashboards to visualize Kubernetes metrics such as:

Cluster CPU usage
Node resource consumption
Pod performance
Memory utilization
Network traffic

These dashboards allow operators to monitor cluster health and troubleshoot issues quickly.

<img width="2940" height="1912" alt="image" src="https://github.com/user-attachments/assets/cf8f9102-7d99-4c83-97d0-846508ba1b1d" />

<img width="2940" height="1912" alt="image" src="https://github.com/user-attachments/assets/24b0474e-56c5-487d-a7eb-cb674a1077a6" />

<img width="2940" height="1912" alt="image" src="https://github.com/user-attachments/assets/f0ed49a6-d1ee-419d-909e-d2c41563c2f9" />

### Observability Benefits

This monitoring stack provides:

Real-time cluster performance visibility
Resource utilization monitoring
Early detection of system anomalies
Foundations for production alerting

#### Cost Consideration

Because the environment was deployed in AWS, the infrastructure was temporarily paused during development due to cost considerations.


## 🌐 Phase 6 — Ingress & External Access (Completed)

In this phase, we exposed the Kubernetes application to the internet using an **Ingress Controller**, but this only worked after the full GitOps delivery flow had completed successfully.

This means the application had to go through:

1. **Code push to GitHub**
2. **GitHub Actions CI pipeline**
   - build Docker image
   - push image to Amazon ECR
3. **ArgoCD GitOps sync**
   - detect manifest changes from GitHub
   - deploy updated resources to EKS
4. **Ingress + Load Balancer access**
   - route public traffic to the frontend service

Only after these steps completed could the application be accessed through the Load Balancer.

---

### 🎯 Objective

- Expose application to the internet
- Route external traffic into the Kubernetes cluster
- Use Ingress as a more production-style entry point
- Prepare for domain and HTTPS in the next phase

---

## ✅ What Was Implemented

### 1. Full delivery flow before public access

Before testing the Load Balancer, the following workflow had to succeed:

```text
Developer → Git Push → GitHub Actions → Amazon ECR → ArgoCD → EKS → Ingress → AWS ELB → Browser
```
**This ensured:**

the latest code was built
the latest image was pushed to ECR
ArgoCD deployed the correct Kubernetes resources
the app was actually running before external routing was tested

### 2 Installed NGINX Ingress Controller

Installed the ingress controller using the official manifest:
```
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/aws/deploy.yaml
Verified installation:

kubectl get pods -n ingress-nginx
kubectl get svc -n ingress-nginx
```
### 3. Created Ingress Resource

Created the ingress manifest in:
```bash
k8s/base/ingress.yaml
```
### 4. Pushed manifest to GitHub

After creating the ingress manifest, it was pushed to the repository:

### 5. GitHub Actions and ArgoCD role in this phase

This phase depended on the existing CI/CD and GitOps setup:

GitHub Actions handled image build and push to ECR
ArgoCD watched the GitHub repository and applied the Kubernetes manifests
The application and ingress resources had to be successfully synced before external access could work

ArgoCD confirmed the application state as:

Healthy
Sync
<img width="2775" height="1624" alt="image" src="https://github.com/user-attachments/assets/e577e20b-141a-4aa5-8167-acbaa9b01bd3" />
<img width="2940" height="1912" alt="image" src="https://github.com/user-attachments/assets/0dc350ca-88db-4b75-a94e-8058725cd2ab" />

### 6. Retrieved external access endpoint

- Checked the ingress controller service:
```bash
kubectl get svc -n ingress-nginx
Used the EXTERNAL-IP / AWS ELB DNS from:
ingress-nginx-controller
```

<img width="2940" height="1912" alt="image" src="https://github.com/user-attachments/assets/964ce5d0-4043-4de9-b222-35521f923f3f" />

### 🚀 Outcome
**By the end of this phase:**
- The application was deployed to EKS
- GitHub Actions was building and pushing images
- ArgoCD was syncing manifests from GitHub
- Ingress was routing traffic correctly
- The app became publicly accessible through AWS Load Balancer

# 🚀 Phase 7 — Production Ingress, HTTPS & Domain Routing

In this phase, the platform was upgraded from an internal Kubernetes service to a **public production-ready application** accessible through a custom domain and HTTPS.

This was achieved by integrating:

- AWS Load Balancer Controller
- AWS Application Load Balancer (ALB)
- AWS Certificate Manager (ACM)
- Route53 DNS
- Kubernetes Ingress

The application is now accessible via:

```
https://futurecars.anzyworld.com
```

---

# 🎯 Objective

Expose the Kubernetes application securely to the internet using:

- AWS Application Load Balancer
- HTTPS via ACM certificate
- Route53 DNS routing
- Kubernetes Ingress

This allows external users to access the platform through a secure public domain.

---

# 🏗 Architecture

```
GitHub
   ↓
GitHub Actions (CI)
   ↓
Amazon ECR
   ↓
ArgoCD (GitOps CD)
   ↓
Amazon EKS (Kubernetes)
   ↓
AWS Load Balancer Controller
   ↓
Application Load Balancer (ALB)
   ↓
Route53 DNS
   ↓
futurecars.anzyworld.com
```

---

# ⚙️ Implementation Steps

## 1️⃣ Install AWS Load Balancer Controller

The AWS Load Balancer Controller was installed using Helm and configured with the correct cluster VPC.

```bash
helm upgrade --install aws-load-balancer-controller eks/aws-load-balancer-controller \
-n kube-system \
--set clusterName=eks-gitops-cluster \
--set serviceAccount.create=false \
--set serviceAccount.name=aws-load-balancer-controller \
--set region=us-east-1 \
--set vpcId=vpc-0bdeb87bda8f53224
```

This controller enables Kubernetes to automatically provision AWS ALBs from Ingress resources.

---

## 2️⃣ Create Kubernetes ALB Ingress

A Kubernetes Ingress resource was created to expose the frontend service through an AWS Application Load Balancer.

File:

```
k8s/base/alb-ingress.yaml
```

Example configuration:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: frontend-alb-ingress
  annotations:
    alb.ingress.kubernetes.io/scheme: internet-facing
    alb.ingress.kubernetes.io/target-type: ip
    alb.ingress.kubernetes.io/listen-ports: '[{"HTTP":80},{"HTTPS":443}]'
    alb.ingress.kubernetes.io/ssl-redirect: '443'
    alb.ingress.kubernetes.io/certificate-arn: <ACM_CERTIFICATE_ARN>
spec:
  ingressClassName: alb
  rules:
  - host: futurecars.anzyworld.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: frontend-service
            port:
              number: 80
```

ArgoCD automatically deployed this resource from Git.

---

## 3️⃣ Automatic ALB Provisioning

Once the Ingress resource was applied, the AWS Load Balancer Controller automatically created:

- Application Load Balancer
- Target Groups
- Security Groups
- HTTPS listeners

Verification command:

```bash
kubectl get ingress
```

Example output:

```
frontend-alb-ingress   alb   futurecars.anzyworld.com
k8s-default-frontend-xxxxx.us-east-1.elb.amazonaws.com
```

---

## 4️⃣ Create ACM SSL Certificate

Terraform was used to create an ACM certificate for the domain:

```
futurecars.anzyworld.com
```

Example Terraform configuration:

```hcl
resource "aws_acm_certificate" "futurecars" {
  domain_name       = "futurecars.anzyworld.com"
  validation_method = "DNS"
}
```

DNS validation was automatically completed through Route53.

---

## 5️⃣ Route53 Domain Routing

Terraform created a Route53 alias record pointing the domain to the ALB.

Example configuration:

```hcl
resource "aws_route53_record" "futurecars_alias" {
  zone_id = data.aws_route53_zone.main.zone_id
  name    = "futurecars.anzyworld.com"
  type    = "A"

  alias {
    name                   = data.aws_lb.futurecars_alb.dns_name
    zone_id                = data.aws_lb.futurecars_alb.zone_id
    evaluate_target_health = true
  }
}
```

---

# 🌐 Application Access

The application is now accessible via:

```
https://futurecars.anzyworld.com
```

Traffic flow:

```
Internet
   ↓
Route53
   ↓
Application Load Balancer
   ↓
Kubernetes Ingress
   ↓
Frontend Service
   ↓
Pods
```

---

# 🔄 GitOps Deployment Flow

All infrastructure and Kubernetes resources are managed through Git.

```
Developer → Git Push → GitHub → GitHub Actions → ECR
                         ↓
                      ArgoCD
                         ↓
                     Kubernetes
                         ↓
                         ALB
```

---

# 📸 Deployment Verification

Screenshots included in this phase:

- ArgoCD application synced and healthy
- Kubernetes ingress showing ALB address
- Application accessible via custom domain

---

# 🧠 Key DevOps Concepts Demonstrated

- Kubernetes Ingress
- AWS Load Balancer Controller
- ALB provisioning from Kubernetes
- HTTPS with ACM
- Infrastructure as Code (Terraform)
- GitOps deployment with ArgoCD
- DNS routing with Route53

---

# ✅ Phase Outcome

✔ Production-grade ingress  
✔ Automatic ALB provisioning  
✔ HTTPS enabled  
✔ Custom domain routing  
✔ GitOps-managed infrastructure  

<img width="1218" height="895" alt="Screenshot 2026-03-24 at 11 30 22" src="https://github.com/user-attachments/assets/708a99c6-4022-4fe5-bc5b-25b17fa43072" />
<img width="1376" height="894" alt="Screenshot 2026-03-24 at 11 31 57" src="https://github.com/user-attachments/assets/c2714ecc-28d6-41fc-953b-f488acf0281c" />
<img width="1470" height="956" alt="Screenshot 2026-03-24 at 11 32 59" src="https://github.com/user-attachments/assets/8edba4e9-03f3-4488-8286-6779e6ebb20e" />
<img width="1470" height="956" alt="Screenshot 2026-03-24 at 11 37 15" src="https://github.com/user-attachments/assets/a219d1c6-f26f-4cd9-9e61-2d3455a4478e" />

---

## Phase 7b — Production Hardening

In this phase, the Kubernetes deployment was improved to behave more like a **real production workload**.

The following improvements were implemented:

### Resource Limits

Resource requests and limits were added to prevent containers from consuming excessive cluster resources.

```yaml
resources:
  requests:
    cpu: "100m"
    memory: "128Mi"
  limits:
    cpu: "250m"
    memory: "256Mi"

### Health Checks

Liveness and readiness probes were added so Kubernetes can automatically detect unhealthy containers and restart them if needed.

```bash
readinessProbe:
  httpGet:
    path: /
    port: 5000
  initialDelaySeconds: 5
  periodSeconds: 10

livenessProbe:
  httpGet:
    path: /
    port: 5000
  initialDelaySeconds: 15
  periodSeconds: 20
```

### Horizontal Pod Autoscaler (HPA)

An HPA was configured to automatically scale the application pods based on CPU utilization.

```bash
kubectl autoscale deployment frontend \
  --cpu-percent=50 \
  --min=2 \
  --max=5
```
Result

These improvements increased the reliability and resilience of the application by enabling:

Automatic container restarts
Better resource management
Automatic scaling under load


## Phase 8 — Build the FutureCars Website
To demonstrate the full GitOps pipeline, **a sample application called FutureCars** was created

The application is a futuristic concept website showcasing rare vehicles that can be reserved today but delivered in 2055.

- Application Features
- Built using Python Flask
- Deployed as a Docker container
- Stored in Amazon ECR
- Deployed automatically via ArgoCD
- Exposed through AWS ALB Ingress
- Secured with HTTPS and Route53 domain

**CI/CD Pipeline**
```bash
GitHub
   ↓
GitHub Actions
   ↓
Docker Image Build
   ↓
Amazon ECR
   ↓
ArgoCD GitOps Deployment
   ↓
Amazon EKS
```

**Website Access**

The application was deployed publicly at:
```bash
https://futurecars.anzyworld.com
```

The site displays futuristic concept vehicles such as:

- Tesla XR Infinity
- BMW Nebula IX
- Mercedes Vision Æon
- Porsche Eclipse 9110
- Lucid Astral GT
- Cadillac Quantum Limo
- DeLorean Thunderflight

The frontend demonstrates how application updates flow through the **GitOps pipeline into Kubernetes automatically.**

<img width="2940" height="1912" alt="image" src="https://github.com/user-attachments/assets/65517037-b114-43a2-8a36-4e21172d5d94" />
<img width="2940" height="1912" alt="image" src="https://github.com/user-attachments/assets/22c55afa-1fa1-4d0d-9588-4dd6cbdd4461" />
<img width="2940" height="1912" alt="image" src="https://github.com/user-attachments/assets/554571f8-1693-4ede-9f2f-0213f1da2b45" />
<img width="2940" height="1912" alt="image" src="https://github.com/user-attachments/assets/ae88661e-529e-40e9-bdb8-f04aca4db3d4" />
<img width="2940" height="1912" alt="image" src="https://github.com/user-attachments/assets/033f61ae-bdca-4e4e-b6e8-d309a6e2fe1b" />
<img width="2940" height="1912" alt="image" src="https://github.com/user-attachments/assets/179f313d-4bf6-4dd3-b579-0d979a12a766" />


## Conclusion

This project demonstrates a complete cloud-native DevOps platform built using modern tools and best practices.

Technologies used:

Terraform (Infrastructure as Code)
Amazon EKS (Kubernetes)
ArgoCD (GitOps continuous delivery)
GitHub Actions (CI pipeline)
Amazon ECR (container registry)
Prometheus & Grafana (monitoring)
AWS ALB + Route53 + ACM (secure ingress)

The platform shows how infrastructure, applications, and deployments can be managed entirely through Git-based workflows.

Due to AWS cost considerations, the environment was paused during development and fully torn down after completing the project, while the repository continues to document the full architecture and implementation.

This project highlights practical DevOps skills in Kubernetes operations, GitOps deployment, cloud infrastructure automation, and observability.


