import requests
from lxml import etree

url = 'https://github.com/login'
response = requests.get(url)
print(response.text)


# def token():
#     login_url = 'https://github.com/login'
#     # session = requests.Session()
#     response = requests.get(login_url, headers=headers)
#     selector = etree.HTML(response.text)
#     token = selector.xpath('//script/@integrity')[0]
#     print(token)
#     return token
#
#
# url = 'https://github.com/session'
# email = '1176356268@qq.com'
# password = 'woshi2B0826'
# headers = {
#     'Referer': 'https://github/com',
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
#     'Host': 'github.com'
# }
# cookies = {
#     'Cookie':'logged_in=no; _ga=GA1.2.1994606258.1529812902; _gat=1; _octo=GH1.1.1367389139.1529812902; tz=Asia%2FShanghai; _gh_sess=aU0xUmpjcWtkbmlzNjlwOTZNOTJOOG1sKyt3d3BXaFFweTlBS2thYkFLOVp4KzR3S1JMQkR6SkYxeTMvSnNCamVNY1dhdy9EYlZkK2hMUFJCYVByVVUyWS8zVkRNWXVmcDN1S3JIRGJxT3Qrb2F3cmhLV3A0ajRxYmg2dER5RCs5VG54TndCMlo1ZVJaKzB4S1NBMnQ1NnFodEM4Ukg3ZllrYjhxMzRDRzlhVHV4c1Q1VnY5ZFZpNWNGUE1vYm0wZXBHaThzaVcrckI0Vytpbk9wNjRzRG96alR6NUxSNkZsMUJCZEtxSDU3amZaazNXOVh5aHcrd3ZpYWVMYlJQRFFQVXc4U3JpaHhDcVlmVERFY3h6enh4WnBJUi9qMVlIV2JkWVNkdjI3QURORUxLcEFkd1FFbTVpZVh4NFRTSW4tLWszSWJRMEYzR1JISUpHWktIVm1rWmc9PQ%3D%3D--dfd50abbf931af4f9c398a3a59b8e5f752e6f01f'
# }
# post_data = {
#             'commit': 'Sign in',
#             'utf8': '✓',
#             'authenticity_token': token(),
#             'login': email,
#             'password': password,
#         }
# response = requests.post(url,data=post_data,headers=headers,cookies=cookies)
# print(response.status_code)