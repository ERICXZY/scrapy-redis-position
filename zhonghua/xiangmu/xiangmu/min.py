from scrapy import cmdline
# cmdline.execute('scrapy crawl mi'.split())
#
import os
#
os.chdir('spiders')
cmdline.execute('scrapy runspider tmps.py'.split())