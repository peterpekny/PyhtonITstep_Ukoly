# web_scraping.py
# ---------------
import re
import requests
import json

url = 'https://mobil.bazos.cz'
response = requests.get(url)

rx_pattern = r'<div class="inzeratynadpis">\s*<a href="(.*?)">\s*<img src="(.*?)\?.*?" alt="(.*?)"'
rx_bazos = re.compile(rx_pattern)

result = rx_bazos.findall(response.text)

data = []

for url, img, title in result:
     item = {'url': url, 'img': img, 'title': title}
     data.append(item)

with open('09/data.json', mode='w', encoding='utf-8') as file:
     json.dump(data, file, indent=4)

print(result)
print('=====================================================')
print(data)