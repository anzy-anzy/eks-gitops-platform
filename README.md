# EKS GitOps Platform

This repository contains:

- Microservices source code
- Docker configurations
- Kubernetes manifests
- Argo CD applications
- GitHub Actions CI pipelines

Implements a GitOps-based deployment to AWS EKS.


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
