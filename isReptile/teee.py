#!/usr/bin/python
# -*- coding: GBK -*-
import requests
r = requests.get('https://www.baidu.com/') # ����ַ��һ�����ǻ����� ����ͷ�����������ģ��������������н���
print(r.text)
print('С˵������д���ı�')