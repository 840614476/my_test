# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import pymysql.cursors
from CSDN.items import CsdnItem


class CsdnPipeline(object):

    def process_item(self, item, spider):
        for i in range(0, len(item["title"])):

            conn = pymysql.connect(host="localhost", user="root", passwd="asdcvb13", db="Test", charset="utf8mb4")
            cursor = conn.cursor()          # 创建一个游标cursor, 是用来操作表。

            title = item["title"][i]
            author = item["author"][i]
            link = item["link"][i]
            read_num = item["read_num"][i]
            comment = item["comment"][i]

            sql = "INSERT INTO article(title,author,link,read_num,comment) VALUES('"+title+"', '"+author+"', '"+link+"', '"+read_num+"', '"+comment+"')"
            # params = (item['title'], item['author'], item['link'], item['read_num'], item['comment'])

            conn.query(sql)
            conn.commit()

        cursor.close()
        conn.close()

        return item
