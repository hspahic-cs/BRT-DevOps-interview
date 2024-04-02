#!/bin/bash

kubectl apply -f application/configmap.yaml
kubectl apply -f application/secret.yaml
kubectl apply -f database/secret.yaml

kubectl apply -f database/storage.yaml
kubectl apply -f application/storage.yaml

kubectl apply -f database/deployment.yaml
kubectl apply -f application/deployment.yaml

kubectl apply -f database/service.yaml
kubectl apply -f application/service.yaml
