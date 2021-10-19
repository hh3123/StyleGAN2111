import secrets, json, re, pathlib, getpass, time, os
model = !nvidia-smi
GPU = model[8]
model
def restart():
  os.kill(os.getpid(), 9)

if (2>1):
  !curl -LJOk https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
  !unzip -n ngrok-stable-linux-amd64.zip


  region = 'eu'
  get_ipython().system_raw("./ngrok http -region {} 8889 &".format(region))

  !sleep 5
  tunnels = !curl -s http://localhost:4040/api/tunnels
  url = json.loads(tunnels[0])["tunnels"][1]["public_url"]
  !sleep 1
  print("Vse work ssulka " + url)
  !jupyter notebook --ip 0.0.0.0 --port 8889 --allow-root
  time.sleep(90)
  while 5<6:
    time.sleep(5)
    print('Marat')
else:
  print("BAD GPU CHANGE")
  restart()
