import scrapy

class QuotesSpider(scrapy.Spider):
    name = "news"

    start_urls = [
        'https://timesofindia.indiatimes.com/2018/5/26/archivelist/year-2018,month-5,starttime-43246.cms',
    ]

    def parse(self, response):
            title = response.xpath('//td[@width="49%"]/span/a/text()').extract()
            url = response.xpath('//td[@width="49%"]/span/a/@href').extract()
        
            yield {
            'title' : title,
            'url' : url
            }