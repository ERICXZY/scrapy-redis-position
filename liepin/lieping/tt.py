# #coding:utf8
# # for sheng in range(40):
# #     if len(str(sheng)) != 1:
# #         sheng = "0" + str(sheng)
# #         for shi in range(40):
# #             if len(str(shi)) != 1:
# #                 shi = sheng + "0" + str(shi)
# #                 for qu in range(40):
# #                     if len(str(qu)) != 1:
# #                         qu = shi + "0" + str(qu)
# #                         print qu
# #                     else:
# #                         qu = shi + "0" + str(qu) + "0"
# #                         print qu
# #             else:
# #                 shi = sheng + "0" + str(shi) + "0"
# #                 for qu in range(40):
# #                     if len(str(qu)) != 1:
# #                         qu = shi + "0" + str(qu)
# #                         print qu
# #                     else:
# #                         qu = shi + "0" + str(qu) + "0"
# #                         print qu
# #
# #     else:
# #         sheng = "0" + str(sheng) + "0"
# #         for shi in range(40):
# #             if len(str(shi)) != 1:
# #                 shi = sheng + "0" + str(shi)
# #                 for qu in range(40):
# #                     if len(str(qu)) != 1:
# #                         qu = shi + "0" + str(qu)
# #                         print qu
# #                     else:
# #                         qu = shi + "0" + str(qu) + "0"
# #                         print qu
# #             else:
# #                 shi = sheng + "0" + str(shi) + "0"
# #                 for qu in range(40):
# #                     if len(str(qu)) != 1:
# #                         qu = shi + "0" + str(qu)
# #                         print qu
# #                     else:
# #                         qu = shi + "0" + str(qu) + "0"
# #                         print qu
# #
# #
#
# a=[
#     #北京：
#     "010010010","010010020","010010030","010010050","010010070","010010080","010010090","010010100","010010110","010010120","010010130","010010140","010010150","010010160","010010170","010010180",
#     #上海：
#     "020010010","020010020","020010030","020010040","020010050","020010060","020010070","020010080","020010100","020010110","020010120","020010130","020010140","020010150","020010160","020010180","020010190",
#     #天津：
#     "030010010","030010020","030010030","030010040","030010050","030010060","030010070","030010080","030010090","03001010","030010110","030010120","030010130","030010140","030010150","030010160","030010170","030010180","030010200","030010210",
#     #重庆：
#     "040010010","040010020","040010030","040010040","040010050","040010060","040010070","040010080","040010090","040010100","040010110","040010120","040010130","040010140","040010170","040010420","040010180","040010190","040010200","040010210","040010220","040010230","040010240","040010250","040010260","040010270","040010280","040010290","040010300","040010310","040010320","040010330","040010340","040010350","040010360","040010370","040010380","040010390","040010410",
#     #广东
#     #广州：
#     "050020010","050020020","050020030","050020040","050020050","050020060","050020070","050020080","050020090","050020100","050020110","050020120",
#     #深圳：
#     "050090010","050090020","050090030","050090040","050090050","050090060","050090070","050090080","050090090","050090100",
#     #广东其他：
#     "050030","050040","050050","050060","050070","050080","050100","050110","050120","050130","050140","050150","050160","050170","050180","050190","050200","050210","050220","050230","050240","050250","050260","050270","050280","050290",
#
# ]
# #江苏：
# for i in range(2,32):
#     if i < 10:
#         i = "0" + str(i)
#     sheng = "060%s0" % i
#     a.append(sheng)
#
# #浙江：
# for i in range(2,35):
#     if i < 10:
#         i = "0" + str(i)
#     sheng = "070%s0" % i
#     a.append(sheng)
#
# #安徽：
# for i in range(2,22):
#     if i < 10:
#         i = "0" + str(i)
#     sheng = "080%s0" % i
#     a.append(sheng)
#
# #福建：
# for i in range(2,12):
#     if i < 10:
#         i = "0" + str(i)
#     sheng = "090%s0" % i
#     a.append(sheng)
#
# #甘肃
# for i in range(2,16):
#     if i < 10:
#         i = "0" + str(i)
#     sheng = "100%s0" % i
#     a.append(sheng)
#
# #广西
# for i in range(2,16):
#     if i < 10:
#         i = "0" + str(i)
#     sheng = "110%s0" % i
#     a.append(sheng)
#
# #贵州
# for i in range(2,11):
#     if i < 10:
#         i = "0" + str(i)
#     sheng = "120%s0" % i
#     a.append(sheng)
#
# #海南：
# for i in range(2,21):
#     if i < 10:
#         i = "0" + str(i)
#     sheng = "130%s0" % i
#     a.append(sheng)
#
# #河北：
# for i in range(2,18):
#     if i < 10:
#         i = "0" + str(i)
#     sheng = "140%s0" % i
#     a.append(sheng)
# #河南
# for i in range(2,22):
#     if i < 10:
#         i = "0" + str(i)
#     sheng = "150%s0" % i
#     a.append(sheng)
# #黑龙江：
# for i in range(2,20):
#     if i < 10:
#         i = "0" + str(i)
#     sheng = "160%s0" % i
#     a.append(sheng)
# #湖北：
# for i in range(2,22):
#     if i < 10:
#         i = "0" + str(i)
#     sheng = "170%s0" % i
#     a.append(sheng)
#
# #湖南：
# for i in range(2,16):
#     if i < 10:
#         i = "0" + str(i)
#     sheng = "180%s0" % i
#     a.append(sheng)
# #吉林：
# for i in range(2,13):
#     if i < 10:
#         i = "0" + str(i)
#     sheng = "190%s0" % i
#     a.append(sheng)
# #江西
# for i in range(2,13):
#     if i < 10:
#         i = "0" + str(i)
#     sheng = "200%s0" % i
#     a.append(sheng)
# #辽宁：
# for i in range(2,20):
#     if i < 10:
#         i = "0" + str(i)
#     sheng = "210%s0" % i
#     a.append(sheng)
# #内蒙古
# for i in range(2,16):
#     if i < 10:
#         i = "0" + str(i)
#     sheng = "220%s0" % i
#     a.append(sheng)
# #宁夏：
# for i in range(2,7):
#     if i < 10:
#         i = "0" + str(i)
#     sheng = "230%s0" % i
#     a.append(sheng)
# #青海：
# for i in range(2,10):
#     if i < 10:
#         i = "0" + str(i)
#     sheng = "240%s0" % i
#     a.append(sheng)
# #山东：
# for i in range(2,31):
#     if i < 10:
#         i = "0" + str(i)
#     sheng = "250%s0" % i
#     a.append(sheng)
# #山西：
# for i in range(2,15):
#     if i < 10:
#         i = "0" + str(i)
#     sheng = "260%s0" % i
#     a.append(sheng)
# #陕西：
# for i in range(2,14):
#     if i < 10:
#         i = "0" + str(i)
#     sheng = "270%s0" % i
#     a.append(sheng)
# #四川
# for i in range(2,26):
#     if i < 10:
#         i = "0" + str(i)
#     sheng = "280%s0" % i
#     a.append(sheng)
# #西藏：
# for i in range(2,9):
#     if i < 10:
#         i = "0" + str(i)
#     sheng = "290%s0" % i
#     a.append(sheng)
# #新疆：
# for i in range(2,22):
#     if i < 10:
#         i = "0" + str(i)
#     sheng = "300%s0" % i
#     a.append(sheng)
# #云南：
# for i in range(2,19):
#     if i < 10:
#         i = "0" + str(i)
#     sheng = "310%s0" % i
#     a.append(sheng)
#
# # for i in a:
# #     print i
#
# for i in range(2):
#     print i

#coding=utf-8
# import re
#
# str = '/zhaopin/?&d_=&ckid=c7c0caf43deb4204&fromSearchBtn=2&&init=-1&industryType=industry_03&&&degradeFlag=0&industries=080&salary=30$50&&headckid=c7bfbd1b20dc5335&d_pageSize=40&siTag=1B2M2Y8AsgTpgAmY7PhCfg%7EbbgKA2gP0gocFDpn9lXcPg&d_headId=3b0240f0cfc70a26b67a6b846fc6676b&d_ckId=bcc37c99ca8321144657ef4fb5a485f9&d_sfrom=search_fp_nvbar&d_&curPage=97'
# ret = re.split(r'curPage=\d+',str)
# str = "".join(ret)
#
# print str

# str = "    \n123\n"
# print str.strip("\n ")

import datetime
print datetime.datetime.utcnow()