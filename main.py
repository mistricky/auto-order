# -*- coding: utf-8 -*-

import itchat
import sys
import re

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    target_name = msg['User']['NickName']
    msg_text = msg['Text']

    a = msg_text.encode('utf8')

    if re.search('(点|订)餐结束', a):
        send_msg('加一份，谢谢')

def send_msg(msg):
    target_users = itchat.search_friends(name=u'晨二广元号子')
    friend_name = target_users[0]['UserName']
    itchat.send(msg.decode('utf8'), toUserName=friend_name)

itchat.auto_login(hotReload=True)
itchat.run()
