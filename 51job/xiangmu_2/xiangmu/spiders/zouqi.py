# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from xiangmu.items import Five1JobItem
import json


class ZouqiSpider(CrawlSpider):
    name = 'zouqi'
    allowed_domains = ['51job.com']
    start_urls = ['http://www.51job.com']

    rules = (

        Rule(LinkExtractor(allow=r'search.51job.com/list/.*') ,follow=True),  #类型分类
        Rule(LinkExtractor(allow=r'http://jobs.51job.com/.*/\d+\.html'), callback='parse_item', follow=True),#列表页,能进详情页
        #Rule(LinkExtractor(allow=r'http://jobs.51job.com/.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        all = response.xpath('//div[@class="tCompany_center clearfix"]')
        for i in all:
            item = Five1JobItem()
            f = lambda x:x[0] if x else ''
            zhiwei = f(i.xpath('.//h1/text()')).extract()
            gs_weizhi = f(i.xpath('.//span[@class="lname"]/text()')).extract()
            gs_name = f(i.xpath('.//p[@class="cname"]/a/text()')).extract()
            money = i.xpath('.//div[@class="cn"]/strong/text()').extract()
            money = self.cheshi(money)
            zhiwei_xinxi = i.xpath('//div[@class="bmsg job_msg inbox"]/text()').extract()


            #把列表里所有的数据都变成字符串,strip并去空
            #data = ''.join(zhiwei_xinxi).strip()
            # print data
            item['zhiwei'] = zhiwei
            item['gs_weizhi'] = gs_weizhi
            item['gs_name'] = gs_name
            item['money'] = money
            item['zhiwei_xinxi'] = ''.join(zhiwei_xinxi).strip()
            yield item
    def cheshi(self,data):
        if data:
            data = data[0]
            return data
        else:
            data = ''
            return data















