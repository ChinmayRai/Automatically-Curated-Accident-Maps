import scrapy

class QuotesSpider(scrapy.Spider):
    name = "news"

    start_urls = [
        'http://epaperbeta.timesofindia.com//Article.aspx?eid=31805&articlexml=Three-bikers-who-chased-lions-nabbed-10112017005029',
    ]

    def parse(self, response):
            title = response.xpath('//div[@id="divTitle"]/text()').extract_first()
            location = response.xpath('//div[@id="artLocation"]/div/text()').extract_first()
            source = response.xpath('//div[@id="artSource"]/div/text()').extract_first()
            top_line = response.xpath('//div[@id="divArticleContent"]/text()').extract_first()
            lines = response.xpath('//div[@id="divArticleContent"]/p/text()').extract()
        

            yield {
            'title' : title,
            'location' : location,
            'source' : source,
            'top-line':  top_line,
            'lines':  lines,
        }

    # def parse(self, response):
    #         yield {
    #         'title' : response.xpath('//div[@id="divTitle"]/text()').extract_first(),
    #         'location' : response.xpath('//div[@id="artLocation"]/div/text()').extract_first(),
    #         'source' : response.xpath('//div[@id="artSource"]/div/text()').extract_first(),
    #         'top-line':  response.xpath('//div[@id="divArticleContent"]/text()').extract_first(),
    #         'lines':  response.xpath('//div[@id="divArticleContent"]/p/text()').extract(),
    #     }