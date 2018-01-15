# -*- coding: utf-8 -*-
import scrapy
from dongguan.items import DongguanItem

class DgSpider(scrapy.Spider):
    name = 'dg'
    allowed_domains = ['wz.sun0769.com']
    url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        # 得到一页中30个超链接
        links = response.xpath('//a[@class="news14"]/@href').extract()
        for link in links :
            # print link
            # 返回response并交给parse_item处理
            yield scrapy.Request(link,callback=self.parse_item)

        if self.offset < 83280 :
            self.offset += 30
            # 一页中30个链接处理完后接这处理下一页
            yield scrapy.Request(self.url + str(self.offset),callback=self.parse)

    def parse_item(self, response):
        print response
        # item = DongguanItem()
        # item["title"] = response.xpath('//div[@class="pagecenter p3"]//strong/text()').extract()[0]
        # item["number"] = item["title"].split(' ')[-1].split(':')[-1]
        # item["url"] = response.url
        # item["content"] = response.xpath('//div[@class="c1 text14_2"]/text() | //div[@class="contentext"]/text()').extract()
		#
        # yield item
