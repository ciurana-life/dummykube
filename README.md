# dummykube

Dummy project to test kubernettes.

## Install (Specific for Apple M1):

Requirements:
1. Xcode required ? (From app store)
2. You need Docker M1 version [click on Apple Chip](https://docs.docker.com/docker-for-mac/install/)

Install minikube:
```
brew update
brew install minikube
```

Then:
```
minikube start --driver=docker
```

## Command list

General info:
1. `kubectl get nodes`.
2. `minikube status`.
3. `kubectl version`.
4. `kubectl get pod` list smallest units, `-o wide` to get ip.
5. `kubectl get replicaset`.
6. `kubectl get deployment`.
7. `kubectl get services`.

---

You will never do this by hand, but it is possible to create a pod (from deployment) with the command:
`kubectl create deployment nginx-deply --image=nginx`

It is possible to directly edit the config created by kubernetes with `kubectl edit deployment nginx-deply`, if you edit something it will create and start a new pod and terminate the old one.

---

Debugging:
1. `kubectl logs PODNAME`, you can get the pod name with `kubectl get pod`.
2. `kubectl describe pod PODNAME`
3. `kubectl exec -it PODNAME -- bin\bash`, you get a terminal inside the pod (docker).
    - **M1 error, maybe because no specifying --platform on docker**

Deleting:
1. Deleting by deployment `kubectl delete deployment DEPLOYMENTNAME` (nginx-deply for this example).
2. Deleteing by file `kubectl delete -f FILE.yml`.

## Secrets
They live in repo for now.
TODO: use sops.

To add secrets as base64:
```
echo -n 'some-secret-info' | base64
```

Order of creation matters if you reference a secret from another file.
