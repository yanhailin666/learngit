from bs4 import BeautifulSoup
from selenium import webdriver
import re
import requests
import random


def url_position():
    driver = webdriver.PhantomJS(executable_path=r"C:\Users\PJlaptop\Downloads\phantomjs-2.1.1-windows\bin\phantomjs.exe")# 需要下载防爬工具Zip压缩包解压后exe文件所在的完整的位置
    url = "https://sh.fang.anjuke.com/loupan/s?kw=%E5%A4%A9%E6%B2%B3"#后面跟地址
    # print(url)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "lxml")
    #print(soup)
    namelist1 = str(soup.findAll("li"))
    #print(namelist1)
    pick = re.findall(r'<li.+?data-href="(.+?)"', namelist1)#打印所有的url
    #print(pick)
    return pick
def agent_ip():#代理ip
    def get_ip_list(url, headers):
        web_data = requests.get(url, headers=headers)
        soup = BeautifulSoup(web_data.text, 'lxml')
        ips = soup.find_all('tr')
        ip_list = []
        for i in range(1, len(ips)):
            ip_info = ips[i]
            tds = ip_info.find_all('td')
            ip_list.append(tds[1].text + ':' + tds[2].text)
        return ip_list

    def get_random_ip(ip_list):
        proxy_list = []
        for ip in ip_list:
            proxy_list.append('http://' + ip)
        proxy_ip = random.choice(proxy_list)
        proxies = {'http': proxy_ip}
        return proxies

    if __name__ == '__main__':
        url = 'http://www.xicidaili.com/nn/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
        }
        ip_list = get_ip_list(url, headers=headers)
        proxies = get_random_ip(ip_list)
        #print(proxies)
        return proxies

def Virtual_Browser():#虚拟浏览器进行访问
    pick=url_position()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    #url = "http://sh.fang.anjuke.com/loupan/411368.html"
    proxies = {'http': 'http://60.218.171.203:80'}
    print(proxies)
    for url in pick:
        print(url)
        url1='http://sh.fang.anjuke.com/loupan/423720.html'
        response = requests.post(url=url, headers=headers, proxies=proxies).text
        # print(response)
        soup = BeautifulSoup(response, "lxml")
        #print(soup)
        namelist2 = soup.find(class_="basic-parms-wrap")
        # print(namelist2)
        namelist3 = soup.find(class_="lp-alias g-overflow").text
        print("楼盘 ：" + namelist3)
        namelist4 = soup.find(class_="sp-price other-price").text
        print("价格 ：" + namelist4 + "元/㎡")
        namelist5 = soup.find(class_="house-item g-overflow").text
        print("户型 ：" + namelist5)
        namelist6 = soup.find(class_="lpAddr-text g-overflow").text
        print("地址 ：" + namelist6)



Virtual_Browser()
