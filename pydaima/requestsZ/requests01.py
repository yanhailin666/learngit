import requests


url="http://t.oa.quanhoo.com/v2/message/countMsgNumByIsRead?token=97ebe773-25ae-4e31-9506-0ab6eb1cb688177"
url1="http://t.oa.quanhoo.com/login/login"

#get请求
# r= requests.get(url)
# print(r.text)

print("----开始请求")
def post1(c1,c12,c21):
    #post请求   https://github.com/yanhailin666/learngit.git
    #请求头
    headers = {'user-agent': "my-app/0.0.1",
               'Connection': 'keep-alive',
               'Content-Type': 'application/x-www-form-urlencoded',
               'Content-Length': "34",
               'Host': 't.oa.quanhoo.com',
                'User-Agent': 'Apache-HttpClient/4.5.3'}

    #传参
    payload = {'loginCode':c1,'pwd':c12}
    payload1={'loginCode':c1,'pwd':c21}
    print("----第一个接口-----")
    #发起post请求
    r = requests.post(url1,data= payload,headers=headers,verify=False)
    # print(r.text)
    # print("---------")
    # print(r.json())
    rs=r.json()
    # print(rs["data"]["userName"])
    # print(rs["success"])

    if rs["success"]== False:
        print(rs["message"])
        return rs["message"]

    elif rs["success"]== True:
        # print(rs)
        print("用户-"+rs["data"]["userName"] + "登陆成功")

    else:
        print("接口访问失败")
    print('')
    print("----第二个接口-----")
    r = requests.post(url1,data= payload1,headers=headers,verify=False)
    rs=r.json()
    if rs["success"]== False:
        print(rs["message"])
        # print(rs)

    elif rs["success"]== True:
        print(rs["data"]["modifyBy"] + "接口登陆成功")

    else:
        print("接口访问失败")

print("\033[0;32m%s\033[0m" %"sasa")

post1("13066875865","gz123456","aa1234560")

print("\033[1;31m%s\033[0m" %"sasa")
print("\033[1;31;40m您输入的帐号或密码错误！\033[0m")
#测试登录接口
# ur301="https://www.caimei365.com/login_loginLimit.action?account="
# ur302="%09&passWord="
# ur303="&imgCode=&token=&identityFlag=0"
# #账号密码
# account="13066875865"
# passWord="1111aaaa"
#
# r=requests.get(ur301+account+ur302+passWord+ur303)
# print("---------")
# print(r.text)