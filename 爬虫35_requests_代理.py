import requests

url = 'https://www.baidu.com/s?'

headers = {'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61'}

data = {'wd': 'IP'}

proxy = {'http': '123.169.34.216:9999'}

response = requests.get(url=url, params=data, headers=headers, proxies=proxy)

content = response.content.decode('utf-8')

print(content)


