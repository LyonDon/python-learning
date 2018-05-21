#coding=utf-8
class UrlManager(object):
	"""docstring for UrlManager"""
	def __init__(self):
		self.new_urls=set()
		self.old_urls=set()

	def has_new_url(self):
		'''
		判断是否有未爬取的url
		：return
		'''
		return self.new_url_size()!=0
		pass

	def get_new_url(self):
		'''
		获取一个未爬取的url
		：return：
		'''
		new_url=self.new_urls.pop()
		self.old_urls.add(new_url)
		return new_url
		pass

	def add_new_url(self,url):
		'''
		将新的url添加到未爬取的url集合中
		'''
		if url is None:
			return
		if url not in self.new_urls and url not in self.old_urls:
			self.new_urls.add(url)
		pass

	def add_new_urls(self,urls):
		if urls is None or len(urls)==0:
			return
		for url in urls:
			self.add_new_url(url)
			pass
		pass

	def new_url_size(self):
		return len(self.new_urls)
		pass

	def old_urls_size(self):
		return len(self.old_urls)
		pass