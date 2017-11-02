# coding:utf8
import json
import redis
import MySQLdb
def min():
    try:
        rediscli = redis.StrictRedis(host='192.168.2.129',port=6379,password='123456',db=1)
        mysqlcli = MySQLdb.connect(host='192.168.2.129', user='root', passwd='123456', db = 'TESTDB', port=3306, charset='utf8')
    except Exception,e:
        print '数据库连接失败'
        print str(e)
        exit()
    while True:

        source, data = rediscli.blpop(["tmps:items"])
        #将json转换为字典，进行数据存储
        item = json.loads(data)
        cur = mysqlcli.cursor()
        sql = "insert into Job(detail_url,pos_name,company,salary,location,pos_desc,crawled,spider,pub_date,edu_bg,experience) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) on duplicate key update " \
              "pos_name=values(pos_name),company=values(company),salary=values(salary),location=values(location),pos_desc=values(pos_desc),crawled=values(crawled),spider=values(spider),pub_date=values(pub_date),edu_bg=values(edu_bg),experience=values(experience)"
        try:
            cur.execute(sql,(item["detail_url"],item["pos_name"],item["company"],item["salary"],item["location"],item["pos_desc"],item["crawled"],item["spider"],item["pub_date"],item["edu_bg"],item["experience"]))
            mysqlcli.commit()
            cur.close()
            print "插入成功"
        except Exception,e:
            print "插入失败：%s" % str(e)

if __name__ == '__main__':
    min()

