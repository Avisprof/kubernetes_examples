**How to run?**


1. Run a config [nginx.yaml](nginx.yaml) file:
`kubectl apply -f nginx.yaml`
<br>
2. Start the tunnel to the LoadBalancer:
`minikube tunnel`
<br>
3. Get info about the deployment:
`kubectl get all`
![01_get_all.png](./pics/01_get_all.png)
<br>
4. Check deployment with the browser:
![02_localhost.png](./pics/02_localhost.png)
1
![1](nginx_minikube/pics/01_get_all.png)

2
![2](/nginx_minikube/pics/01_get_all.png)

3
![3](./nginx_minikube/pics/01_get_all.png)

4
![4](./pics/01_get_all.png)

5
![5](pics/01_get_all.png)
