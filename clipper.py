import cv2
import numpy as np
from PIL import ImageGrab
import os


def matching(imgname, templatename, resultname):
    img = cv2.imread(imgname, 0)
    template = cv2.imread(templatename, 0)

    def size(h):
        return (int(h * w_h_ratio), h)

    (hm, wm) = img.shape
    print wm,hm

    (h,w) = template.shape
    w_h_ratio = 1. * w / h

    height_min = hm / 10
    step = hm / 30

    maxVal = None
    for h in xrange(height_min, hm, step):
        w,h = size(h)

        if w > wm:
            break

        print w,h
        resized = cv2.resize(template,(w,h),
         interpolation=cv2.INTER_AREA)
        res = cv2.matchTemplate(img, resized,cv2.TM_CCOEFF_NORMED)
        _,t,_,loc = cv2.minMaxLoc(res)

        if (maxVal is None or t > maxVal):
            maxVal = t
            top_left = loc
            bottom_right = (loc[0]+w, loc[1]+h)


    colorful = cv2.imread(imgname)
    result = colorful[top_left[1]:bottom_right[1],
                      top_left[0]:bottom_right[0]]
    cv2.imwrite(resultname, result)


def getCapture(sourcename):
    p = ImageGrab.grab()
    p.save(sourcename)

def fromTemplate(tmp):
    getCapture(src(tmp))
    matching(src(tmp), tmp, res(tmp))

def src(s):
    return "src_" + s

def res(s):
    return "res_" + s



def clean(s):
    os.remove(s)
    os.remove(src(s))
    os.remove(res(s))