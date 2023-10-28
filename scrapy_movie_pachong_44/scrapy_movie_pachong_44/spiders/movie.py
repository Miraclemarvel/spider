import scrapy
from ..items import ScrapyMoviePachong44Item


class MovieSpider(scrapy.Spider):
    name = "movie"
    allowed_domains = ["www.dytt.to"]
    start_urls = ["https://www.dytt.to/index.htm"]

    def parse(self, response):
        # 要第一页的名字和第二面的图片

        a_list = response.xpath('//td[@class="inddline"]/a[2]')
        # //td[@class="inddline"]/a[2]/text()
        for a in a_list:
            href = a.xpath('./@href').extract_first()
            name = a.xpath('./text()').extract_first()

            # 第二页的地址是
            url = 'https://www.dytt.to/' + href

            # 对第二页的;链接发起访问
            yield scrapy.Request(url=url, callback=self.parse_second, meta={'name': name})


    def parse_second(self, response):
        # 注意: 如果拿不到数据的情况下,  一定要检查你的xpath语法是否正确
        src = response.xpath('//div[@id="Zoom"]//img/@src').extract_first()
        name = response.meta['name']

        movie = ScrapyMoviePachong44Item(src=src,name=name)

        yield movie



