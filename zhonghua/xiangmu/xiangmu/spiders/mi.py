# -*- coding: utf-8 -*-
import scrapy
import re
import os
from scrapy_redis.spiders import RedisSpider
from xiangmu.items import DomeItem
class ZhongSpider(scrapy.Spider):
    name = 'mi'
    allowed_domains = ['chinahr.com']

    start_urls = ['http://www.chinahr.com/beijing/jobs/']

    def parse(self, response):


        a = response.xpath('//div[@class="ul-con"]/a/text()|//ul[@class="item-hot"]//a/text()').extract()

        with open('url.html','r') as f:
             html = f.read()
             url_id = re.compile(r'\d{3,4}')
             id =  url_id.findall(html)
        for i in id :
            start_url = 'http://www.chinahr.com/sou/?city=' + i
            for s in a :
                fulurl = start_url +'&keyword=' + s

                yield scrapy.Request(url=fulurl,callback=self.parse_list)

    def parse_list(self,response):
        shu = response.xpath('//div[@class="quickPage"]/span/text()').extract()
        if shu:
            shu = shu[0]
            u = re.compile(r'\d+')
            sh = u.findall(shu)[0]
            shs = sh.encode('utf-8')
            for i in range(1,int(shs)+1):
                fulurl = response.url +'&page=' + str(i)
                yield scrapy.Request(url=fulurl,callback=self.parse_liaaaaa)


    def parse_liaaaaa(self,response):

        url = response.xpath('//div[@class="jobList"]/@data-url').extract()
        for i in url:
            print i