**How to run?**


1. Run a config [nginx.yaml](/nginx_minikube/nginx.yaml) file:
`kubectl apply -f nginx.yaml`
<br>
2. Start the tunnel to the LoadBalancer:
`minikube tunnel`
<br>
3. Get info about the deployment:
`kubectl get all`
![01_get_all.png](/nginx_minikube/pics/01_get_all.png)
<br>
4. Check deployment with the browser:
![02_localhost.png](/nginx_minikube/pics/02_localhost.png)


