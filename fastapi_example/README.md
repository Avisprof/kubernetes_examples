**How to run?**


1. Run a config [fastapi.yaml](/fastapi_example/fastapi.yaml) file:
`kubectl apply -f fastapi.yaml`
<br>
2. Get info about ingress:
`kubectl get ing`
![01_get_ing.png](/fastapi_example/pics/01_get_ing.png)
<br>
3. Add the line into the `hosts` file (C:\Windows\System32\drivers\etc)
`37.18.118.82 avisprof.local`
<br>
4. Check deployment with the browser:
`https://avisprof.local/server/`
![02_check.png](/fastapi_example/pics/02_check.png)

5. Check the long duration function (10 seconds):
`https://avisprof.local/server/predict`
![03_predict.png](/fastapi_example/pics/03_predict.png)