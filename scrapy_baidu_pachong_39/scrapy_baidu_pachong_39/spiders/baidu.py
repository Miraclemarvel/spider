import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫的名字 用于运行爬虫的时候 使用的值
    name = "baidu"
    # 允许访问的域名
    allowed_domains = ["www.baidu.com"]
    # 起始的url地址 指的是第一次访问的域名
    start_urls = ["http://www.baidu.com/"]

    # 是执行了start_urls之后 执行的方法  方法中的response 就是返回的那个对象
    # 相当于 response = urllib.request.urlopen() or resposne = requests.get()
    def parse(self, response):
        print('苍茫的天涯是我的爱')
        pass
