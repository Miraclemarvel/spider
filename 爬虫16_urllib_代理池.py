proxies_pool = [
    {'http': '113.124.85.240:9999'},
    {'http': '182.34.27.55:9999'}
]

import random

proxies = random.choice(proxies_pool)

import urllib.request

url = 'https://ip.900cha.com/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.57'}

request = urllib.request.Request(url=url, headers=headers)

handler = urllib.request.ProxyHandler(proxies)
opener = urllib.request.build_opener()
response = opener.open(request)
content = response.read().decode('utf-8')

with open('daili2.html', 'w', encoding='utf-8') as f:
    f.write(content)