# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

import scrapy
import urllib.request
from jingdong.items import JingdongItem
import re


class JdSpider(CrawlSpider):
    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = ['http://jd.com/']

    rules = (
        Rule(LinkExtractor(allow=''), callback='parse_item', follow=True),
    )

    def parse_item(self, response):

        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        try:
            i = JingdongItem()
            this_url = response.url               #获取当前爬取的页面
            form = "item.jd.com/(.*?).html"       #正则表达式
            x = re.search(form, this_url)

            #判断能够找到网页
            if (x):
                goods_id = re.compile(form).findall(this_url)[0]
                title = response.xpath("//div[@class='sku-name']/text()").extract()
                shop = response.xpath("//div[@class='usertopleft']/h2/text()").extract()
                shop_link = response.xpath("//div[@class='usertopleft']/a[@target='_blank']/@href").extract()

                #抓包分析商品价格的网址
                price_url = "https://p.3.cn/prices/mgets?callback=jQuery1888176&type=1&area=19_1601_3633_0&pdtk=&pduid=323942232&pdpin=&pin=null&pdbp=0&skuIds=J_" + str(goods_id) + "&ext=11100000&source=item-pc"
                #讲网址信息读取出来
                price_data = urllib.request.urlopen(price_url).read().decode("utf-8")
                #价格的正则
                price_form = '"p":"(.*?)"'
                #提取出来的价格
                price = re.compile(price_form).findall(price_data)

                if (len(title) and len(shop) and len(shop_link) and len(price)):
                    print(title[0])
                    print(shop[0])
                    print(shop_link[0])
                    print(price[0])
                    print("………………")

                else:
                    pass

            else:
                pass

            return i

        except Exception as e:
            print(e)

