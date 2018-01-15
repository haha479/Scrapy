# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DbcommentItem(scrapy.Item):
    # 书名
    book_name = scrapy.Field()
    # 评论人昵称
    pepole_name = scrapy.Field()
    # 有用数
    yes = scrapy.Field()
    # 评论日期
    date = scrapy.Field()
    # 评论内容
    content = scrapy.Field()