# -*- coding:utf-8 -*-
import werobot
import re

robot = werobot.WeRoBot(token='yanhuaijun')

@robot.handler
def echo(message):
    return 'Hello World!'



@robot.text
def echo(message):
    # try:
    #     # 提取消息
    #     msg = message.content.strip().lower().encode('utf8')
        # 解析消息
        msg=message.content
        if  re.compile(".*?你好.*?").match(msg) or\
            re.compile(".*?嗨.*?").match(msg) or\
            re.compile(".*?哈喽.*?").match(msg) or\
            re.compile(".*?hello.*?").match(msg) or\
            re.compile(".*?hi.*?").match(msg) or\
            re.compile(".*?who are you.*?").match(msg) or\
            re.compile(".*?你是谁.*?").match(msg) or\
            re.compile(".*?你的名字.*?").match(msg) or\
            re.compile(".*?什么名字.*?").match(msg) :
            return "你好~\n我是呓语的管家机器人，主人还没给我起名字 T_T\n有什么能帮您的吗？（绅士脸）"
        elif re.compile(".*?厉害.*?").match(msg):
            return '承让承让 (๑•̀ㅂ•́)ﻭ✧'
        elif re.compile(".*?想你.*?").match(msg):
            return '我也想你'
        elif re.compile(".*?miss you.*?").match(msg):
            return 'I miss you,too'
        elif re.compile(".*?我爱你.*?").match(msg):
            return '我也爱你'
        elif re.compile(".*?love you.*?").match(msg):
            return 'I love you,too'
        elif re.compile(".*?美女.*?").match(msg):
            return '我是男生哦♂'
        elif re.compile(".*?帅哥.*?").match(msg):
            return '谢谢夸奖 (๑•̀ㅂ•́)ﻭ✧'
        elif re.compile(".*?傻逼.*?").match(msg):
            return '爸爸不想理你'
        else:
            return '噢，抱歉，没有你想要的结果！'
    # except Exception as e:
    #     print (e)
    #


robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80

robot.run()
