# encoding:utf-8
import scrapy
from tencent.items import TencentItem


class Tencentspider(scrapy.Spider):
	name = "tencent"
	allowed_domain = ["tencent.com"]
	url = "http://hr.tencent.com/position.php?&start="
	offset = 10
	start_urls = [url+str(offset)]

	def parse(self, response):
		node_list = response.xpath('//tr[@class="even"] | //tr[@class="odd"]')

		for node in node_list :
			# 创建item中的对象
			item = TencentItem()
			item["name"] = node.xpath('./td[@class="l square"]/a/text()').extract()[0]
			item["type"] = node.xpath('./td[2]/text()').extract()[0]
			item["num"] = node.xpath('./td[3]/text()').extract()[0]
			item["address"] = node.xpath('./td[4]/text()').extract()[0]
			item["date"] = node.xpath('./td[5]/text()').extract()[0]

			# 将item的数据迭代到piplines文件中
			yield item

		# 每遍历完一页让网页的偏移量加10
		if self.offset < 2610 :
			self.offset += 10


		# 再次发送请求
		yield scrapy.Request(self.url + str(self.offset),callback=self.parse)
