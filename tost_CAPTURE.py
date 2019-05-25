from base64 import b64decode
from bs4 import BeautifulSoup
import requests
import io
import pytesseract
try:
    import Image
except ImportError:
    from PIL import Image
url="http://challenge01.root-me.org/programmation/ch8/"
prox = {'http': 'http://127.0.0.1:8080'}
s = requests.Session()
res = s.get(url,proxies=prox)
soup = BeautifulSoup(res.content, "html.parser")
img=soup.find('img')['src']
capture=img.split(',')[1]

image_string = io.BytesIO(b64decode(capture))

image = Image.open(image_string)

bg = Image.new("RGB", image.size, (255,255,255))

bg.paste(image)

answer = pytesseract.image_to_string(bg)
print(answer)
r = s.post(url,{"cametu":answer},proxies=prox)
print (r.content)