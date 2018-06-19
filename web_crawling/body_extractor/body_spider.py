import scrapy
import json

class BodyExtractor(scrapy.Spider):
    name = "body_spider"

    # file_object = open(r"input.json","r")
    # input = file_object.read()
    # j = json.loads(input)
    # file_object.close()

    # start_urls = [
    #     'http://epaperbeta.timesofindia.com//Article.aspx?eid=31805&articlexml=Three-bikers-who-chased-lions-nabbed-10112017005029',
    # ]
    
    start_urls = [
        ''
    ]

    def parse(self, response):
        title = response.xpath('//div[@class="main-content"]/section/h1/arttitle/text()').extract_first()
        lines = response.xpath('//div[@class="Normal"]/text()').extract()
    
        yield {
        'title' : title,
        'lines':  lines,
    }


    def start_requests(self):
        # self points to the spider instance
        # that was initialized by the scrapy framework when starting a crawl
        #
        # spider instances are "augmented" with crawl arguments
        # available as instance attributes,
        # self.ip has the (string) value passed on the command line
        # with `-a ip=somevalue`
        for url in self.start_urls:
            yield scrapy.Request(url+self.ip, dont_filter=True)


# os.system('scrapy runspider sp.py -a ip="2018/5/26/archivelist/year-2018,month-5,starttime-43246.cms" -o a.json')

    # def closed( self, reason ):
    #     # will be called when the crawler process ends
    #     # any code 
    #     # do something with collected data 
    #     for i in self.spider_attr: 
    #         print i