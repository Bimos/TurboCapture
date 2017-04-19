# -*- coding: UTF-8 -*-
import itchat
from clipper import *
import time
@itchat.msg_register(itchat.content.PICTURE)
def test(msg):
    print msg['ToUserName']
    if msg['ToUserName'] == 'filehelper':


        st = time.time()

        (pid,_) = msg['FileName'].split('.')
        path = base_path+'/'+pid+'/'
        if not(os.path.exists(path)):
            os.makedirs(path)

        getCapture(src_(path))
        with open(tmp_(path), "wb") as f:
            f.write(msg["Text"]())
        matching(path)
        print "time: ", (time.time() - st)

        itchat.send_image(res_(path), toUserName='filehelper')
        print "time: ", (time.time() - st)

def _make_dirs(s,name):

    (pid,png) = s.split('.')
    path = base_path+'/'+pid
    if not(os.path.exists(path)):
        os.makedirs(path)

    return path +'/'+ name + '.'+png

itchat.auto_login(hotReload=True)
itchat.run()
