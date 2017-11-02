# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiangmuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class DomeItem(scrapy.Item):
    zhiwei = scrapy.Field()
    mani = scrapy.Field()
    biyao = scrapy.Field()
    yaoqiu = scrapy.Field()
    didian = scrapy.Field()
    gongsi = scrapy.Field()