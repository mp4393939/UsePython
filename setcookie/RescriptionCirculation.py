import ssl
import urllib

import requests

headers = {
    'GET https': '//https://yx-cflz.kinglian.cn:8084/admin/drugOrder/getDrugOrderPage?page=1&limit=20 HTTP/1.1',
    'Host': 'yx-cflz.kinglian.cn',
    'port': '443',
    'Request Method': 'GET',
    'Connection': 'keep-alive',
    # token为空则看不到数据
    'token': 'c1b3c4b2-2d4a-486a-a641-7a6a09c57415',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400',
    'Cookie': 'Hm_lvt_c1b8f9036f2b5eb6c31ec6e2835c30eb=1558165912,1558847853,1560070761; x-access-token=c1b3c4b2-2d4a-486a-a641-7a6a09c57415; Hm_lpvt_c1b8f9036f2b5eb6c31ec6e2835c30eb=1560073097'
}  # cookie
ssl._create_default_https_context = ssl._create_unverified_context
request = urllib.request.Request('https://yx-cflz.kinglian.cn:8084/admin/drugOrder/getDrugOrderPage?page=1&limit=20',headers=headers)
response = urllib.request.urlopen(request)
print(response.read())
with open('weibo.txt', 'wb') as fp:
    fp.write(response.read())
