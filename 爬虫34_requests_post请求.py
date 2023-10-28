import requests

url = 'https://fanyi.baidu.com/v2transapi?'

headers = { 'Accept':'*/*',
            #'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Acs-Token':'1698228881493_1698228881318_C96HSitbHWl/bpGSHx5zDrP5AzLP6DSKOGI0u7+H8aQqQe+XANJipO7AL3QEgSeO1s8oxyIFqtZQjiiLucPZOSOsjhgwJb8sfzyUwtFAteJgOaCzdxoJwdtDx0KJqFXzrryeRiI0YsvnZEuxf/HUXrpY5WQxzAehCNLKt7FOlAfftEt3Kd+RqxJ+tI8xgn+VOZPzaiRF08nbKxgYeFAzzaEN+Ax2I8JSE5SKGVSVmV63eCY4w3yIQPoCA3gyzbeTKPcLBN3F9ZD+cK4zxl9Y5xpoiu5R+sCRnXUgPgMLPv5FHZ5DKxOxt2YkG3bYdp5NiW7KDDBKDdwpC2tgZxdo3zqv7dSGiF1LOophFfkivjCPM8QtA0VXIpT4/+e9vUJF2jSvSUua7PZNjjC6YwuQw/hzH4yMPOOezVFAOhHv2saQVasnAVmp4l7x36DsHad7qzDM9h9qFVEMOiBcEKGXn+2Nn2Ez7cDQoRqUxjDMBsiPWM/r+lFCLh6pVo3h2ICPOpKjNS/f3KJuNdmngZNJFg==',
            'Connection':'keep-alive',
            'Content-Length':'131',
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie':'BDUSS=ZEeENCYklUblBWUE1QdmRjTlc5UEtkWFNwbHh4SkJHcTNKS0JVRkM4fkhENU5rSVFBQUFBJCQAAAAAAAAAAAEAAABQJKVrTWlyTWFydmVsAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMeCa2THgmtkdX; BDUSS_BFESS=ZEeENCYklUblBWUE1QdmRjTlc5UEtkWFNwbHh4SkJHcTNKS0JVRkM4fkhENU5rSVFBQUFBJCQAAAAAAAAAAAEAAABQJKVrTWlyTWFydmVsAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMeCa2THgmtkdX; BAIDUID=5714F83FD829786045ACF99AB80ED0BF:FG=1; newlogin=1; PSTM=1697886916; BIDUPSID=A25F3A688D747FD6EC75B988ECB88075; BAIDUID_BFESS=5714F83FD829786045ACF99AB80ED0BF:FG=1; APPGUIDE_10_6_6=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; ZFY=9ZUDnOsfneRPNnmV6VwT5YD3tCX8olUQce27S87g08I:C; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1697902389,1697941204,1697969462,1698228865; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1698228881; ab_sr=1.0.1_MzBiYmU3ZTFiZDIwMjVkYjU4OTllZjQ0ZjZhYzFjZTFmOGZiOGQ2NzAxNGI3YWVhNTA4YzNkNjRiYTg4ZGFjNTY5YTUwYjk0YmViYWM3ODhkOWYwMTUzMThhMmYwNmYwNjIyMTkzMjdjNjQ1NWY1YTRiYzJkNGMzYjgxNzcxNTAxMDNhNzUyZjEwYTg3NzJkYmYzZDJiNmZiYzU4NmYyZGJiNWFjZmEwNDU4ZGU0ZTc4MWM2ZGI2M2MwY2YyODE5',
            'Host':'fanyi.baidu.com',
            'Origin':'https://fanyi.baidu.com',
            'Referer':'https://fanyi.baidu.com/',
            'Sec-Ch-Ua':'"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
            'Sec-Ch-Ua-Mobile':'?0',
            'Sec-Ch-Ua-Platform':'"Windows"',
            'Sec-Fetch-Dest':'empty',
            'Sec-Fetch-Mode':'cors',
            'Sec-Fetch-Site':'same-origin',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61',
            'X-Requested-With':'XMLHttpRequest'}

data = {'from':'en',
        'to':' zh',
        'query':' eye',
        'simple_means_flag':' 3',
        'sign':' 67056.386753',
        'token':' 56494c8d0601c8a893977fcd7eb1a4e9',
        'domain':' common',
        'ts':' 1698228881300'}

# url:请求地址  data: 请求参数  kwargs 字典
response = requests.post(url=url, data=data, headers=headers)

content = response.text

import json

obj = json.loads(content, encoding='utf-8')

print(obj)

# 总结
# (1) post请求 是不需要编解码
# (2) post 请求的参数是data
# (3) 不需要请求对象的定制