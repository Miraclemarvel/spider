import urllib.request

url = 'https://www.baidu.com/'

#url的组成
#https://cn.bing.com/search?q=%E4%B8%AD%E5%9B%BD%E5%9C%B0%E8%B4%A8%E5%A4%A7%E5%AD%A6

#http/https  www.cug.edu.cn     80/443      search       q = 中国地质大学      #
#  协议           主机            端口号        路径              参数          锚点
#http 80   https 443
#mysql 3306  oracle 1521  redis 6379 mongodb 27017

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.57'}

#第一个反爬: UA反爬
#因为urlopen方法中不能存储字典 所以headers不能传递进去
#请求对象的定制
#注意 因为参数顺序的问题 不能直接写url 和headers 中间还有data  所以我们还需要关键字传参
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)