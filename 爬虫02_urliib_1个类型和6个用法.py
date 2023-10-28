import urllib.request

url = 'https://www.baidu.com/'

#模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

#一个类型和六个方法
#response是HTTPresponse类型
#print(type(response))

#按照一字节一字节的去读
# content = response.read()
# print(content)

#返回多少个字节
# content = response.read(5)
# print(content)

#读取一行
# content = response.readline()
# print(content)

#一行一行的去读
# content = response.readlines()
# print(content)

#f返回状态码 如果是200 那就证明我们的逻辑没错
#print(response.getcode())

#返回的是url地址
# print(response.geturl())

#获取的是一个状态信息
# print(response.getheaders())

#一个类型 HTTPresponse
#六个方法 read  readline  readlines  getcode  geturl  getheaders