import scrapy
from scrapy import Spider
from crawler import ParseConfig


class GPU(scrapy.Spider):
    name = "CPUcrawl";
    allowed_domains = ["tweakers.net"]
    start_urls = ["http://tweakers.net/pricewatch/394885/intel-core-i7-4790k-boxed/specificaties/"]

    def parse(self, response):
        p = ParseConfig.ParseConfig()
        listCrawl = p.getCrawlList("crawler/crawl-conf/CPU.conf")
        print "SECTIONS FOUND: " + str(p.sumSection())
        for x in listCrawl:

            key = response.xpath(p.getKeyxPath(x, "crawler/crawl-conf/CPU.conf") % x).extract()
            value= response.xpath(p.getValuexPath(x, "crawler/crawl-conf/CPU.conf") % x ).extract()
            print "ROW",x, key, value