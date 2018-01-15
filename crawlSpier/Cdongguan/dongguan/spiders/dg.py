# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dongguan.items import DongguanItem


class DgSpider(CrawlSpider):
    name = 'dg'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    rules = (
        # 没有回调函数,follow默认为True,跟进页数的超链接
        Rule(LinkExtractor(allow=r'type=4&page=\d+')),
        # 使用parse_item做回调函数处理,定义了回调函数,follow默认为False
        Rule(LinkExtractor(allow=r'html/question/\d+/\d+.shtml'),follow=False,callback='parse_item'),
    )

    def parse_item(self, response):
        item = DongguanItem()
        # 拿到提问信息,包括编号
        title = response.xpath('//div[@class="pagecenter p3"]//strong/text()').extract()[0]
        # 通过切片得到提问信息
        item["question"] = title.split(' ')[1]
        # 通过切片得到编号
        item["number"] = title.split(' ')[-1].split(':')[-1]

        item["url"] = response.url
        item["answer"] = response.xpath('//div[@class="c1 text14_2"]/text()').extract()[0]

        yield item
