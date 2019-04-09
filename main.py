# -*- coding: utf-8 -*-

import itchat
import sys
import re

reload(sys)
sys.setdefaultencoding('utf8')

cli_args = sys.argv[1:]

# lazy const
right_order_person_name = u'kayla王亚玲'

for index, arg in enumerate(cli_args):
    if index % 2 == 0 and arg == '-n':
        val = cli_args[index + 1]
        target_group_name = val

@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def print_content(msg):
    target_name = msg['User']['NickName']
    msg_text = msg['Text']
    groups = itchat.get_chatrooms(update=True)
    order_person_name = msg['ActualNickName']

    for group in groups:
        if group['NickName'] == target_group_name.decode('utf8'):
            if order_person_name.encode('utf8') != right_order_person_name.encode('utf8'):
                if re.search('(点|订)餐结束', msg_text.encode('utf8')):
                    send_msg('啊？你说什么？', group['UserName'])
                elif re.search('脚本', msg_text.encode('utf8')):
                    send_msg('脚本？什么脚本？🤔️', group['UserName'])
            elif msg_text == '[OK]' or msg_text == '好的':
                send_msg('谢谢啦🙏', group['UserName'])
            else:
                send_msg('啊！忘了点了！加一份谢谢😭', group['UserName'])

def send_msg(msg, user_name):
    itchat.send(msg.decode('utf8'), toUserName=user_name)

itchat.auto_login(hotReload=True)
itchat.run()
