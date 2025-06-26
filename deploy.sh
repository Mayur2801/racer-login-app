#!/bin/bash
# Deploy the racer-login-app to Kubernetes

kubectl apply -f ./racer-login-app/k8s/deployment.yaml
kubectl apply -f ./racer-login-app/k8s/service.yaml 