import json
import re
# from .utils import get_page
from pyquery import PyQuery as pq
import requests
from lxml import etree
from requests.exceptions import ConnectionError
from redis import StrictRedis





def crawl_daili66(page_count):
    start_url = 'http://www.66ip.cn/{}.html'
    urls = [start_url.format(page) for page in range(1, page_count + 1)]
    print(urls)
    for url in urls:
        print('Crawling', url)
        html = requests.get(url,headers=base_headers)
        print(html.status_code)
        if html:
            a = html.text.encode('iso-8859-1').decode('gbk')
            b = etree.HTML(a)
            ip_list = b.xpath('//table/tr/td[1]/text()')
            ip_list.pop(0)
            ip_list.pop(0)
            ip_list.pop(0)
            port_list = b.xpath('//table/tr/td[2]/text()')
            port_list.pop(0)
            for i in range(len(ip_list)):
                ip_port_list = ':'.join([ip_list[i],port_list[i]])
                print(ip_port_list)
                # yield ip_port_list

def crawl_ip3366():
    for page in range(1, 4):
        url = 'http://www.ip3366.net/free/?stype=1&page={}'.format(page)
        print('Crawling', url)
        html = requests.get(url)
        if html:
            a = html.text.encode('iso-8859-1').decode('gbk')
            b = etree.HTML(a)
            ip_list = b.xpath('//table/tbody/tr/td[1]/text()')
            port_list = b.xpath('//table/tbody/tr/td[2]/text()')
            # for i in range(len(ip_list)):
            #     ip_port_list = ':'.join([ip_list[i], port_list[i]])
            #     print(ip_port_list)
            #     yield ip_port_list
            for ip, port in zip(ip_list,port_list):
                ip_port_list = ':'.join([ip,port])
                print(ip_port_list)
                # yield ip_port_list

# def init_redis():
#     redis = StrictRedis(host='localhost',port=6379,db=0,password='shun')



if __name__ == '__main__':
    base_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
        # 'Accept-Encoding': 'gzip, deflate, sdch',
        # 'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
    }
    # a = crawl_daili66(page_count=4)
    a = crawl_ip3366()






# def get_page(url, options={}):
#     """
#     抓取代理
#     :param url:
#     :param options:
#     :return:
#     """
#     headers = dict(base_headers, **options)
#     print('正在抓取', url)
#     try:
#         response = requests.get(url, headers=headers)
#         print('抓取成功', url, response.status_code)
#         if response.status_code == 200:
#             return response.text
#     except ConnectionError:
#         print('抓取失败', url)
#         return None


