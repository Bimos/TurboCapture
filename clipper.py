import cv2
import numpy as np
from PIL import ImageGrab
import os
import csv
base_path = 'data'



def src_(s):
    return s+'src.png'

def res_(s):
    return s+'res.png'

def tmp_(s):
    return s+'tmp.png'

def matching(s):
    templatename = tmp_(s)
    imgname = src_(s)
    resultname = res_(s)

    img = cv2.imread(imgname, 0)
    template = cv2.imread(templatename, 0)

    def size(h):
        return (int(h * w_h_ratio), h)

    (hm, wm) = img.shape
    (h,w) = template.shape
    w_h_ratio = 1. * w / h

    height_min = hm / 5
    step = hm / 40
    # step = 1
    maxVal = None
    for h in xrange(height_min, hm, step):
        w,h = size(h)

        if w > wm:
            break
        resized = cv2.resize(template,(w,h),
         interpolation=cv2.INTER_AREA)
        res = cv2.matchTemplate(img, resized,cv2.TM_CCOEFF_NORMED)
        _,t,_,loc = cv2.minMaxLoc(res)
        # t,_,loc,_ = cv2.minMaxLoc(res)
        # if (maxVal is None or t < maxVal):
        if (maxVal is None or t > maxVal):
            maxVal = t
            top_left = loc
            bottom_right = (loc[0]+w, loc[1]+h)
            hmaaa = h


    print "similar = ", maxVal
    print "hmaaa = ", hmaaa
    colorful = cv2.imread(imgname)
    result = colorful[top_left[1]:bottom_right[1],
                      top_left[0]:bottom_right[0]]
    cv2.imwrite(resultname, result)

    print top_left, bottom_right, hm, wm
    with open(s+'res.txt','w') as f:
        __little_helper(f,
            [1.*top_left[0]/wm,1.*top_left[1]/hm,1.*bottom_right[0]/wm,1.*bottom_right[1]/hm])

def __little_helper(f,lst):
    for n in lst:
        f.write(str(n))
        f.write('\n')
    f.flush()

def getCapture(sourcename):
    p = ImageGrab.grab()
    p.save(sourcename)

def fromTemplate(tmp):
    getCapture(src(tmp))
    matching(src(tmp), tmp, res(tmp))




def clean(s):
    os.remove(s)
    os.remove(src(s))
    os.remove(res_(s))
    pass