# -*- coding: utf-8 -*-

import itchat
import sys
import re

cli_args = sys.argv[1:]

for index, arg in enumerate(cli_args):
    if index % 2 == 0 and arg == '-n':
        val = cli_args[index + 1]
        target_group_name = val

@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def print_content(msg):
    target_name = msg['User']['NickName']
    msg_text = msg['Text']
    groups = itchat.get_chatrooms(update=True)

    for group in groups:
        if group['NickName'] == target_group_name.decode('utf8') and re.search('(点|订)餐结束', msg_text.encode('utf8')):
            send_msg('加一份，谢谢', group['UserName'])

def send_msg(msg, user_name):
    itchat.send(msg.decode('utf8'), toUserName=user_name)

itchat.auto_login(hotReload=True)
itchat.run()
