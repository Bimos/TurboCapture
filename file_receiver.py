# -*- coding: UTF-8 -*-
import itchat
import time
import os.path

MB=1<<20
default = lambda msg:0
callback = default
debug = 1

@itchat.msg_register(itchat.content.TEXT)
def receiver(msg):
    global callback
    callback(msg)
    callback = default

@itchat.msg_register(itchat.content.ATTACHMENT,isFriendChat=True, isGroupChat=True,)
def dl_attachment(msg):
    if (msg['FromUserName'] == itchat.search_friends()['UserName'] and not(debug)):
        return
    print "dl attachment"
    if int(msg['FileSize']) > 100 :
        txt = get_name(itchat.search_friends(userName=msg["FromUserName"])) + \
                    u'发送了一个文件: ' + msg['FileName'] + \
                    u', 大小为 ' + msg['FileSize'] + \
                    u', 是否接收到电脑上？'
        send_fh(txt)
        
        global callback
        @bool_msg
        def callback(b):
            if b:
                save_file(msg)
            else:
                skip()
    else:
        save_file(msg)
                
def bool_msg(func):
    def callback(msg0):
        val = None
        while val is None:
            if msg0["Text"] in ['Y', 'y', u'是']:
                val = True
            elif msg0["Text"] in ['N', 'n', u'否']:
                val = False
            else:
                send_fh(u"不支持的命令。重新来一遍")
        return func(val)
    return callback

def send_fh(text):
    return itchat.send_msg(text, toUserName="filehelper")

def save_file(msg):
    if not(os.path.exists("download")):
        os.mkdir("download")
    msg["Text"]("download/"+msg["FileName"])
    send_fh(u"成功接收")

def get_name(obj):
    if len(obj["DisplayName"]) == 0:
        return obj["NickName"]
    else:
        return obj["DisplayName"]
itchat.auto_login(hotReload=True)
itchat.run()