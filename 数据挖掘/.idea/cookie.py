#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:TBH time:2019/9/22


b = '__permanent_id=20190828140238355387507178102235978; from=460-5-biaoti; ddscreen=2; __ddc_15d_f=1569080496%7C!%7C_utm_brand_id%3D11106; __rpm=mix_65152.403752%2C5357..1569080505752%7Cmix_104762.851950%2C6411..1569080597761; dest_area=country_id%3D9000%26province_id%3D111%26city_id%3D0%26district_id%3D0%26town_id%3D0; pos_9_end=1569080607076; pos_6_end=1569080608559; pos_6_start=1569080678223; __visit_id=20190922011748179288096685123812586; __out_refer=1569086268%7C!%7Csp0.baidu.com%7C!%7C%25E5%25BD%2593%25E5%25BD%2593%25E7%25BD%2591; __trace_id=20190922011748180411330592019118137; __ddc_1d=1569086268%7C!%7C_utm_brand_id%3D11106; __ddc_24h=1569086268%7C!%7C_utm_brand_id%3D11106; __ddc_15d=1569086268%7C!%7C_utm_brand_id%3D11106; order_follow_source=P-460-5-bi%7C%231%7C%23sp0.baidu.com%252F9q9JcDHa2gU2pMbgoY3K%252Fadrc.php%253Ft%253D06KL00c00fZ-jkY07ZG-0KGwAsjxgmuI00000QyPw-C00000I3Ajcg%7C%230-%7C-'
cookie = {}
for line in b.split(';'):
    key, value = line.split('=', 1)
    cookie[key] = value
print(cookie)