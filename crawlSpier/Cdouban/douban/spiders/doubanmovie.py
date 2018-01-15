# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from douban.items import DoubanItem


class DoubanmovieSpider(CrawlSpider):
    name = 'doubanmovie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250?start=0']

    rules = (
        Rule(LinkExtractor(allow=r'start=\d+&filter='), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        movies = response.xpath('//div[@class="info"]')
        for each in movies :
            item = DoubanItem()
            # 标题
            item['name'] = each.xpath(".//span[@class='title'][1]/text()").extract()[0]
            # 信息
            item['info'] = each.xpath(".//div[@class='bd']/p/text()").extract()[0]
            # 评分
            item['rating'] = each.xpath(".//div[@class='star']/span[@class='rating_num']/text()").extract()[0]
            # 简介
            item["quote"] = each.xpath(".//p[@class='quote']/span/text()").extract()[0]

            # 到管道文件
            yield item