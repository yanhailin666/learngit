import requests
from bs4 import BeautifulSoup

url="https://www.huobi.co/zh-cn/"
a = requests.get(url)
a.encoding=a.apparent_encoding
# print(a.text)
soup = BeautifulSoup(a.text,features='html.parser')



aa1=soup.find(class_="pur-content")
# aa2=soup.find_all("tr")
# # print(aa1)
print(aa1)
# aa2=soup.find_all("ul")
# print(aa2[2])

# a1=soup.find_all("h2")  symbol_list
# print("电影名称："+a1[0].text)
# aa = soup.find(class_='play-list').text
# # print(aa)
# if   u"高清" in aa :
#     print(a1[0].text+"可以观看")
# else:
#     print(a1[0].text+"：不是高清电影不建议观看")
#
# key1=x
# key2=y
#
# key1=x
# key2=y
# sum=x+y
# print(sum)