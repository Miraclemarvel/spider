import urllib.request

# 需求: 使用handler访问百度 获取网页源码

url = 'http://www.baidu.com'

headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61'}

request = urllib.request.Request(url=url,headers=headers)

#handler  build_opener   open
# (1)获取handler对象
handler = urllib.request.HTTPHandler()

# (2)获取opener对象
opener = urllib.request.build_opener(handler)

# (3)调用open方法
response = opener.open(request)

content = response.read().decode('utf-8')

print(content)