import scrapy

class QuotesSpider(scrapy.Spider):
    name = "headings"

    start_urls = [
        'https://timesofindia.indiatimes.com/2018/5/26/archivelist/year-2018,month-5,starttime-43246.cms',
    ]

    def parse(self, response):
            title = response.xpath('//td[@width="49%"]/span/a/text()').extract()
            url = response.xpath('//td[@width="49%"]/span/a/@href').extract()
            # title = response.xpath('//td[@align="left"]/span/a/text()').extract()
            # location = response.xpath('//div[@id="artLocation"]/div/text()').extract_first()
            # source = response.xpath('//div[@id="artSource"]/div/text()').extract_first()
            # top_line = response.xpath('//div[@id="divArticleContent"]/text()').extract_first()
            # lines = response.xpath('//div[@id="divArticleContent"]/p/text()').extract()
        
            yield {
            'title' : title,
            'url' : url
            }

            # yield {
            # 'title' : title,
            # 'location' : location,
            # 'source' : source,
            # 'top-line':  top_line,
            # 'lines':  lines,
        # }

    # def parse(self, response):
    #         yield {
    #         'title' : response.xpath('//div[@id="divTitle"]/text()').extract_first(),
    #         'location' : response.xpath('//div[@id="artLocation"]/div/text()').extract_first(),
    #         'source' : response.xpath('//div[@id="artSource"]/div/text()').extract_first(),
    #         'top-line':  response.xpath('//div[@id="divArticleContent"]/text()').extract_first(),
    #         'lines':  response.xpath('//div[@id="divArticleContent"]/p/text()').extract(),
    #     }