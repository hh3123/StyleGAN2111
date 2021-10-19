import secrets, json, re, pathlib, getpass, time, os

!curl -LJOk https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
!unzip -n ngrok-stable-linux-amd64.zip
region = 'eu'
get_ipython().system_raw("./ngrok http -region {} 8889 &".format(region))
!sleep 5
tunnels = !curl -s http://localhost:4040/api/tunnels
url = json.loads(tunnels[0])["tunnels"][1]["public_url"]
!sleep 1
print(url)
!jupyter notebook --ip 0.0.0.0 --port 8889 --allow-root
