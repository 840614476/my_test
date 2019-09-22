# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class JingdongPipeline(object):
    def process_item(self, item, spider):
        title = item["title"]
        shop = item["shop"]
        shop_link = item["shop_link"]
        price = item["price"]

        for i in range(0, len(item["title"])):
            print(title[i])
            print(shop[i])
            print(shop_link[i])
            print(price[i])
            print("………………")
        return item
