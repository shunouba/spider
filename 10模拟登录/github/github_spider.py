import requests
from lxml import etree



class Login():
    def __init__(self):
        self.headers = {
            # 'Referer': 'https://github/com',
            'Origin': 'https://github.com',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
            'Host': 'github.com'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.logined_url = 'https://github.com/settings/profile'
        self.session = requests.Session()


    def token(self):
        response = self.session.get(self.login_url, headers=self.headers)
        selector = etree.HTML(response.text)
        token = selector.xpath('//form/input[2]/@value')
        # 下面的写法对input标签不适用
        # token = selector.xpath('//form/input[name="authenticity_token"]/@value')
        print(token)
        return token

    def login(self,email,password):
        post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': self.token(),
            'login': email,
            'password': password,
        }
        response = self.session.post(self.post_url, data=post_data, headers=self.headers)
        print(response.text)



if __name__ == '__main__':
    login = Login()
    login.login(email='1176356268@qq.com', password='woshi2B0826')