
import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

#第二个反爬 cookie反爬
headers = {'Accept':'*/*',
        #'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Acs-Token':'1697942113389_1697942113417_1cp7ED6KiK1qX1VpD2UIkkiXag2V1i6NgOGwCbpcaO6oSJ/vGn4F2WZgvL//c+tANBZNPCfkBPi6Ol/OlI1YPZL4di+7EijRN9rf4w3kDMonMnLZ8a7lQe3hKaikN2djHrMlqZj5CdHtmBYt+dR9VczO1hR0eFePMPQbhdzMLkKc2gwGA8i6yNvAyy8qU9EbCZ3gDbYwKksWjztBOU8T/O/7itqEnYiyQ/sWUUp4CfcC2XNVnAwLZzQNCCmqtU6uj/KQ4qAPXFIUmVMmwNgizl7sTlUgUZ8fP0+HS1UsFg9quZLQuyd0ADhkNfRDktVOhU3CLaSKyoJuIyqrYiZ2Fc8Vd3KpN8KgARXiJmqTq+BqmMW5NkNbcuoMBGfexnLZw8r+i4u9ClpdQV4sYBO/tgf6VFE7AiORxPSwKGkmviBi+nvN6bBrvWTfFDZdoizaqKd1JrXJettz91pq+NgdYBR+0wsADqa9246alc06NavHHL49ZPn26wIuoR44UFNlUuRT5a118Jd6kD0/sNrk/w==',
        'Connection':'keep-alive',
        'Content-Length':'133',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie':'BDUSS=ZEeENCYklUblBWUE1QdmRjTlc5UEtkWFNwbHh4SkJHcTNKS0JVRkM4fkhENU5rSVFBQUFBJCQAAAAAAAAAAAEAAABQJKVrTWlyTWFydmVsAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMeCa2THgmtkdX; BDUSS_BFESS=ZEeENCYklUblBWUE1QdmRjTlc5UEtkWFNwbHh4SkJHcTNKS0JVRkM4fkhENU5rSVFBQUFBJCQAAAAAAAAAAAEAAABQJKVrTWlyTWFydmVsAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMeCa2THgmtkdX; BAIDUID=5714F83FD829786045ACF99AB80ED0BF:FG=1; newlogin=1; PSTM=1697886916; BIDUPSID=A25F3A688D747FD6EC75B988ECB88075; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=5714F83FD829786045ACF99AB80ED0BF:FG=1; APPGUIDE_10_6_6=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1697899900,1697902389,1697941204; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1697942113; ab_sr=1.0.1_MjJlZjNiOWJhZTczYjFjYjMyZmYxMGIxMDYyZDNmMThmYzJiN2MyYzExZDBlZjQwYWM2YTA5NDE2YzMzOWMzMGZkNzEzNmE2OWUyODQ2NzhlYjQ1NDVhNGQ2N2Y1MDhlNzc0NTdjM2Q1NjllYmM4NDhmMzk5OWNhMzFmNzUzZjM4M2VkNWU1NWE4NjkyMjI0MDljMWY5OTliZTEzYjRhZWQyYWYzOWNmM2YyOTIzZThmYTZlNTBkMGQ0N2YxY2U2',
        'Host':'fanyi.baidu.com',
        'Origin':'https://fanyi.baidu.com',
        'Referer':'https://fanyi.baidu.com/',
        'Sec-Ch-Ua':'"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
        'Sec-Ch-Ua-Mobile':'        ?0',
        'Sec-Ch-Ua-Platform':'        "Windows"',
        'Sec-Fetch-Dest':'        empty',
        'Sec-Fetch-Mode':'        cors',
        'Sec-Fetch-Site':'        same-origin',
        'User-Agent':'        Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.57',
        'X-Requested-With':'XMLHttpRequest'}

data = {'from': 'en',
        'to': 'zh',
        'query': 'love',
        'simple_means_flag': '3',
        'sign': '198772.518981', #sign的含义是什么你知道吗 我直接复制的整段
        'token': '56494c8d0601c8a893977fcd7eb1a4e9',
        'domain': 'common',
        'ts': '1697942113375'}

#post请求的参数 必须进行编码 并且要调用encode方法
data = urllib.parse.urlencode(data).encode('utf-8')

#请求对象的定制
request = urllib.request.Request(url, data, headers)

#模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

#获取响应的数据
content = response.read().decode('utf-8')

# print(content)

#反序列化
import json
obj = json.loads(content)
print(obj)