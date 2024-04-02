# BRT-DevOps-interview

# Kubernetes Application Deployment Guide

## Introduction

This guide describes the steps necessary to deploy the "Pizza Ordering" application on a Kubernetes cluster. Before you begin, ensure you have the necessary prerequisites installed and configured.

### Prerequisites

- kubectl 
- Docker
- minikube
- git
- python==3.10.12
- pip==24.0

## Deployment Steps

### Step 1: Clone the Repository

Clone the repository containing your Kubernetes manifests:

```bash
git clone git@github.com:hspahic-cs/BRT-DevOps-interview.git
cd BRT-DevOps-interview
```

### STEP 2: Create a Minikube Cluster

Start a "minikube" cluster to prepare for kubernetes deployment. To make
sure everything configured correctly, check the minikube status.

```bash
minikube start
minikube status
```

### STEP 3: Switch Minikube Docker Daemon

Minikube comes installed with its own Docker daemon. In order to make your
Docker images accessible to the minikube cluster, we will point our terminal
to the minikube's Docker daemon. 

There are alternatives to this method, and for more details I'll I've provided
documentation [here](https://minikube.sigs.k8s.io/docs/handbook/pushing/).

```bash
eval $(minikube docker-env)
```

### STEP 4: Build & Push Docker Images

Navigate to the .../BRT-DevOps-interview/kubernetes/proxy folder and run the docker build
command with the label "django-proxy".

```bash
cd your-registry/BRT-DevOps-interview/kubernetes/proxy
docker build -t django-proxy .
```

Repeat the process in the .../BRT-DevOps-interview/web folder and run the docker build
command with the label "brt_devops_interview"

```bash
cd your-registry/BRT-DevOps-interview/web
docker build -t brt_devops_interview .
```

### STEP 5: Deploying with Kubernetes 

Now that we have our Docker images accessible to minikube, we can deploy our kubernetes application.
I've provided a helper file with all the necessary commands. For your convenience I'll attach them here.
!!Make sure you are in the kubernetes directory before attempting these commands!!

``` bash
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
```

Once these commands have been run, I suggest checking to see if the storage and services were properly created. 

``` bash
kubectl get pvc
kubectl get pv
kubectl get services
```

or 

```bash
minikube dashboard
```

#### STEP 5.1: Adjusting Postgres Host

Before we continue, we need to change the .../kubernetes/application/configmap.yaml file in order to have our application
properly connect to the postgres database. 

Look at the output of *kubectl get services* and look for the *ip* of the *django-postgres* service.
Go into the .../kubernetes/application/configmap.yaml and change the *POSTGRES_HOST* variable to be
the new *ip*.

#### STEP 5.2: Continue Deployment

Run the following. We'll start with applying the new ip from the configmap file. Then we can send out
our application and database deployment. Once those are done, we'll schedule a job to migrate our database
and create a superuser for testing purposes.

```bash
kubectl apply -f application/configmap.yaml
sleep 2  # Pause for 2 seconds

# Deploy database and application
kubectl apply -f database/deployment.yaml
kubectl apply -f application/deployment.yaml
sleep 2  # Pause for 2 seconds

# Apply jobs
kubectl apply -f application/jobs.yaml
```

Make sure to test the deployments and jobs to see if they were deployed correctly. You can do this using the, 
```bash
minikube get deployments
minikube get jobs
``` 
commands, or through the minikube dashboard.

### Step 6: Enable Tunnel to App

Given that minikube is run locally, we do not have an external ip to access our cluster's services. We need to 
expose our services to our local host machine for testing and we do this via the *minikube service* command. 
First we get the service we'd like to expose: *django*. Then we open a second terminal in order to keep a continous
tunnel from our service to our host machine.

```bash 
minikube service django
```

You should now be able to access our app via the link that gets provided. 

Brief aside, there were some dependency issues with the service command and the firefox browser. If you are having
issues getting localhost to appear, try switching your default browser. Brave worked well for me.

### Step 7: Enjoy Your Hard Earned Pizza
![Alt Text](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNnU1azlvZHZiZWZxNjgxaDRva3FrcHRscW10bWo5ZjN1cDUxd3pleCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/tIQxZUG8NjarN8AGVK/giphy.gif)

ENJOY :D