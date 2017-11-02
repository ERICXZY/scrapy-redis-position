# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy_redis.spiders import RedisSpider
from lieping.spiders.ctity import c_list


class LiepinSpider(RedisSpider):
    name = 'liepin'
    allowed_domains = ['www.liepin.com']
    base_url = 'http://www.liepin.com'
    #start_urls = ["https://www.liepin.com/job/197277500.shtml"]
    redis_key = 'liepin:start_urls'

    #职位总页面
    def parse(self, response):
        zhaopin_url = response.xpath('//li[@data-name="job"]/a/@href').extract()[0]
        print zhaopin_url

        yield scrapy.Request(zhaopin_url,callback=self.parse_industry)

    #行业分类
    def parse_industry(self,response):
        industry_list= response.xpath('//dd[@class="short-dd select-industry"]//a/@href')
        #print len(industry_list)
        for industry in industry_list:
            yield scrapy.Request(self.base_url+industry.extract(),callback=self.parse_salary)

    #每个行业的工资分类
    def parse_salary(self,response):
        salary_list = response.xpath('//dd[@data-param="salary"]/a/@href')
        for salary in salary_list:
            yield scrapy.Request(self.base_url+salary.extract(),callback=self.parse_location)

    #地点分区
    def parse_location(self,response):
        for i in c_list():
            yield scrapy.Request(response.url + "&" + "dqs=" + str(i),callback=self.parse_page)

    #分页
    def parse_page(self,response):
        lastpage_url = response.xpath('//div[@class="pagerbar"]/a[@class="last"]/@href | //div[@class="pagerbar"]/a[@class="last disabled"]/@href').extract()[0].encode("utf-8")
        if lastpage_url == "javascript:;":
            yield scrapy.Request(response.url,callback=self.parse_page)
        else:
            pattern = re.compile(r'curPage=(\d+)')
            res = pattern.search(lastpage_url)
            if res is not None:
                r = res.group(1)
                for i in range(1,int(r)+1):
                    ret = re.split(r'curPage=\d+', lastpage_url)
                    str = "".join(ret)
                    str += "curPage=%s" % i
                    str = self.base_url + str
                    yield scrapy.Request(str,callback=self.parse_list)

    #每页提取详情链接
    def parse_list(self,response):
        pos_list = response.xpath('//ul[@class="sojob-list"]/li')
        for pos in pos_list:
            detail_url = pos.xpath('.//div[@class="job-info"]/h3/a/@href').extract()[0]
            if len(detail_url) < 20:
                detail_url = self.base_url + detail_url
            #print detail_url
            yield scrapy.Request(detail_url,callback=self.parse_item,priority=1)

    #进入详情进行数据提取
    def parse_item(self,response):
        #职位名称
        pos_name = response.xpath('//div[@class="about-position "]//h1/text() | //div[@class="job-title"]//h1/text() | //div[@class="about-position"]//h1/text()').extract_first()
        #公司名称
        company = response.xpath('//div[@class="about-position "]//h3/a/text() | //div[@class="title-info "]//h3/text() | //div[@class="job-main-title"]/strong/text()').extract_first()
        if company is not None:
            company = company.strip("\n \t")
        else:
            company = ""
        #工资
        salary = response.xpath('//div[@class="job-item"]//p[@class="job-item-title"]/text() | //p[@class="job-main-title"]/text() | //div[@class="job-main-title"]/strong/text()').extract_first().strip("\r\n ")
        #地点
        location = response.xpath('//p[@class="basic-infor"]/span/a/text() | //p[@class="basic-infor"]/span/text() | //p[@class="job-main-tip"]/span[1]/text()').extract()
        if len(location) == 1:
            location=location[0].strip("\r\n\t ")
        elif len(location) == 2:
            location = location[1].strip("\r\n\t ")
        else:
            location = location[2].strip("\r\n\t ")
        #职位描述
        pos_desc = response.xpath('//div[@class="content content-word"]/text()').extract()
        pos_desc = "".join(pos_desc).strip(" \r\n")

        #发布时间
        pub_date = response.xpath('//time/@title | //p[@class="basic-infor"]/span[2]/text()[2]').extract_first()

        #教育背景
        edu_bg = response.xpath('//div[@class="job-qualifications"]/span[1]/text() | //div[@class="resume clearfix"]/span[1]/text()').extract_first()

        #工作经验
        experience = response.xpath('//div[@class="job-qualifications"]/span[2]/text() | //div[@class="resume clearfix"]/span[1]/text()').extract_first()

        item = {
            #详情页的url
            "detail_url":response.url,
            "pos_name":pos_name,
            "company":company,
            "salary":salary,
            "location":location,
            "pos_desc":pos_desc,
            "pub_date":pub_date,
            "edu_bg":edu_bg,
            "experience":experience,
        }
        #print item
        yield item







