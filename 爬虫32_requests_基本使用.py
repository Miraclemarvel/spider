import requests

url = 'https://www.baidu.com'

response = requests.get(url)

# 一个类型和六个属性
# <class 'requests.models.Response'>
# print(type(response))

# 设置响应的编码格式
# response.encoding = 'utf-8'

# 以字符串的形式返回网页的源码  *****
# print(response.text)

# 返回一个url地址
# print(response.url)

# 返回的是二进制的数据
# print(response.content)

# 返回响应的状态码
# print(response.status_code)

# 返回响应头的信息
# print(response.headers)