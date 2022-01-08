import scrapy
from ..items import TedItem


class TedSpider(scrapy.Spider):
    name = 'ted'
    #start_urls = ['https://www.ted.com/talks']
    start_urls = ['https://select.pdgzf.com/villageLists']

    def parse(self, response):
        results = response.xpath('//*[@id="app"]/div[2]/div/div[2]/ul/li[@class="clearfix rel"]')
        print(results)
        for element in results:
            print(element)
            # item = TedItem()
            # item['talk'] = element.xpath('./div/div/div/div[2]/h4[2]/a/text()').extract_first()
            # item['link'] = element.xpath('./div/div/div/div[2]/h4[2]/a/@href').extract_first()
            # yield item