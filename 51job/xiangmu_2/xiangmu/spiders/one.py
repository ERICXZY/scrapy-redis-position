# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
import json
from xiangmu.items import Five1Item
#from xiangmu.settings import city_list
import re
from scrapy_redis.spiders import RedisSpider
from xiangmu.tt import area_list

class OneSpider(RedisSpider):
    name = 'one'
    allowed_domains = ['51job.com']
    redis_key = 'xiangmu:start_urls'
    #start_urls = ['http://search.51job.com/jobsearch/search_result.php']

    headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
       # "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"zh-CN,zh;q=0.8",
        "Cache-Control":"max-age=0",
        "Connection":"keep-alive",
        "Cookie":"guid=15087609007718700098; slife=lastvisit%3D020000%26%7C%26; adv=adsnew%3D0%26%7C%26adsresume%3D1%26%7C%26adsfrom%3Dhttp%253A%252F%252Fbzclk.baidu.com%252Fadrc.php%253Ft%253D06KL00c00fZEOkb06TGp00uiAs0D98du00000j03Idb00000XRRNRM.THYdnyGEm6K85HRLnjbdnHRsg1FxUvNVgvwM0ZnquyR4njf3mWbsnj0sPyDzrfKd5RmkPWn4njDknHmvfWb1wDwaPWFawDDvf1ckrHFAPYf10ADqI1YhUyPGujY1njRzrHR1Pj0dFMKzUvwGujYkP6K-5y9YIZ0lQzqYTh7Wui3dnyGEmB4WUvYEIZF9mvR8TA9s5v7bTv4dUHYLrjbzn1nhmyGs5y7cRWKWwAqvHjPbnvw4Pj7PNLKvyybdphcznZufn-G4mWcsrN-VwMKpi7uLuyTq5iuo5HK-nHRzPjfzuj9Bm1bdnARdrHuBm1fvnH-WuWbsuhuB0APzm1YzPHn4n6%2526tpl%253Dtpl_10085_15730_11224%2526l%253D1500985392%2526attach%253Dlocation%25253D%252526linkName%25253D%252525E6%252525A0%25252587%252525E9%252525A2%25252598%252526linkText%25253D%252525E5%25252589%2525258D%252525E7%252525A8%2525258B%252525E6%25252597%252525A0%252525E5%252525BF%252525A7%252851Job%2529-%252525E6%25252589%252525BE%252525E5%252525B7%252525A5%252525E4%252525BD%2525259C%252525E5%252525B0%252525BD%252525E5%2525259C%252525A8%252525E5%25252589%2525258D%252525E7%252525A8%2525258B%252525E6%25252597%252525A0%252526xp%25253Did%2528%25252522m3bf209a9%25252522%2529%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FH2%2525255B1%2525255D%2525252FA%2525255B1%2525255D%252526linkType%25253D%252526checksum%25253D22%2526ie%253Dutf-8%2526f%253D8%2526tn%253D57095150_2_oem_dg%2526wd%253D51job%2526oq%253D51job%2526rqlang%253Dcn%26%7C%26adsnum%3D789233; search=jobarea%7E%60220200%7C%21ord_field%7E%600%7C%21recentSearch0%7E%601%A1%FB%A1%FA220200%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA05%A1%FB%A1%FA99%A1%FB%A1%FA04%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1508810260%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21recentSearch1%7E%601%A1%FB%A1%FA220200%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA33%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1508817260%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21recentSearch2%7E%601%A1%FB%A1%FA220200%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA03%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1508815186%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21recentSearch3%7E%601%A1%FB%A1%FA010000%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA05%A1%FB%A1%FA99%A1%FB%A1%FA04%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1508809644%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21recentSearch4%7E%601%A1%FB%A1%FA010000%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA05%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1508809639%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21collapse_expansion%7E%601%7C%21; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; NSC_tfbsdi.51kpc.dpn-159=ffffffffc3a01b3f45525d5f4f58455e445a4a423660",
        "Host":"search.51job.com",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",

    }
    # cookies = {
    #     "Cookie:guid":"15087609007718700098",
    #     "slife":"lastvisit%3D020000%26%7C%26",
    #     "adv":"adsnew%3D0%26%7C%26adsresume%3D1%26%7C%26adsfrom%3Dhttp%253A%252F%252Fbzclk.baidu.com%252Fadrc.php%253Ft%253D06KL00c00fZEOkb06TGp00uiAs0D98du00000j03Idb00000XRRNRM.THYdnyGEm6K85HRLnjbdnHRsg1FxUvNVgvwM0ZnquyR4njf3mWbsnj0sPyDzrfKd5RmkPWn4njDknHmvfWb1wDwaPWFawDDvf1ckrHFAPYf10ADqI1YhUyPGujY1njRzrHR1Pj0dFMKzUvwGujYkP6K-5y9YIZ0lQzqYTh7Wui3dnyGEmB4WUvYEIZF9mvR8TA9s5v7bTv4dUHYLrjbzn1nhmyGs5y7cRWKWwAqvHjPbnvw4Pj7PNLKvyybdphcznZufn-G4mWcsrN-VwMKpi7uLuyTq5iuo5HK-nHRzPjfzuj9Bm1bdnARdrHuBm1fvnH-WuWbsuhuB0APzm1YzPHn4n6%2526tpl%253Dtpl_10085_15730_11224%2526l%253D1500985392%2526attach%253Dlocation%25253D%252526linkName%25253D%252525E6%252525A0%25252587%252525E9%252525A2%25252598%252526linkText%25253D%252525E5%25252589%2525258D%252525E7%252525A8%2525258B%252525E6%25252597%252525A0%252525E5%252525BF%252525A7%252851Job%2529-%252525E6%25252589%252525BE%252525E5%252525B7%252525A5%252525E4%252525BD%2525259C%252525E5%252525B0%252525BD%252525E5%2525259C%252525A8%252525E5%25252589%2525258D%252525E7%252525A8%2525258B%252525E6%25252597%252525A0%252526xp%25253Did%2528%25252522m3bf209a9%25252522%2529%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FH2%2525255B1%2525255D%2525252FA%2525255B1%2525255D%252526linkType%25253D%252526checksum%25253D22%2526ie%253Dutf-8%2526f%253D8%2526tn%253D57095150_2_oem_dg%2526wd%253D51job%2526oq%253D51job%2526rqlang%253Dcn%26%7C%26adsnum%3D789233",
    #     "search":"jobarea%7E%60220200%7C%21ord_field%7E%600%7C%21recentSearch0%7E%601%A1%FB%A1%FA220200%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA05%A1%FB%A1%FA99%A1%FB%A1%FA04%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1508810260%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21recentSearch1%7E%601%A1%FB%A1%FA220200%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA33%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1508817260%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21recentSearch2%7E%601%A1%FB%A1%FA220200%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA03%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1508815186%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21recentSearch3%7E%601%A1%FB%A1%FA010000%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA05%A1%FB%A1%FA99%A1%FB%A1%FA04%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1508809644%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21recentSearch4%7E%601%A1%FB%A1%FA010000%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA05%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1508809639%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21collapse_expansion%7E%601%7C%21",
    #     "nsearch":"jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D",
    #     "NSC_tfbsdi.51kpc.dpn-159":"ffffffffc3a01b3f45525d5f4f58455e445a4a423660",
    # }

    # def start_requests(self):
    #     base_url = "http://www.51job.com"
    #     #cookies=self.cookies
    #     yield scrapy.Request(url=base_url,callback=self.list_parse,headers=self.headers)


    #启动爬虫而准备的
    def parse(self,response):
        base_url = "http://www.51job.com"
        #cookies=self.cookies
        yield scrapy.Request(url=base_url,callback=self.list_parse,headers=self.headers)

    #进入列表页
    def list_parse(self,response):
        url_list = response.xpath('//div[@class="nag"]//p[@class="nlink"]/a[2]/@href')[0].extract()
        yield scrapy.Request(url=url_list,callback=self.parse007,headers=self.headers)

    def parse007(self,response):
        # url_list = "http://search.51job.com/list/%s%s,000000,0000,00,9,99,%s,2,%s.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=%s&jobterm=99&companysize=99&lonlat=0%sC0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
        # list_url = url_list % ("city","252C00", "2B","page","edu","2")
        #每一个薪资
        list_salary = response.xpath('//div[@class="el mk"]/ul/li/a/@href').extract()[1:]
        for url in list_salary:
            yield scrapy.Request(url,callback=self.parse_edu)



    #获取每一条件页面的最大分页数,有12个,因为有12个条件.
    def parse_edu(self,response):
         xueli = response.xpath('//div[@id="filter_degreefrom"]//ul/li/a/@href').extract()[1:]
         for url in xueli:
             yield scrapy.Request(url,callback=self.parse_city)

    #city_list
    # url_list = "http://search.51job.com/list/%s%252C00,000000,0000,00,9,99,%s,2,%s.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=%s&jobterm=99&companysize=99&lonlat=0%sC0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    # list_url = url_list % ("city","252C00", "2B","page","edu","2")
    def parse_city(self,response):
        for city in area_list:
            res = re.sub(r'list/(\d+),','list/%s,' % city,response.url)
            yield scrapy.Request(res,callback=self.parse_page)


    #page_list
    def parse_page(self,response):

        #print response.url
        page_num = response.xpath('//div[@class="dw_page"]//span[@class="td"][1]/text()')[0].extract()
        gz = re.compile(r'(\d+)')
        page = gz.findall(page_num)
        for nums in page:  #获取每一个最大的页数
            for i in range(1,int(nums)+1):  #在遍历最大个页数
                res=re.sub(r'2,(\d+).html',"2,%s.html" % i,response.url) #正则替换response的url里的 *.html
                print "分页"
                yield scrapy.Request(res,callback=self.gs_parse,priority=2)

    #列表页的提取公司信息
    def gs_parse(self,response):
        print "开始解析"
        # title = response.xpath('//title/text()')[0].extract()
        # print title
        #print response.body.decode('gbk')
        detail_list = response.xpath('//div[@class="el"]')
        for detail in detail_list:
            #print response.body.decode('gbk')
            f = lambda x:x[0] if x else ''
            pos_name = f(detail.xpath('.//p/span[1]/a/text()').extract()) #公司需要的职位
            pos_name = self.meihua(pos_name)
            company = f(detail.xpath('.//span[@class="t2"]//a/text()').extract())   #这是公司名
            location = f(detail.xpath('.//span[@class="t3"]/text()').extract()) #这是公司地点
            salary = f(detail.xpath('.//span[@class="t4"]/text()').extract())  #这是薪水
            pub_date = f(detail.xpath('.//span[@class="t5"]/text()').extract())  #这是公司招聘发布时间
            detail_url = detail.xpath('.//p[@class="t1 "]//a/@href').extract()  #这是详情页的链接   要发起二次提取的链接

            #print pos_name,detail_url,company,location,salary,pub_date
            info = {
                'pos_name':pos_name,
                'company':company,
                'location':location,
                'salary':salary,
                'pub_date':"2017-"+pub_date,
                'detail_url':detail_url,
            }
            for url in detail_url:
                yield scrapy.Request(url=url,callback=self.detail_parse,meta=info,priority=1)
    # #解析响应页面
    def detail_parse(self,response):
        #print response.body.decode('gbk')
        item = Five1Item()
        pos_name = response.meta['pos_name']
        company = response.meta['company']
        location = response.meta['location']
        salary = response.meta['salary']
        pub_date = response.meta['pub_date']
        detail_url = response.meta['detail_url']

        pos_desc = response.xpath('//div[@class="bmsg job_msg inbox"]/text()').extract()    #职位描述
        experience = response.xpath('//div[@class="t1"]/span[1]/text()').extract()    #工作经验
        experience = self.suoyin(experience)
        edu_bg = response.xpath('//div[@class="t1"]/span[2]/text()').extract()        #教育背景
        edu_bg = self.suoyin(edu_bg)
        #print ''.join(gs_yq).strip()
        item['company'] = company                                    #公司名
        item['detail_url'] = detail_url                             #详情页链接
        item['pos_name'] = pos_name                                   #公司职位
        item['location'] = location                                     #公司地点
        item['salary'] = salary                                         #工资
        item['edu_bg'] = edu_bg                                          #教育背景
        item['experience'] = experience                                 #工作经验
        item['pub_date'] = pub_date                                     #发布日期
        item['pos_desc'] = ''.join(pos_desc).strip()                    #职位描述
        # crawled = time.strftime('%Y-%m-%d',time.localtime(time.time()))   #爬取时间
        print "生成,item"
        yield item

    def meihua(self,data):
        data = data.strip()
        return data
    def suoyin(self,data):
        return data[0] if data else ''




