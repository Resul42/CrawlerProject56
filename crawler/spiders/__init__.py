# /home/j/workspace/Neo4j-octo-loveThis package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy

class GPUtest(scrapy.Spider):
    name = "GPUtest";
    allowed_domains = ["tweakers.net"]
    start_urls = ["http://tweakers.net/pricewatch/416125/msi-geforce-gtx-970-gaming-4g/specificaties/"]

def parse(self, response):
    '''
    :param response:
    :return:
    '''
    item = GPU()
    item['key'] = response.xpath("//*[@id='tab:specificaties']/table/tr[13]/td[1]/text()").extract()
    item['value'] = response.xpath("//*[@id='tab:specificaties']/table/tr[13]/td[2]/text()").extract()
    yield item

 
 
