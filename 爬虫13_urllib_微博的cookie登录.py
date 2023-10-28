# 适用场景: 数据收集的时候 需要绕过登录 然后进入到某个页面
# 个人信息页面是utf-8 但是还是报错了 因为没有进入个人信息页面 而是跳转到了登录页面

import urllib.request

url = 'https://weibo.com/u/5908403841'

headers = {':authority': 'weibo.com',
            ':method': 'GET',
            ':path': '/u/5908403841',
            ':scheme': 'https',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Cache-Control': 'max-age=0',
           #cookie携带着你的登录信息, 如果有登陆之后的cookie 那么就可以携带着cookie进入到任何页面
            'Cookie': 'XSRF-TOKEN=NN0_ts6EqTwLyLQwKE8gds6p; PC_TOKEN=6b58be5e91; login_sid_t=cde9319bb4f2b4780ddf52233a0afdd5; cross_origin_proto=SSL; WBStorage=4d96c54e|undefined; _s_tentry=weibo.com; Apache=3520242572023.122.1697953381407; SINAGLOBAL=3520242572023.122.1697953381407; ULV=1697953381409:4:1:1:3520242572023.122.1697953381407:1696045163905; wb_view_log=1549*8721.2395833730697632; SUB=_2A25IMMdXDeRhGeNH61oV8C3Ezz2IHXVrR7-frDV8PUNbmtANLWvFkW9NSssnAon8uiiDLv1hfxjmfrNVBOrLKDPN; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W56HIzlHOp8lG3XwsYDIGLC5JpX5KzhUgL.Fo-4ehnXeheRSh22dJLoIEBLxKqL1KnLB-qLxKMLB.2LB-qLxK-LBonL12eLxK-L1K5L1Kqt; ALF=1729489543; SSOLoginState=1697953543; WBPSESS=Uy53Ou98LAPqZalnDXIg6y8H3w9wrC4ZU69mPJ7F0TG2aNzSk0Hs5ZAybuOLyGRYiU5NBGE0hvzx9Ke1M8uqF2UEf9jHUysSrEWV7ywy4SjRfHoa8tFE-J5RnvTB_sq7aSM_4EA778FP8gW0raRzlQ==',
           #referer 判断当前路径是不是由上一个路径进来的
            'Referer': 'https://weibo.com/u/5908403841/info',
            'Sec-Ch-Ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61'}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

with open('weibo.html', 'w', encoding='utf-8') as f:
    f.write(content)