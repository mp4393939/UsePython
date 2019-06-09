#!/usr/bin/python
#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import urllib.request
import urllib.parse
url = 'http://m.ucxiaoshuo.com/book/30249/16492796_1.html'
#正常的方式进行访问
headers = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36' }
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
req = requests.get(url = url)
html = req.text
bf = BeautifulSoup(html)
texts = bf.find_all('nr', class_ = 'nr_nr')
print(texts)
#输出所有
# print(response.read().decode('gbk'))
#将内容写入文件中
with open('weibo.txt','wb') as fp:
 fp.write(response.read())
print('小说内容已写入文本')
