# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings
from datetime import datetime

class XiangmuPipeline(object):
    def process_item(self, item, spider):
        return item



class ExamplePipeline(object):
    def process_item(self, item, spider):
        item["crawled"] = datetime.utcnow() # 获取当前utc时间
        item['spider'] = spider.name # 爬虫名称
        return item


# 输入Mogondb
class MongodbPipeLine(object):

    def __init__(self):
        self.databases = pymongo.MongoClient(host=settings['HOST'],port=settings['PORT'])

    def process_item(self, item,spider):
        mongodb = self.databases[settings['DB']]
        mongodb.proxy.insert(dict(item))
        return item



