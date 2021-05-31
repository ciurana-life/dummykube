`docker build -f Dockerfile -t dummy-flask:latest .`
`docker run -p 5000:5000 dummy-flask`
Will show results here `http://127.0.0.1:5000/`.
Kill it.

You need to enable it to pull images from docker descktop.
`kubectl config use-context docker-desktop`
`kubectl apply -f deployment.yaml`
`kubectl get pods`

Aaaaand is not working lol.
