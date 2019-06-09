import urllib.request
import urllib.parse

url = 'https://weibo.cn/2996682383/info'
# 正常的方式进行访问
# headers = {
#  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
# }
# 携带cookie进行访问
headers = {
    'GET https': '//weibo.cn/pub/?tf=5_005 HTTP/1.1',
    'Host': ' weibo.cn',
    'Connection': ' keep-alive',
    'Upgrade-Insecure-Requests': ' 1',
    'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    'Accept': ' text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    # 'Referer: https':'//weibo.cn/',
    'Accept-Language': ' zh-CN,zh;q=0.9',
    'Cookie': 'SCF=AsDsQV7y--t6FRUTu3Eu3FAvBn8e098iJ5r79zVJk_QPZiEypqlcYXUSi67IjvmM2HgDIVkdWQMxOT0rvT74n7c.; SUB=_2A25x__rRDeRhGeRH4lQX-CzPwz-IHXVTA4aZrDV6PUJbkdAKLRLHkW1NTZwNFoPOyiQX_41yfnMB2lSDbJCqREd2; SUHB=0ebtfbT7dPIJnU; SSOLoginState=1559988865; MLOGIN=1; _T_WM=38801131065; M_WEIBOCN_PARAMS=luicode%3D20000174',
}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
# 输出所有
# print(response.read().decode('gbk'))
# 将内容写入文件中
with open('weibo.txt', 'wb') as fp:
    fp.write(response.read())
