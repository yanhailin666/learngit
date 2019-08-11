# -*- coding:utf-8 -*-获取cookie
from selenium import webdriver
import time
import requests

url="https://www.caimei365.com/login_loginLimit.action"
url2="https://www.caimei365.com/"
content={"account":"13066875865","passWord":"1111aaaa","identityFlag":"0"}

r=requests.post(url,data=content)
print(r.text)

# r1=requests.get(url2)  D:\PyCharm Community Edition 2017.3.2\requests_cookie.py
# print(r1.text)
# browser = webdriver.Firefox()
#
# url_3="https://www.caimei365.com"
# browser.get(url_3)
# time.sleep(3)
# cookies = browser.get_cookies() #获取cookie
# print(cookies)

