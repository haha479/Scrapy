# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tencent.items import TencentItem


class TencentspiderSpider(CrawlSpider):
    name = 'tencentspider'
    # 允许爬虫爬取的域名
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?&start=0#a=0']

    """
        linkExtractor : 深度跟进使用正则匹配网页中的链接
        callback : 找到匹配的链接时,使用该方法处理
        follow : 是否跟进
    """
    rules = (
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=True),
    )

    # 指定的回调函数
    def parse_item(self, response):
        link_list = response.xpath('//tr[@class="even"] | //tr[@class="odd"]')

        for each in link_list :
            item = TencentItem()
            item["positionname"] = each.xpath('./td[1]/a/text()').extract()[0]
            item["positionlink"] = each.xpath('./td[1]/a/@href').extract()[0]
            item["positionType"] = each.xpath('./td[2]/text()').extract()[0]
            item["peopleNum"] = each.xpath('./td[3]/text()').extract()[0]
            item["workLocation"] = each.xpath('./td[4]/text()').extract()[0]
            item["publishTime"] = each.xpath('./td[5]/text()').extract()[0]

            # 将item数据输送到piplines文件中
            yield item