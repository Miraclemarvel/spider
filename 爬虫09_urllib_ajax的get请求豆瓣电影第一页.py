
# get请求
# 获取豆瓣电影第一页的数据并且保存起来

import urllib.request
import urllib.parse

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'

headers = {'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.57'}

#(1)请求对象的定制
request = urllib.request.Request(url=url,headers=headers)

#(2)获取响应的程序
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

# print(content)

#(3)将获取内容下载到本地
# open方法默认情况下使用的是gbk编码 如果我们想保存汉字中文 我们需要在open方法中指定编码格式为utf-8
# f = open('douban.json', 'w', encoding='utf-8')
# f.write(content)

with open('douban1.json', 'w', encoding='utf-8') as f:
    f.write(content)
