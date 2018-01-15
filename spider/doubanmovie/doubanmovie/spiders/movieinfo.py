# -*- coding: utf-8 -*-
import scrapy
from doubanmovie.items import DoubanmovieItem


class MovieinfoSpider(scrapy.Spider):
    name = 'movieinfo'
    allowed_domains = ['movie.douban.com']
    url = 'https://movie.douban.com/top250?start='
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        movies = response.xpath('//div[@class="info"]')
        for each in movies :
            item = DoubanmovieItem()
            item['moviename'] = each.xpath('./div[@class="hd"]/a/span[1]/text()').extract()[0]
            item['info'] = each.xpath('./div[@class="bd"]/p/text()').extract()[0]
            item['star'] = each.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            quote = each.xpath('.//p[@class="quote"]/span/text()').extract()
            if len(quote) != 0 :
                item["quote"] = quote[0]
            yield item
        if self.offset < 225 :
            self.offset += 25
            yield scrapy.Request(self.url + str(self.offset),callback=self.parse)

