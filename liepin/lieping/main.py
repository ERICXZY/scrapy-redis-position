#coding:utf8
from scrapy import cmdline
import os
#要切换目录
os.chdir('./lieping/spiders')
cmdline.execute("scrapy runspider liepin.py".split())