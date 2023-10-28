#post请求

import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/v2transapi?'

headers =  {"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.57"}

data = {'from': 'en',
'to': 'zh',
'query': 'spider',
'transtype': 'realtime',
'simple_means_flag': 3,
'sign': '63766.268839',
'token': '56494c8d0601c8a893977fcd7eb1a4e9',
'domain': 'common',
'ts': '1697941276067'}
#post请求的参数 必须要进行编码

data = urllib.parse.urlencode(data).encode('utf-8')

#post请求的参数 必须要进行编码
#post请求的参数是不会拼接在url后面的 而是需要放在请求对象定制的参数中


request = urllib.request.Request(url=url, data=data, headers=headers)

# print(request)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)

#字符串 -> json对象
import json
obj = json.loads(content)
print(obj)

#post请求方式的参数必须编码 data = urllib.parse.urlencode(data).encode('utf-8')
# #编码之后必须调用encode方法 data = urllib.parse.urlencode(data).encode('utf-8')
#参数是放在请求对象定制的方法中 request = urllib.request.Request(url=url, data=data, headers=headers)