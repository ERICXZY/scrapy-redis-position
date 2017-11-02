# -*- coding: utf-8 -*-
import scrapy
import re
import os
from scrapy_redis.spiders import RedisSpider
from xiangmu.items import DomeItem
class ZhongSpider(RedisSpider):
    name = 'tmps'
    allowed_domains = ['chinahr.com']
    redis_key = 'tmps:start_urls'


    def parse(self, response):

        start_url = 'http://www.chinahr.com/beijing/jobs/'
        yield scrapy.Request(url=start_url,callback=self.parse_mi)

    def parse_mi(self, response):
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
                yield scrapy.Request(url=fulurl,callback=self.parse_li,priority=1)


    def parse_li(self,response):
        url = response.xpath('//div[@class="jobList"]/@data-url').extract()

        if url :
            for i  in url:

                yield scrapy.Request(url=i,callback=self.parse_detail,priority=2)
    #
    def parse_detail(self,response):


        si =  response.xpath('//span[@class="p4LeImg fl"]/img/@src').extract()
        if si :
            pass
        else:
            item = {}

            detail_url = response.xpath('//div[@class="job-company jrpadding"]//h4/a/@href').extract()[0]
            pos_name =  response.xpath('//div[@class="base_info"]//h1/span[@class="job_name"]/text()').extract()[0]
            salary =  response.xpath('//div[@class="job_require"]/span[1]/text()').extract()[0]
            location =  response.xpath('//div[@class="job_require"]/span[2]/text()').extract()[0]
            edu_bg =  response.xpath('//div[@class="job_require"]/span[4]/text()').extract()[0]
            pos_desc =  response.xpath('//div[@class="job_intro_info"]/text()').extract()[0]
            company = response.xpath('//div[@class="job-company jrpadding"]/h4/a/text()').extract()[0]
            pub_date = response.xpath('//div[@class="job_profile jpadding"]/p/text()').extract()[0]
            experience = response.xpath('//div[@class="job_require"]/span[5]/text()').extract()[0]
            item['detail_url'] = detail_url
            item['pos_name'] = pos_name
            item['salary'] = salary
            item['location'] = location
            item['edu_bg'] = edu_bg
            item['company'] = company
            item['pos_desc'] = pos_desc
            item['pub_date'] =pub_date
            item['experience']=experience
            print item
            yield item
