#!/bin/bash

# ====== DO NOT RUN BASH SCRIPT, ORDER PROVIDED IN README ======

# Apply configuration maps and secrets
kubectl apply -f application/configmap.yaml
kubectl apply -f application/secret.yaml
kubectl apply -f database/secret.yaml
sleep 2  # Pause for 2 seconds

# Apply storage configurations
kubectl apply -f database/storage.yaml
kubectl apply -f application/storage.yaml
sleep 2  # Pause for 2 seconds

# Apply services
kubectl apply -f database/service.yaml
kubectl apply -f application/service.yaml
# Repeat to apply service IP
kubectl apply -f application/configmap.yaml
sleep 2  # Pause for 2 seconds

# Deploy database and application
kubectl apply -f database/deployment.yaml
kubectl apply -f application/deployment.yaml
sleep 2  # Pause for 2 seconds

# Apply jobs
kubectl apply -f application/jobs.yaml