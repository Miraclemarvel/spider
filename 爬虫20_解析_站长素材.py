

# (1)请求对象的定制
# (2)获取网页的源码
# (3)下载

# 需求: 下载前十页的图片
#第一页: url = 'https://sc.chinaz.com/tupian/dongman.html'
#第二页: url = 'https://sc.chinaz.com/tupian/dongman_2.html'
#第三页: url = 'https://sc.chinaz.com/tupian/dongman_3.html'
#....第page页: url = 'https://sc.chinaz.com/tupian/dongman_page.html'

import urllib.request
def create_request(page):
    if(page==1):
        url = 'https://sc.chinaz.com/tupian/dongman.html'
    else:
        url = 'https://sc.chinaz.com/tupian/dongman_' + str(page) + '.html'

    headers = {'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61'}

    request = urllib.request.Request(url=url, headers=headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

from lxml import etree

def down_load(content, page):
    #下载图片 urllib.request.urlretrieve('图片地址', '文件的名字')
    tree = etree.HTML(content)

    name_list = tree.xpath("//div[@class='bot-div']//a/@title")
    # 一般涉及图片的网站一般都会涉及懒加载
    src_list = tree.xpath("//div[@class='item']//img/@data-original")

    #print(len(name_list), len(src_list))
    for i in range(len(name_list)):
        name = name_list[i]
        src = src_list[i]
        url = 'https:' + src

        urllib.request.urlretrieve(url, './Img01/'+ name +'.jpg')



if __name__ == '__main__':
    start_page = int(input('请输入起始页码: '))
    end_page = int(input('请输入结束页码: '))

    for page in range(start_page, end_page + 1):
        # 请求对象的定制
        request = create_request(page)
        # 获取网页的源码
        content = get_content(request)
        # 下载
        down_load(content, page)

