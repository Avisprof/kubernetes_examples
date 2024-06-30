**How to run?**


1. Run a config [fastapi.yaml](/fastapi_example/fastapi.yaml) file:
<br>`kubectl apply -f fastapi.yaml`</br>

2. Get info about ingress:
<br>`kubectl get ing`</br>
<br>![01_get_ing.png](/fastapi_example/pics/01_get_ing.png)</br>

3. Add the line into the `hosts` file (C:\Windows\System32\drivers\etc)
<br>`37.18.118.82 avisprof.local`</br>

4. Check deployment with the browser:
<br>`https://avisprof.local/server/`</br>
<br>![02_check.png](/fastapi_example/pics/02_check.png)</br>

5. Check the long duration function (10 seconds):
<br>`https://avisprof.local/server/predict`</br>
<br>![03_predict.png](/fastapi_example/pics/03_predict.png)</br>