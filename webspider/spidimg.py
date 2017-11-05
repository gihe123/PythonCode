import requests
import bs4 from BeautifulSoap
class Downloader(object):
	"""docstring for Downloader"""
	def __init__(self, arg):
		super(Downloader, self).__init__()
		self.arg = arg
'''
方法说明：返回全部文本
parameters:
	target  URL
return
	所有内容
'''
	def get_text(self,target):
		req=requests.get(target)
		return req.text

	def get_content(self,label,atribute):
		bf=BeautifulSoap(html,'lxml')
		find=bf.find_all(label,atribute)
