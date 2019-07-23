# -*- coding:utf-8 -*-爬虫看想看的电影是不是高清的
import requests
from bs4 import BeautifulSoup

#第一种方法
# url2="https://www.yyff2.com/movie/xiju/34266/"   #断片之险途夺宝
# url3="https://www.yyff2.com/movie/xiju/34252/"    #来电狂响
# url4="https://www.yyff2.com/movie/dongzuo/34055/"   #武林怪兽
# url5="https://www.yyff2.com/movie/dongzuo/33226/"  #中国蓝盔
# url6="https://www.yyff2.com/movie/dongzuo/32855/"   #三国幻杀
# url1 = 'https://www.yyff2.com/movie/juqing/34308/'  #地球最后的夜晚
# list1=[url1,url2,url3,url4,url5,url6]
# for i in list1:
#     print(i)


print("开始查询")
#第二种方法
# list=["xiju/34266","xiju/34252","dongzuo/34055","dongzuo/33226","dongzuo/32855","juqing/34308"]
# for i in list:
#     url1='https://www.yyff2.com/movie/'
#     a = requests.get(url1+str(i))

#第一种方法
url1 = 'https://www.yyff1.com/movie/juqing/34308/'  #地球最后的夜晚
url2="https://www.yyff1.com/movie/xiju/34266/"   #断片之险途夺宝
url3="https://www.yyff1.com/movie/xiju/34252/"    #来电狂响
url4="https://www.yyff1.com/movie/dongzuo/34055/"   #武林怪兽
url5="https://www.yyff1.com/movie/dongzuo/33226/"  #中国蓝盔
url6="https://www.yyff1.com/movie/dongzuo/32855/"   #三国幻杀
url7="https://www.yyff1.com/movie/xiju/34057/"    #天气预爆


list1=[url1,url2,url3,url4,url5,url6,url7]
for i in list1:
    # print(i)
    a = requests.get(i)
    a.encoding=a.apparent_encoding  #转格式编码
    # print(a.text)
    soup = BeautifulSoup(a.text,features='html.parser')
    # list =[soup.title]
    # print(list)
    # aa1=soup.h2   #直接打印页面的第一个h2标签对
    # print("电影名称："+aa1.string)
    a1=soup.find_all("h2")  #打印页面所有的h2标签对，可以用下标取值
    print("电影名称："+a1[0].text)
    aa = soup.find(class_='play-list')
    # print(aa)
    if   u"高清" in aa.text :
        print(aa.text+"可以观看")
        print(i)
    else:
        print(a1[0].text+"：不是高清电影不建议观看")
    print("------------^_^-------------")
print("查询完毕")