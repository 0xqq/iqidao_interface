# coding=utf-8
import requests
from unittesttool.Get_global_var import Return_global_var

# 判断前端或后端登陆，获取cookies
class Get_cookies:
    def __init__(self,i):
        self.global_var = Return_global_var()
        self.user = self.global_var.return_username(i)
        self.password = self.global_var.return_password(i)
        self.captcha = self.global_var .return_captcha(i)
        self.url = self.global_var .return_url(i)
    def get_cookies_admin(self):
        adminlogin_data = {
            'phone': self.user,
            'password': self.password,
            'captcha': self.captcha
        }
        r1 = requests.post(url=self.url, verify=False, data=adminlogin_data)
        cookies = r1.cookies
        return cookies
    def getcookies_web(self):
        web_login = {
            'key': self.user,
            'password': self.password,
            'captcha': self.captcha,
            "rememberMe": 1
        }
        r1 = requests.post(url=self.url, verify=False, data=web_login)
        cookies = r1.cookies
        return cookies
