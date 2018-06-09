import scrapy

class TestClass(scrapy.Spider):
    name = "test"

    start_urls = ['https://timesofindia.indiatimes.com/']

# 2018/5/26/archivelist/year-2018,month-5,starttime-43246.cms

    def parse(self, response):
            title = response.xpath('//td[@width="49%"]/span/a/text()').extract_first()
            url = response.xpath('//td[@width="49%"]/span/a/@href').extract_first()
        
            yield {
            'title' : title,
            'url' : url
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