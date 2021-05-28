Command order

```
# cd dummy-mongo
kubectl apply -f mongo-secret.yml
kubectl apply -f mongo-deploy.yml
kubectl apply -f mongo-configmap.yml
kubectl apply -f mongo-express.yml
minikube service mongo-express-service
```