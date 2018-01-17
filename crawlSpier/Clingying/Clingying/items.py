# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ClingyingItem(scrapy.Item):
    head = scrapy.Field()
    work = scrapy.Field()
    company = scrapy.Field()
    school = scrapy.Field()
    address = scrapy.Field()
    call_num = scrapy.Field()
    work_experience = scrapy.Field()
    education_experience = scrapy.Field()