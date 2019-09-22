# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class DangdangPipeline(object):
    def process_item(self, item, spider):

        conn = pymysql.connect(host="127.0.0.1", user="root", passwd="root", db="dangdang", charset="utf8")

        for i in range(0,len(item["title"])):
            title = item["title"][i]
            link = item["link"][i]
            comment = item["comment"][i]
            sql = "insert into books(title,link,comment) VALUES('"+title+"', '"+link+"', '"+comment+"')"
            conn.query(sql)
            conn.commit()

        conn.close()

        return item
