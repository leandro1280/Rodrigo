import urllib.request
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def fetch_images(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        response = urllib.request.urlopen(req, context=ctx)
        html = response.read().decode('utf-8')
        images = set(re.findall(r'src="(https://[^"]+(?:jpg|jpeg|webp|png))"', html))
        return list(images)
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return []

urls = [
    'https://www.lavoz.com.ar/buscar/rodrigo+de+loredo/',
    'https://www.infobae.com/tag/rodrigo-de-loredo/',
    'https://www.clarin.com/tema/rodrigo-de-loredo.html'
]

for url in urls:
    print(f"Images from {url}:")
    for img in fetch_images(url)[:5]:
        print(img)
