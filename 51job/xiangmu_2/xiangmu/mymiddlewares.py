#coding:utf8
from settings import USER_AGENS
import random

# 随机更换浏览器身份中间件
class RandomUserAgent(object):
    def process_request(self,request,spider):
        user_agent = random.choice(USER_AGENS)
        request.headers.setdefault('User-Agent',user_agent)