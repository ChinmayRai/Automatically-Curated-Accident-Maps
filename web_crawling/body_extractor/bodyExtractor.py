import scrapy
import json

class BodyExtractor(scrapy.Spider):
    name = "bodyExtractor"

    file_object = open(r"input.json","r")
    input = file_object.read()
    j = json.loads(input)
    file_object.close()

    urls = j[0]['urls']

    # start_urls = [
    #     'http://epaperbeta.timesofindia.com//Article.aspx?eid=31805&articlexml=Three-bikers-who-chased-lions-nabbed-10112017005029',
    # ]

    start_urls = urls

    def parse(self, response):
        title = response.xpath('//div[@class="main-content"]/section/h1/arttitle/text()').extract_first()
        lines = response.xpath('//div[@class="Normal"]/text()').extract()
    

        yield {
        'title' : title,
        'lines':  lines,
    }

    # def parse(self, response):
    #         title = response.xpath('//div[@id="divTitle"]/text()').extract_first()
    #         location = response.xpath('//div[@id="artLocation"]/div/text()').extract_first()
    #         source = response.xpath('//div[@id="artSource"]/div/text()').extract_first()
    #         top_line = response.xpath('//div[@id="divArticleContent"]/text()').extract_first()
    #         lines = response.xpath('//div[@id="divArticleContent"]/p/text()').extract()
        

    #         yield {
    #         'title' : title,
    #         'location' : location,
    #         'source' : source,
    #         'top-line':  top_line,
    #         'lines':  lines,
    #     }

    # def parse(self, response):
    #         yield {
    #         'title' : response.xpath('//div[@id="divTitle"]/text()').extract_first(),
    #         'location' : response.xpath('//div[@id="artLocation"]/div/text()').extract_first(),
    #         'source' : response.xpath('//div[@id="artSource"]/div/text()').extract_first(),
    #         'top-line':  response.xpath('//div[@id="divArticleContent"]/text()').extract_first(),
    #         'lines':  response.xpath('//div[@id="divArticleContent"]/p/text()').extract(),
    #     }