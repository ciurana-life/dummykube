# README
Dummy project that just returns "hello world".


## 1 - Build the Docker image
To run it on k8s you need first the Docker image:
```
docker build -f Dockerfile -t dummy-django:latest .
```

Test it runs:
```
docker run -p 8000:8000 dummy-django
```

## 2 - Apply the kubernetes configuration

`kubectl config use-context docker-desktop`
`kubectl apply -f k8s/deployment.yaml`
`kubectl get pods`
`kubectl describe deploy`

`kubectl apply -f k8s/service.yaml`

Get the last port
```
kubectl get svc dummy-django-app
NAME               TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
dummy-django-app   NodePort   10.110.10.224   <none>        8000:**30970**/TCP   83s
```

Check all works: `127.0.0.1:30970`
