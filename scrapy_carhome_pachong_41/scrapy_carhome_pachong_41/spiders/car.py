import scrapy


class CarSpider(scrapy.Spider):
    name = "car"
    allowed_domains = ["car.autohome.com.cn"]
    # 注意如果请求的接口是html结尾的 那么不需要加/的
    start_urls = ["https://car.autohome.com.cn/price/brand-15.html"]

    def parse(self, response):
        print("===============================")
        name_list = response.xpath('//div[@class="main-title"]/a/text()')
        price_list = response.xpath('//span[@class="lever-price red"]/span/text()')
        img_list = response.xpath('//div[@class="list-cont-img"]/a/img/@src')
        for i in range(len(name_list)):
            name = name_list[i].extract()
            price = price_list[i].extract()
            img_url = 'https:' + img_list[i].extract()
            print(name, price, img_url)