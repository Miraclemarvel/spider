# 通过登录  然后进入到主页面

# __VIEWSTATE: lS5BoSUWci7lagx0D892Qs3nBqqATcG4IBGNtAvHUPeC58pmsOEBSZ6L5snyewOeasMDzdBR2dora/QBWhk2pdQDm/ROzwEStBFMc+gI6+lShJaAb14XxzlJfTT/svw5ss10sem5xg9EgsxHEexQgL9jB1Y=
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://so.gushiwen.cn/user/collect.aspx
# email: 2942486336@qq.com
# pwd: shang123
# code: D8RG
# denglu: 登录

#我们观察到 __VIEWSTATE  __VIEWSTATEGENERATOR  code是一个可以变化的量

# 难点: (1) __VIEWSTATE  __VIEWSTATEGENERATOR  一般情况下看不到的数据 都是在页面的源码中
#           我们观察到这两个数据在页面的源码中 所以我们需要获取页面的源码 然后进行解析就行了
#       (2) 验证码

import requests
#这是登录页面的url地址
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

headers={'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61'}

#获取网页源码
response = requests.get(url=url, headers=headers)
content = response.text

# 解析页面源码
from bs4 import BeautifulSoup
soup = BeautifulSoup(content, 'lxml')

# 获取__VIEWSTATE
viewstate = soup.select('#__VIEWSTATE')[0].attrs.get('value')
viewstategenerator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')

code = soup.select('#imgCode')[0].attrs.get('src')
code_url = 'https://so.gushiwen.cn' + code

# 有坑!!!
# 获取到验证码的图片之后 下载到本地 然后观察验证码 观察之后 然后在控制台输入验证码 就可以给code的参数 就可以登录
# import urllib.request
# urllib.request.urlretrieve(url=url, filename='code.jpg')
# requests里面有一个方法 session(), 通过session的返回值 就能使请求变成一个对象

session = requests.session()
# 验证码的url的内容
response_code = session.get(code_url)
#注意此时要使用二进制数据 因为我们使用的是图片的下载
content_code = response_code.content
#wb模式: 将二进制数据写入文件
with open('code.jpg', 'wb') as f:
    f.write(content_code)


# code_name = input('请输入你的验证码: ')
import ddddocr
ocr = ddddocr.DdddOcr()
with open('code.jpg', 'rb') as f:
    Img_code = f.read()
res = ocr.classification(Img_code)

#点击登录
url_post = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
data_post = {'__VIEWSTATE': viewstate,
             '__VIEWSTATEGENERATOR': viewstategenerator,
             'from': 'http://so.gushiwen.cn/user/collect.aspx',
             'email': '18872016683',
             'pwd': 'shang123',
             'code': res,
             'denglu': '登录'}

response_post = session.post(url=url, data=data_post, headers=headers)

content_post = response_post.text

with open('gushiwen.html', 'w', encoding='utf-8') as f:
    f.write(content_post)

# print(content)

#难点:
# (1)隐藏域
# (2)验证码