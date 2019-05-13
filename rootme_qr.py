import requests
from pyzbar.pyzbar import decode
from base64 import b64decode
from bs4 import BeautifulSoup
from PIL import Image
from PIL import ImageDraw
import io

url = "http://challenge01.root-me.org/programmation/ch7/"

s = requests.Session()
r = s.get(url)

soap = BeautifulSoup(r.content,"html.parser")
src = soap.find("img")['src']
dataB64 = src.split(",")[1]
image = Image.open(io.BytesIO(b64decode(dataB64)))
d = ImageDraw.Draw(image)
line_color = (0, 0, 0)
d.rectangle([30,30,60,60], fill=line_color, width=15)
d.rectangle([270,30,240,60], fill=line_color, width=2)
d.rectangle([30,270,60,240], fill=line_color, width=2)
#verhnii levii
d.line([10,14,80,14], fill=line_color, width=10)
d.line([14,14,14,80], fill=line_color, width=10)
d.line([10,75,75,75], fill=line_color, width=10)
d.line([75,15,75,80], fill=line_color, width=10)
#niznii levii
d.line([9,300-16,80,300-16], fill=line_color, width=10)
d.line([14,300-14,14,300-80], fill=line_color, width=10)
d.line([10,300-76,76,300-76], fill=line_color, width=10)
d.line([76,300-14,76,300-80], fill=line_color, width=10)

#verhnii pravo
d.line([300-14,14,300-14,80], fill=line_color, width=10)
d.line([240-14,14,240-14,80], fill=line_color, width=10)
d.line([225,75,225+60,75], fill=line_color, width=10)
d.line([222,14,225+66,14], fill=line_color, width=10)

qr = decode(image)[0]
q = str(qr.data).split(' ')[3]
print(q)
payload={'metu':q.replace('\'','')}
rr = s.post(url, payload)
soapr = BeautifulSoup(rr.content,"html.parser")
print(soapr.find('p'))
