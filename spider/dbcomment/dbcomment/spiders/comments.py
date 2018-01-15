# -*- coding: utf-8 -*-
import scrapy
import re


class CommentsSpider(scrapy.Spider):
    name = 'comments'
    allowed_domains = ['book.douban.com']
    start_urls = ['http://book.douban.com/']
    def parse(self, response):
        hrefs = response.xpath('//ul[@class="list-col list-col2 list-summary s"]//div[@class="cover"]/a/@href').extract()
        for href in hrefs :
            # 得到十本书中每本书中url的数字
            num = re.match(r'https://book.douban.com/subject/(\d+)',href).group(1)
            link ='book.douban.com/subject' + str(num) + "/comments/"
            yield scrapy.Request(url = link,callback=self.parse_it)

    def parse_it(self,response):
        print "Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"