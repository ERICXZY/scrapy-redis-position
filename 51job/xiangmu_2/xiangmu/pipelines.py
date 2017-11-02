# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import MySQLdb
import hashlib



#这是加密
def getMd5(data):
    m = hashlib.md5()
    m.update(data)
    return m.hexdigest()


class XiangmuPipeline(object):
    def process_item(self, item, spider):
        return item




from datetime import datetime

class JobPipeline(object):
    def process_item(self, item, spider):
        item["crawled"] = datetime.utcnow() # 获取当前utc时间
        item["spider"] = spider.name # 爬虫名称
        return item






#写入json文件
# class Five1Pipeline(object):
#     def __init__(self):
#         self.f = open('Five51job.json','a')
#     def process_item(self,item,spider):
#         self.f.write(json.dumps(dict(item),ensure_ascii=False).encode('utf-8')+'\n')
#         return item
#     def close_spider(self,spider):
#         self.f.close()
#
#
#
# #链接mysql
# class list_ipPipeline(object):
#     #初始化
#     def __init__(self):         #connect()链接的意思
#         try:
#             self.conn = MySQLdb.connect('192.168.2.190','cjl','123456','mypython',charset='utf8')
#             self.cursor = self.conn.cursor()    #cursor()指针的意思
#         except Exception,e:
#             print "链接失败"
#             print str(e)
#     def process_item(self,item,spider):
#         print dict(item)
#         sql = 'insert into 51job(spider,detail_url,pos_name,salary,pub_date,edu_bg,experience,location,company,pos_desc)'\
#         'values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
#         try:            #execute()执行的意思
#             self.cursor.execute(sql,(item['spider'],item['detail_url'],item['pos_name'],item['salary'],item['pub_date'],item['edu_bg'],item['experience'],item['location'],item['company'],item['pos_desc'],item['crawled'],))
#             self.conn.commit()          #commit()提交的意思
#         except Exception,e:
#             print "插入失败",str(e)
#         return item
#
#     def close_spider(self):
#         self.cursor.close()
#         self.conn.close()
#
#




