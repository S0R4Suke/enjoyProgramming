# -*- coding: utf-8 -*-
import numpy as np
import cv2
import datetime
from time import sleep

cap = cv2.VideoCapture(0)
while(True):
    sleep(10)
    d = datetime.datetime.now().strftime('%Y%m%d%H%M%S') # 現在時刻
    print(str(d))
        # フレームをキャプチャする
    ret, frame = cap.read()

        # 画面に表示する
    #cv2.imshow('frame',frame)

        # キーボード入力待ち
        #key = cv2.waitKey(1) & 0xFF

        # qが押された場合は終了する
        #if key == ord('q'):
            #break
        # sが押された場合は保存する
        #if key == ord('s'):
    path = "C:\\Users\\Kosuke\\Desktop\\proken\\procon\\"
    cv2.imwrite(path + str(d) + ".jpg",frame)
        #break
    # キャプチャの後始末と，ウィンドウをすべて消す
    #cap.release()
    #cv2.destroyAllWindows()