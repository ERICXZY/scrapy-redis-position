#coding:utf8
#写入数据库

import MySQLdb
import redis
import json

def main():
    #连接
    try:
        redis_cli = redis.StrictRedis(host='192.168.2.190', port=6379, db=0 ,password="123456")
        mysql_cli = MySQLdb.connect(host='192.168.2.190', user='root', passwd='123456', db='mypython', port=3306, charset='utf8')
    except Exception,e:
        print "数据库连接失败,错误信息：%s" % str(e)
        #如果连接失败则退出
        exit()

    #操作
    while True:
        source, data = redis_cli.blpop(["one:items"])
        #将json转换为字典，进行数据存储
        item = json.loads(data)
        cur = mysql_cli.cursor()
        sql = "insert into 51job(detail_url,pos_name,company,salary,location,pos_desc,crawled,spider,pub_date,edu_bg,experience) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) on duplicate key update " \
              "pos_name=values(pos_name),company=values(company),salary=values(salary),location=values(location),pos_desc=values(pos_desc),crawled=values(crawled),spider=values(spider),pub_date=values(pub_date),edu_bg=values(edu_bg),experience=values(experience)"
        try:
            cur.execute(sql,(item["detail_url"],item["pos_name"],item["company"],item["salary"],item["location"],item["pos_desc"],item["crawled"],item["spider"],item["pub_date"],item["edu_bg"],item["experience"]))
            mysql_cli.commit()
            cur.close()
            print "插入成功"
        except Exception,e:
            print "插入失败：%s" % str(e)

if __name__ == '__main__':
    main()



