# -*- coding: utf-8 -*-
import numpy as np
import cv2
import datetime
from time import sleep
import os
import shutil
from glob import glob

cap = cv2.VideoCapture(0)
num = 0

while(True):
    d = datetime.datetime.now().strftime('%Y%m%d%H%M%S') # 現在時刻
    print(str(d))
    sleep(10)
    ret, frame = cap.read()
    num += 1
    path = "C:\\Users\\Kosuke\\Desktop\\proken\\procon\\"
    if num == 5:
        filelist = glob("*.jpg")
        for x in filelist:   
            os.remove(x)
        num -=5
    
    cv2.imwrite(path + d + ".jpg",frame)
    

#　https://www.with-test.tk サーバーネーム　
