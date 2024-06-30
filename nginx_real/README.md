**How to run?**


1. Run a config [nginx.yaml](/nginx_real/nginx.yaml) file:
`kubectl apply -f nginx.yaml`
<br>
2. Get info about the deployment:
`kubectl get all`
![01_get_all.png](/nginx_real/pics/01_get_all.png)
<br>
3. Get info about ingress:
`kubectl get ing`
![02_get_ing.png](/nginx_real/pics/02_get_ing.png)
<br>
4. Add the line into the `hosts` file (C:\Windows\System32\drivers\etc)
`37.18.118.82 avisprof.local`
<br>
5. Check deployment with the browser:
![03_check_browser.png](/nginx_real/pics/03_check_browser.png)
