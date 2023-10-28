import urllib.request
import json
import jsonpath

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1698051278939_188&jsoncallback=jsonp189&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

#带冒号:的请求头一般不好使
headers = {#':authority':'dianying.taobao.com',
           # ':method':'GET',
           # ':path':'/cityAction.json?activityId&_ksTS=1698051278939_188&jsoncallback=jsonp189&action=cityAction&n_s=new&event_submit_doGetAllRegion=true',
           # ':scheme':'https',
            'Accept':'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
           # 'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Bx-V':'2.5.3',
            'Cookie':'t=942f2eb5694f85a62fd2e828cee28941; cookie2=1adb93a55f4b30fdf28aa35032178782; v=0; _tb_token_=eb4d555485e06; cna=8hW9HefPsygCAatx3RYz9pPw; xlly_s=1; tb_city=110100; tb_cityName="sbG+qQ=="; tfstk=duJWvubg8z4WDR1LUYi2lzmO6iXIbUMZVkspjHezvTBRAvTeuu-yYLRfve8mx0XyvwTBuZxPT2muvITkX_8Bx0jdJeLC8QlqQ3xlK93NRAkwqOj0jHMxgeFWy86K7VkagoCoz9dz9wKGjcl__2GXq2eYhR8E5fJtHELyhg1xg3QvMCmFq_g6xZ2KWIWaqR76QsFQc12CcNojcWV3RIj0q; l=fBMSGzelPM6Tsx0FBO5aourza77O3CdbzsPzaNbMiIEGa6QPth-uyOCtzjPDSdtjgT5XVetPw3HW8dh9rJaLRAsWHpfk_OEyAtvDReM3N7AN.; isg=BIeH6SnEriiRXiqkblZBoiITFjtRjFtuTADdP1lxA5c3yKWKYVmcvn7GaoiWIDPm',
            'Referer':'https://dianying.taobao.com/index.htm',
            'Sec-Ch-Ua':'"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
            'Sec-Ch-Ua-Mobile':'?0',
            'Sec-Ch-Ua-Platform':'"Windows"',
            'Sec-Fetch-Dest':'empty',
            'Sec-Fetch-Mode':'cors',
            'Sec-Fetch-Site':'same-origin',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61',
            'X-Requested-With':'XMLHttpRequest'}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

content = content.split('(')[1].split(')')[0]

with open("爬虫22_解析_jsonpath解析淘票票.json", 'w', encoding='utf-8') as f:
    f.write(content)

obj = json.load(open("爬虫22_解析_jsonpath解析淘票票.json", encoding='utf-8'))

region_list = jsonpath.jsonpath(obj, "$..regionName")

with open('city.txt', 'w', encoding='utf-8') as f:
    for region in region_list:
        f.write(region + '\n')
