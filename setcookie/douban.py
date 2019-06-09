import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
    'Cookie': 'viewed="3516753"; bid=XpT30PVFT1w; gr_user_id=e8fd418d-1cbb-4ca4-a81d-616b86394316; __utmz=30149280.1557832958.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _vwo_uuid_v2=D8D88C03EF71515E9DA1572CD69E6C609|f5d9950baf00bb989863ce6b13cfce36; ap_v=0,6.0; __utma=30149280.1961723458.1557832958.1557832958.1559921365.2; __utmc=30149280; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1559922049%2C%22https%3A%2F%2Faccounts.douban.com%2Faccounts%2Fpassport%2Fregister%22%5D; _pk_ses.100001.8cb4=*; push_noty_num=0; push_doumail_num=0; __utmv=30149280.19754; douban-profile-remind=1; __utmb=30149280.71.10.1559921365; _pk_id.100001.8cb4=120b4128de572bbd.1559922049.1.1559922734.1559922049.; dbcl2="197545292:XJ7bZ2b7FsA"'
}  # cookie
r = requests.get('https://www.douban.com/contacts/list', headers=headers)
print(r.text)
