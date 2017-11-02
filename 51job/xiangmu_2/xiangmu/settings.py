# -*- coding: utf-8 -*-

# Scrapy settings for xiangmu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'xiangmu'

SPIDER_MODULES = ['xiangmu.spiders']
NEWSPIDER_MODULE = 'xiangmu.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'xiangmu (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 80

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 100
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
   # "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.8",
    "Cache-Control":"max-age=0",
    "Connection":"keep-alive",
    #"Cookie":"guid=15087609007718700098; search=jobarea%7E%60010000%7C%21ord_field%7E%600%7C%21recentSearch0%7E%601%A1%FB%A1%FA010000%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA33%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA%B5%E7%D7%D3%B9%A4%B3%CC%CA%A6%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1508760900%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; NSC_tfbsdi.51kpc.dpn-159=ffffffffc3a01b3f45525d5f4f58455e445a4a423660",
    "Host":"search.51job.com",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",

 }

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'xiangmu.middlewares.XiangmuSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
# #    'xiangmu.middlewares.MyCustomDownloaderMiddleware': 543,
#     'xiangmu.mymiddlewares.RandomUserAgent': 3,
#
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'xiangmu.pipelines.JobPipeline':2,
#    'xiangmu.pipelines.XiangmuPipeline': 300,
    # 'xiangmu.pipelines.Five1Pipeline':1,
#     'xiangmu.pipelines.MysqlPipeline':2,
    #'xiangmu.pipelines.list_ipPipeline':3,
    #'xiangmu.pipelines.TruelovePipeline': 1,
    'scrapy_redis.pipelines.RedisPipeline': 999,   # 数据统一存到redis服务器上的 管道文件

}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

#随机请求USER-Agent
# USER_AGENS = [
#     'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)',
#     'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3'
#     'Mozilla/4.0 (compatible; MSIE 7.0; Windows Phone OS 7.0; Trident/3.1; IEMobile/7.0; LG; GW910)'
#     'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3'
# ]


# #所有城市
# city_list = [
#     '010000','020000','030200','040000','180200','200200','080200','070200','090200','060000','030800','230300','230200','070300','250200','190200','150200','080300','170200','050000','120300','120200','220200','240200','110200'
#     '092200','310600','310900','281500','311300','300800','230400','201000','150400','260500','170900','280900','311800','092000','241000','101800','240900','270800','141100','150600','280400','160400','251200','101700','200400','140500','010000','231000','260700','121500','311900','151800','160800','300600','311200','101900','190700','070700','070500','240200','190200','210600','231400','032000','190900','090200','101300','161000','151500','280300','141400','150900','251700','060000'
#     '091700','250500','230300','220500','210400','221400','230800','072100','251600','090600','121300','172000','252000','101100','271100','100900','121000','030800','100800','280800','181000','181800','140800','030600','110200','230600','131100','231500','150700','271500','092100','130800','290600','091300','091600','030200','140300','141000','260200','320800'
#     '220200','310700','320500','320300','100200','320700','081600','320400','160700','200900','080200','121400','311600','150200','141200','032100','171700','221000','141500','221200','161200','190500','251000','280200','281100','230900','080900','191100','071900','151700','151100','181100','320600','151000','180400','030300'
#     '220900','130900','240300','120200','120900','171900','080700','270400','220800','031500','170500','032200','270300','080600','230700','210700','211000','180800','180700','130400','072500','130300','270500','310400','170400','032700','310300','311700','250200','070600'
#     '300200','121800','141300','270200','160300','090400','250600','081000','071200','092300','121700','231100','240400','300400','251800','210500','101400','271400','120800','102100','140400','151200','260400','111000','271200','191200','211200','170300','090500','171500','150500','032300','032600','091200','090300','220700','300700','130200','091100','070200','140200','110800','070900','170600','090900','080300','110900','251900'
#     '091000','231300','130500','171000','271000','110600','251100','171600','221300','220600','260900','261000','260800','181500','140900','160600','120300','031900','271300','100600','101600','250300','110400','081200','300300','121200'
#     '171800','110700','101500','100300','300500','030400','032400','201100','171300','020000','131200','031400','191000','080500','040000','181700','230200','180600','310800','160200','290500','221100','210900','240600','240700','070300','072000','151600','181200','220400','091500','311500','080800','121100','072300','071800','071600','210200','160500','050000','181600','270600','231200','240500','280700','200500','150800','260600','311100','311400','101200'
#     '100700','120600','120500','200700','080400','100500','251400','281000','281200','310200','070400','150300','140700','290300','180200','270700','311000','101000','200200','091900','320200','251500','281400','110300','181400','181300','200300','180500','190400','191500','180900','170700','130600','211100','171200','281300','161100','071100','171100','151400'
#     '102000','091800','120400','071300','200600','241100','240800','161300','201200','070800','100400','032800','210800','220300','310500','090700','180300','131000','081400','190800','290200','130700','230500','191300','200800','140600','320900','250400','190600','032900','210300','121600','031700','110500','071400','191400','160900','270900','251300','031800','071000','170200','030700','290400','081100','170800','030500','190300','171400','091400','120700','090800','260300'
#     '030000','070000','080000','090000','100000','110000','120000','130000','140000','150000','160000','170000','180000','190000','200000','210000','220000','230000','240000','250000','260000','270000','280000','290000','300000','310000','320000','330000','340000','350000'
#     ]


# city_list = [
#     '010000','020000'
# ]

# ---------------------------------scrapy-redis-----------------------------------
# url 过滤 用scrapy_redis
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 调度器改成 scrapy-redis 调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 可以暂停
SCHEDULER_PERSIST = True

# 请求队列模式
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue" # 优先级
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"  # 队列
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"  # 栈  先进后出

# LOG_LEVEL = 'DEBUG'
# redis服务器的 ip地址和端口号
# REDIS_HOST = '192.168.2.129'
# REDIS_PORT = 6379
REDIS_URL = 'redis://:123456@192.168.2.190:6379/0'




