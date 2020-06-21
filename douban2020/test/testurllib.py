import urllib.request

response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read())
# 使用utf-8解码
print(response.read().decode("utf-8"))
print(response.status)
print(response.getheaders())

# 超时处理
try:
    response = urllib.request.urlopen("http://httpbin.org/get", timeout=0.01)
    print(response.read().decode("utf-8"))
except urllib.error.URLError as e:
    print("连接超时")

# 伪装成浏览器
url = "http://httpbin.org/post"
headers = {}  # 不带"user-agent会被识别为python
headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4043.400"}
data = bytes(urllib.parse.urlencode({"key": "value"}), encoding="utf-8")
req = urllib.request.Request(url=url, headers=headers, data=data, method="POST")
#把请求的网址，请求头，数据，请求方式封装,将请求的内容保存到响应
reponse = urllib.request.urlopen(req)
#把utf-8解码的响应打印出来
print(reponse.read().decode("utf-8"))

# 访问豆瓣首页
url="https://www.douban.com/"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4043.400"}
req=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(req)
print("访问豆瓣首页")
print(response.read().decode("utf-8"))