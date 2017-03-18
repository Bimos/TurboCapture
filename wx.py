# -*- coding: UTF-8 -*-
import itchat
from clipper import *
import time

@itchat.msg_register(itchat.content.PICTURE)
def test(msg):
    print msg['ToUserName']
    if msg['ToUserName'] == 'filehelper':


        st = time.time()

        fn = msg['FileName']
        with open(fn, "wb") as f:
            f.write(msg["Text"]())
        fromTemplate(fn)
        itchat.send_image(res(fn), toUserName='filehelper')

        et = time.time()
        print (et - st)
        # clean(fn)

itchat.auto_login(hotReload=True)
itchat.run()
