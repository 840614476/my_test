# -*- coding: utf-8 -*-
import scrapy
from dangdang.items import DangdangItem
from scrapy.http import Request


class DdSpider(scrapy.Spider):
    name = 'dd'
    allowed_domains = ['dangdang.com']          # 允许爬取的域名，非此域名的网页不会爬取
    start_urls = ['http://dangdang.com/']       # 起始url，这里设置为从最大tid开始，向0的方向迭代

    # 用来保持登录状态，可把chrome上拷贝下来的字符串形式cookie转化成字典形式，粘贴到此处
    cookies = {'__permanent_id': '20190828140238355387507178102235978', ' from': '460-5-biaoti', ' ddscreen': '2', ' __ddc_15d_f': '1569080496%7C!%7C_utm_brand_id%3D11106', ' __rpm': 'mix_65152.403752%2C5357..1569080505752%7Cmix_104762.851950%2C6411..1569080597761', ' dest_area': 'country_id%3D9000%26province_id%3D111%26city_id%3D0%26district_id%3D0%26town_id%3D0', ' pos_9_end': '1569080607076', ' pos_6_end': '1569080608559', ' pos_6_start': '1569080678223', ' __visit_id': '20190922011748179288096685123812586', ' __out_refer': '1569086268%7C!%7Csp0.baidu.com%7C!%7C%25E5%25BD%2593%25E5%25BD%2593%25E7%25BD%2591', ' __trace_id': '20190922011748180411330592019118137', ' __ddc_1d': '1569086268%7C!%7C_utm_brand_id%3D11106', ' __ddc_24h': '1569086268%7C!%7C_utm_brand_id%3D11106', ' __ddc_15d': '1569086268%7C!%7C_utm_brand_id%3D11106', ' order_follow_source': 'P-460-5-bi%7C%231%7C%23sp0.baidu.com%252F9q9JcDHa2gU2pMbgoY3K%252Fadrc.php%253Ft%253D06KL00c00fZ-jkY07ZG-0KGwAsjxgmuI00000QyPw-C00000I3Ajcg%7C%230-%7C-'}

    # 发送给服务器的http头信息，有的网站需要伪装出浏览器头进行爬取，有的则不需要
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }

    def parse(self, response):
        item = DangdangItem()
        item["title"] = response.xpath("//a[@class='pic']/@title").extract()                    #提取书名
        item["link"] = response.xpath("//a[@class='search_comment_num']/@href").extract()       #提取连接
        item["comment"] = response.xpath("//a[@class='search_comment_num']/text()").extract()   #提取评论数
        yield item
        for i in range(2,27):
            url = "http://category.dangdang.com/pg" + str(i) + "-cp01.54.06.19.00.00.html"
            yield Request(url, callback = self.parse, headers=self.headers, cookies=self.cookies)       
