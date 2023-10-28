import requests
# urllib
# (1) 一个类型以及六个方法
# (2) get请求
# (3) post请求  百度翻译
# (4) ajax的get请求
# (5) ajax的post请求
# (6) cookie登录 微博
# (7) 代理

# requests
# (1) 一个类型以及六个属性
# (2) get请求
# (3) post请求
# (4) 代理
# (5)cookie 验证码

url = 'https://www.baidu.com/s'

headers = {'Cookie':
                   'BDUSS=ZEeENCYklUblBWUE1QdmRjTlc5UEtkWFNwbHh4SkJHcTNKS0JVRkM4fkhENU5rSVFBQUFBJCQAAAAAAAAAAAEAAABQJKVrTWlyTWFydmVsAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMeCa2THgmtkdX; BDUSS_BFESS=ZEeENCYklUblBWUE1QdmRjTlc5UEtkWFNwbHh4SkJHcTNKS0JVRkM4fkhENU5rSVFBQUFBJCQAAAAAAAAAAAEAAABQJKVrTWlyTWFydmVsAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMeCa2THgmtkdX; BAIDUID=5714F83FD829786045ACF99AB80ED0BF:FG=1; newlogin=1; PSTM=1697886916; BD_UPN=12314753; BIDUPSID=A25F3A688D747FD6EC75B988ECB88075; BAIDUID_BFESS=5714F83FD829786045ACF99AB80ED0BF:FG=1; ZFY=9ZUDnOsfneRPNnmV6VwT5YD3tCX8olUQce27S87g08I:C; COOKIE_SESSION=36747047_0_6_5_3_9_1_0_6_5_0_0_36747007_0_1_0_1697983624_0_1697983623%7C6%230_0_1697983623%7C1; BA_HECTOR=8k2121018h018g058l05250s1ijf0851o; BDRCVFR[DzC1COp47gC]=aeXf-1x8UdYcs; BD_CK_SAM=1; PSINO=6; H_PS_PSSID=39324_39396_39530_39418_39541_39521_39497_39479_39234_26350; delPer=0; sugstore=1; H_PS_645EC=47eeIkoUe3AVhdIGI8EAQK1K46ALeJ4INt6NYsdrXi%2FQ7an7E2fKbq3zU2o; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; baikeVisitId=a7d8b55a-747c-490c-9dd1-cde900b9325a; B64_BOT=1',
           'User-Agent':
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61'
        }

data ={'kw':
       '北京'}

#url 请求资源路径  params 参数   kwargs 字典

response = requests.get(url=url, params=data, headers=headers)

content = response.content.decode('utf-8')

print(content)

# 总结:参数使用parmas传递
# 参数无需urlencode编码
#不需要请求对象的定制
#请求资源路径中的?可以加也可以不加