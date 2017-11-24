# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class DangdangPipeline(object):
    def process_item(self, item, spider):
        #连接数据库
        conn = pymysql.connect(host="192.168.6.250",user="root",passwd="111111",db="scrapy",charset='UTF8')
        for i in range(0,len(item["title"])):
            title = item["title"][i]
            link = item["link"][i]
            comment = item["comment"][i]
            #print("标题 %s---链接 %s---评论 %s" %(title,link,comment))
            sql="insert into dangdang(title,link,comment) VALUES('"+title+"','"+link+"','"+comment+"')"
            cursor = conn.cursor()
            try:  #异常处理
                cursor.execute(sql)
            except Exception as err:  #输出异常处理
                print(err)
            conn.commit()
            #print(sql1)
        conn.close()
        return item
