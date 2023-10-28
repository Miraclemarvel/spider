import urllib.request
import urllib.error

url = 'https://blog.csdn.net/weixin_61370021/article/details/127777393'
# HTTPerror: 一般为域名错误
# url = 'https://blog.csdn.net/weixin_61370021/article/details/1277773931'
# URLerror: 一般为主机地址和参数有问题
# url = 'http://www.goudan1111.com'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61'}

try:
    request = urllib.request.Request(url=url, headers=headers)

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    print(content)
except urllib.error.HTTPError:
    print('系统正在升级...')
except urllib.error.URLError:
    print('我都说了系统正在升级')