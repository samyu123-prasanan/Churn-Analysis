# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonreviewItem(scrapy.Item):
    # define the fields for your item here like:
     reviews = scrapy.Field()
     pass


