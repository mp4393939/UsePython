#!/usr/bin/python
# -*- coding: GBK -*-
import requests
r = requests.get('https://www.baidu.com/') # 打开网址，一般我们会设置 请求头，来更逼真的模拟浏览器，下文有介绍
print(r.text)
print('小说内容已写入文本')