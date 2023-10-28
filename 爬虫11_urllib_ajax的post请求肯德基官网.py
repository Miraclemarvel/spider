# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# post

# 第二页
# cname: 武汉
# pid:
# pageIndex: 1
# pageSize: 10

# 第二页
# cname: 武汉
# pid:
# pageIndex: 2
# pageSize: 10

import urllib.request
import urllib.parse


def create_request(page):
    base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

    data = {'cname': '武汉',
            'pid': '',
            'pageIndex': page,
            'pageSize': '10'}

    data = urllib.parse.urlencode(data).encode('utf-8')

    headers = {'User-Agent':
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61'}

    request = urllib.request.Request(base_url, data, headers)

    return request

def get_content(request):
    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    return content

def down_load(content, page):
    with open('KFC_' + str(page) + '.json', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    start_page = int(input('请输入起始页码: '))
    end_page = int(input('请输入结束页码: '))

    for page in range(start_page, end_page + 1):
        # 请求对象的创建
        request = create_request(page)
        # 获取网页源码
        content = get_content(request)
        # 下载
        down_load(content, page)