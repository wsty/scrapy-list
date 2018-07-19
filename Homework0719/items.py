# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Homework0719Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    thumb_url = scrapy.Field()
    date = scrapy.Field()
    title = scrapy.Field()
    tag = scrapy.Field()
    summary = scrapy.Field()
    detail_url = scrapy.Field()

