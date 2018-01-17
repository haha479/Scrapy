# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request

class LingyingSpider(CrawlSpider):
	name = 'lingying'
	allowed_domains = ['www.linkedin.com']
	start_urls = ['http://www.linkedin.com/in/qi-hu-24623a117/']

	rules = (
		Rule(LinkExtractor(allow=r'/in/'), follow=False, callback='parse_item'),
	)
	def start_requests(self):
		print('444444444444444444444444444444444444444')
		cookies = {
			"bcookie" : "v=2&367ee934-e6b6-4ad2-8bf0-0f0edc6cf84a",
			"bscookie" : "v=1&201801170221019f135339-0c63-4f5e-8d40-4725e2cb1eb2AQGfyZtpene0WUJ7O9-ci1a2L2VlVkRR",
			"visit" : "v=1&M",
			"lang" : "v=2&lang=zh-cn",
			"JSESSIONID" : "ajax:0519148329685751114",
			"leo_auth_token" : "GST:Ztund1X1pdg2qB-iYdV1FCiD3oI2tvhi6DDn9zFn22jLttyyqzmedp:1516186193:ccec6f4a7038462c9023df56418b47682418985f",
			"liap" : "true",
			"li_at" : "AQEDASWzNNIE-RVRAAABYQO9T64AAAFhJ8nTrlEAEE3xxRLuscSuw8ctAnXKknLsxORdfm7-XXSUFXDOQxApGbG11VAh9-NoKFYiPCEQ2S1R6Z7JTjzXXPBd25FGtTIEN5TCrKe0ysF7V6ysGH_eMj3i",
			"RT" : "s=1516186194625&r=https%3A%2F%2Fwww.linkedin.com%2Fuas%2Flogin%3FformSignIn%3Dtrue%26session_redirect%3D%252Fvoyager%252FloginRedirect.html%26one_time_redirect%3Dhttps%253A%252F%252Fwww.linkedin.com%252Fm%252Flogin%252F",
			"_lipt" : "CwEAAAFhA79SKaRCMn-79BqOfTexG6b7qd-h-Q6_jY7tfBpze3v30T2xocjaM1pVca1-zR6uOzHjVjs-AgW8sY630P0_WhvEGDTmQ_5GWRGPotj61qXiI5X5tks",
			"lidc" : "b=SGST01:g=3:u=1:i=1516186327:t=1516241411:s=AQH4C3sMP8rEH2tRP8ljzChBIrS0Sv3p"
		}
		return [Request("http://www.linkedin.com/",cookies=cookies,callback=self.zhoubin)]
	def zhoubin(self, response):
		print('111111111111111111111111111111111111111')
		for url in self.start_urls:
			yield self.make_requests_from_url(url)

	def parse_item(self, response):
		print('22222222222222222222222222222222222222')
		print(response.body)

