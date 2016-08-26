from scrapy import Spider
from scrapy.selector import Selector
from stack.items import StackItem


class StackSpider(Spider):
    #defines the name of the spider
    name = "stack"
 
    #contains the base url for the allowed domains for the spider to crawl
    allowed_domains = ["stackoverflow.com"]

    #is a list of url's for the spider to start crawling from.
    start_urls = [
            "http://stackoverflow.com/questions?pagesize=50&sort=newest"
            ]

    def parse(self, response):
        questions  = Selector(response).xpath('//div[@class="summary"]/h3')

        for question in questions:
            item = StackItem()
            item['title'] = question.xpath(
                    'a[@class = "question-hyperlink"]/text()').extract()[0]
            item['url'] = question.xpath(
                    'a[@class = "question-hyperlink"]/@href').extract()[0]
            yield item
                    
