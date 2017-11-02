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
#CrawlSpider Item
class Five1JobItem(scrapy.Item):
    zhiwei = scrapy.Field()
    gs_weizhi = scrapy.Field()
    gs_name = scrapy.Field()
    money = scrapy.Field()
    zhiwei_xinxi = scrapy.Field()

#scrapySpider Item
class Five1Item(scrapy.Item):
    spider = scrapy.Field()    #爬虫名称
    detail_url = scrapy.Field()  #详情页的链接           #职位详情链接
    pos_name = scrapy.Field()   #公司的职位             #职位名称
    salary = scrapy.Field()    #薪资                   #工资
    pub_date = scrapy.Field()     #发布时间               #发布时间
    edu_bg = scrapy.Field()                              #教育背景
    experience = scrapy.Field()                          #工作经验
    location = scrapy.Field()   #公司地点               #工作地点
    company = scrapy.Field()     #公司的名字             #公司名称
    pos_desc = scrapy.Field()       #职位描述               #职位描述
    crawled = scrapy.Field()                             #爬取时间


