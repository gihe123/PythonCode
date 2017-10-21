#-*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests,sys,os
"""
类说明：下载《笔趣看》网小说《一念永恒》

Parameters
  无
Return
  无
Modify
	2017-10-20

"""
class Downloader(object):
	def __init__(self):
		self.server='http://www.biqukan.com'
		self.target='http://www.biqukan.com/1_1094/'
		self.names=[]  #章节名
		self.urls=[]   #章节链接
		self.nums=0    #章节数
		"""
	函数说明：获取下载链接
	Parameters:
		无
	Returns:
			无
	Modify:
	2017-09-13
		"""
	def get_download_url(self):
		req=requests.get(url=self.target)
		html=req.text
		div_bf=BeautifulSoup(html,"lxml")
		div=div_bf.find_all('div',class_='listmain')
		a_bf=BeautifulSoup(str(div[0]),"lxml")
		a=a_bf.find_all('a')
		self.nums=len(a[15:])  #删除不必要的章节，并统计章节数
		for each in a[15:]:
			self.names.append(each.string)
			self.urls.append(self.server+each.get('href'))
	"""
	函数说明：获取章节内容
	Parameters:
		target --下载链接（string）
	Returns:
		texts --章节内容（string）
	Modify:
		2017-09-13
	"""
	def get_contents(self,target):
		req=requests.get(url=target)
		html=req.text
		bf=BeautifulSoup(html,"lxml")
		texts=bf.find_all('div',class_='showtxt')
		texts=texts[0].text.replace('        ','\n\n')
		return texts
	"""
	函数说明：获取章节内容
	Parameters:
		name --章节名称（string）
		path --章节路径，小说保存名称（string）
		text --章节内容（string）
	Returns:
		无
	Modify:
		2017-09-13
	"""
	def writer(self,name,path,text):
		write_flag=True
		with open(path,'a',encoding='UTF-8') as f:
			f.write(name+'\n')
			f.writelines(text)
			f.write('\n\n')
if __name__=="__main__":
	dl=Downloader()
	dl.get_download_url()
	print('《一年永恒》开始下载')
	for i in range(dl.nums):
		dl.writer(dl.names[i],'一年永恒.txt',dl.get_contents(dl.urls[i]))
		sys.stdout.write("  已下载:%.3f%%" %  float(i/dl.nums) + '\r')
		sys.stdout.flush()
	print("《一年永恒》下载完成！")

	# self.get_contents()
