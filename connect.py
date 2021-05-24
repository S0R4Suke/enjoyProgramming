# -*- coding: utf-8 -*-
import serial
import time
def send():
	ser = serial.Serial('/dev/ttyACM0', 9600)
	time.sleep(2)
	ser.write(b'A')
	ser.close()

def rec():
    ser = serial.Serial('/dev/ttyACM0', 9600)
    time.sleep(2)
    t0 = time.time()
    while time.time() - t0 < 5:
        # シリアル通信でデータを受信
        str = ser.read(1)
        print(str.decode())
        # 読み込んだデータの表示

send()
rec()
