import requests
from bs4 import BeautifulSoup

url = 'http://www.amazon.com'
url = 'http://www.amazon.com/Wind-Through-Keyhole-Tower-Novel-ebook/dp/B005GG0MTC/ref=tmm_kin_swatch_0?_encoding=UTF8&sr=&qid='

response = requests.get(url)

print(response.status_code)
print(response.headers['content-type'])
print(response.encoding)

content = response.content

soup = BeautifulSoup(content)

samples = soup.find_all("a")

samples[0]
