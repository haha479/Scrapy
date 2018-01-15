# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # 职位名称
    name = scrapy.Field()

    # 职位类别
    type = scrapy.Field()

    # 招聘人数
    num = scrapy.Field()

    # 工作地点
    address = scrapy.Field()

    # 发布时间
    date = scrapy.Field()