**How to run?**

1. Run a config [nginx.yaml](nginx.yaml) file:
`kubectl apply -f nginx.yaml`


2. Start the tunnel to the LoadBalancer:
`minikube tunnel`


3. Get info about the deployment:
`kubectl get all`
![01_get_all.png](./pics/01_get_all.png)


4. Check deployment with the browser:
![02_localhost.png](./pics/02_localhost.png)
