import scrapy
from ..items import AmazonreviewItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    start_urls = ['https://www.amazon.in/TATASKY-Set-Month-Dhamaal-Free/product-reviews/B00HT06T54']

    def parse(self, response):
        items = AmazonreviewItem()
        reviews= response.css('.a-text-bold span::text').extract()
        items['reviews'] = reviews
        yield items

        next_page = response.xpath('//a[text() = "Next page"]/@href').get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page)) 