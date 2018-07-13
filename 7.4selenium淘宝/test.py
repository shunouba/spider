from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from selenium import webdriver
from pyquery import PyQuery as pq
import pymongo



option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
browser = webdriver.Chrome(chrome_options=option)
wait = WebDriverWait(browser, 10)
KEYWORD = 'ipad'
url = 'https://s.taobao.com/search?q=' + KEYWORD
browser.get(url)

a = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str('1')))
b = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
print(a)
print(b)