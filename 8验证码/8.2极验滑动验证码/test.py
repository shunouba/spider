import time
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



EMAIL = '1176356268@qq.com'
PASSWORD = '123456'
# url = 'https://auth.geetest.com/register'
url = 'https://auth.geetest.com/login'
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 20)


def get_geetest_button():
    """
    获取初始验证按钮
    :return: 按钮对象
    """
    button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_radar_tip_content')))
    return button


def open():
    """
    打开网页输入用户名密码
    :return: None
    """
    browser.get(url)
    email = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="email"]')))
    password = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]')))
    email.send_keys(EMAIL)
    password.send_keys(PASSWORD)


def get_position():
    """
    获取图片位置
    :return: 图片位置元祖
    """
    img = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_fullbg')))
    time.sleep(2)
    location = img.location
    size = img.size
    top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size['width']
    return(top, bottom, left, right)


def get_screenshot():
    """
    获取网页截图
    :return: 截图对象
    """
    screenshot = browser.get_screenshot_as_png()
    screenshot = Image.open(BytesIO(screenshot))
    return screenshot


def get_geetest_img(name='captcha.png'):
    """
    获取验证码图片
    :param name:
    :return: 获取图片对象
    """
    top, bottom, left, right = get_position()
    print('图片验证码位置',top,bottom.left,right)
    screenshot = get_screenshot()
    captcha = screenshot.crop((left,top,right,bottom))
    return captcha


def get_slider():
    """
    获取滑块
    :return:滑块对象
    """
    slider = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_slider_button')))
    return slider


if __name__ == '__main__':
    open()
    # 点击验证按钮
    button = get_geetest_button()
    button.click()

    # 点击滑块
    slider = get_slider()
    slider.click()


