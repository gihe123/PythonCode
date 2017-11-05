#-*- coding:UTF-8 -*-
import requests
if __name__ == '__main__':
	target='https://unsplash.com/napi/feeds/home'
	headers={'authorization':'your Client-ID'}
	req=requests.get(url=target,verify=False)
	print(req.text)