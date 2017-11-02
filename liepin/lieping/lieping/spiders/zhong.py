# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
import time

class ZhongSpider(scrapy.Spider):
    name = 'zhong'
    allowed_domains = ['chinahr.com']
    start_urls = ['http://www.chinahr.com/']

    # rules = (
    #     Rule(LinkExtractor(allow=r'http://www.chinahr.com/.*?/jobs/\.*?/'), callback='parse_item', follow=True),
    # )

    def parse(self, response):

        url_list =  response.xpath('//div[@class="sideMain hide"]//a/@href | //div[@class="sideMen"]//a/@href').extract()
        for url in url_list:


            yield scrapy.Request(url=url,callback=self.parse_list)
    def parse_list(self,response):
        print response.url



        shu = response.xpath('//div[@class="quickPage"]/span/text()').extract()[0]
        u = re.compile(r'\d+')
        sh = u.findall(shu)[0]
        shs = sh.encode('utf-8')

        url_index = response.url +'%d/'
        base_list = range(1,int(shs))
        for i in base_list:
            fulurl = url_index % i

            yield scrapy.Request(url = fulurl,callback=self.parse_index)
    def parse_index(self,response):

        url_detail = response.xpath('//div[@class="jobList"]/@data-url').extract()
        for a in url_detail:

            yield scrapy.Request(url=a,callback=self.parse_detail)
    def parse_detail(self,response):
        # print response.body
        print response.xpath('//div[@class="base_info"]//h1/span/text()').extract()
        # print response.xpath('//div[@class="job_require"]/span[1]/text()').extract()
        # print response.xpath('//div[@class="job_require"]/span[2]/text()').extract()
        # print response.xpath('//div[@class="job_require"]/span[5]/text()').extract()
