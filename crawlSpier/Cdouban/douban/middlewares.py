# -*- coding:utf-8 -*-
import random
import base64
from douban.settings import USER_AGENTS
from douban.settings import PROXIES

# 随机的User-Agent
class RandomUserAgent(object):
	def process_request(self,request,spider):
		# 随机选择一个User-Agent
		useragent = random.choice(USER_AGENTS)
		# print useragent
		request.headers.setdefault("User-Agent" , useragent)

# 随机代理
class RandomProxy(object):
	def process_request(self,request,spider):
		# 随机选择一个代理
		proxy = random.choice(PROXIES)
		request.meta['proxy'] = "http://" + proxy['ip_port']
		if proxy['user_passwd'] is None:
			# 没有代理账户验证的代理使用方式(免费代理)
			print "haha"
			request.meta['proxy'] = "http://" + proxy['ip_port']

		else:
			# 对账户密码进行base64编码转换
			base64_userpasswd = base64.b64encode(proxy['user_passwd'])
			# 对应到代理服务器的信令格式里
			request.headers['Proxy-Authorization'] = 'Basic ' + base64_userpasswd

			request.meta['proxy'] = "http://" + proxy['ip_port']

