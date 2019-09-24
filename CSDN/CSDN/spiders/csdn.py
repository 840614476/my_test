# -*- coding: utf-8 -*-
import scrapy
from CSDN.items import CsdnItem

import re
import urllib.request

class CsdnSpider(scrapy.Spider):
    name = 'csdn'
    allowed_domains = ['csdn.net']
    start_urls = ['http://csdn.net/']

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
    }

    def parse(self, response):
        item = CsdnItem()
        item["title"] = response.xpath("//div[@class='title']/h2/a[@target='_blank']/text()").extract()
        item["author"] = response.xpath("//dd[@class='name']/a[@target='_blank']/text()").extract()
        item["link"] = response.xpath("//dd[@class='name']/a[@target='_blank']/@href").extract()
        item["read_num"] = response.xpath("//dd[@class='read_num']/a/span[@class='num']/text()").extract()
        item["comment"] = response.xpath("//a[@target='_blank']/span[@class='num']/text()").extract()

        yield item


