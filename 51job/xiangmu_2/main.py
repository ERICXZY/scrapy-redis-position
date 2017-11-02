from scrapy import cmdline
# cmdline.execute('scrapy crawl love'.split())

import os
os.chdir('xiangmu/spiders')
cmdline.execute('scrapy runspider one.py'.split())