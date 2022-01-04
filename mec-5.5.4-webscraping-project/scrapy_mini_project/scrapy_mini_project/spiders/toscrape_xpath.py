# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "toscrape_xpath"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.xpath(".//div[@class='quote']"):
            yield {
                'text': quote.xpath(".//span[@class='text']/text()").extract(),
                'author': quote.xpath(".//small[@class='author']/text()").extract(),
                'tags': quote.xpath(".//a[@class='tag']/text()").extract(),
            }

        next_page = response.xpath("//li[@class='next']/a/@href").get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
            
