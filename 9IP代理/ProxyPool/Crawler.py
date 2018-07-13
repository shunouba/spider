import json
import re
# from .utils import get_page
from pyquery import PyQuery as pq
import requests
from lxml import etree


class ProxyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls, name, bases, attrs)


class Crawler(object, metaclass=ProxyMetaclass):
    def __init__(self):
        self.headers = {
            'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
        }

    def get_proxies(self, callback):
        proxies = []
        for proxy in eval("self.{}()".format(callback)):
            print('成功获取到代理', proxy)
            proxies.append(proxy)
        return proxies

    def crawl_daili66(self, page_count=2):
        start_url = 'http://www.66ip.cn/{}.html'
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        print(urls)
        for url in urls:
            print('Crawling', url)
            html = requests.get(url,headers=self.headers)
            print(html.status_code)
            if html:
                # a = html.text.encode('iso-8859-1').decode('gbk')
                a = html.text
                b = etree.HTML(a)
                ip_list = b.xpath('//table/tr/td[1]/text()')
                ip_list.pop(0)
                ip_list.pop(0)
                ip_list.pop(0)
                port_list = b.xpath('//table/tr/td[2]/text()')
                port_list.pop(0)
                for i in range(len(ip_list)):
                    ip_port_list = ':'.join([ip_list[i], port_list[i]])
                    # print(ip_port_list)
                    yield ip_port_list

    def crawl_ip3366(self):
        for page in range(1, 3):
            url = 'http://www.ip3366.net/free/?stype=1&page={}'.format(page)
            print('Crawling', url)
            html = requests.get(url,headers=self.headers)
            if html:
                # a = html.text.encode('iso-8859-1').decode('gbk')
                a = html.text
                b = etree.HTML(a)
                ip_list = b.xpath('//table/tbody/tr/td[1]/text()')
                port_list = b.xpath('//table/tbody/tr/td[2]/text()')
                # for i in range(len(ip_list)):
                #     ip_port_list = ':'.join([ip_list[i], port_list[i]])
                #     print(ip_port_list)
                #     yield ip_port_list
                for ip, port in zip(ip_list, port_list):
                    ip_port_list = ':'.join([ip, port])
                    # print(ip_port_list)
                    yield ip_port_list
