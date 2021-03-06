#!/usr/bin/python
# coding: utf-8

# モジュールをインポートする
import RPi.GPIO as GPIO
import time
import os

PIN_1 = 6
PIN_2 = 13
PIN_3 = 19
PIN_4 = 26
PIN_5 = 16
PIN_6 = 20
PIN_7 = 21
PIN_END = 18


# GPIO指定をGPIO番号で行う
GPIO.setmode(GPIO.BCM)


GPIO.setup(PIN_1, GPIO.IN)
GPIO.setup(PIN_2, GPIO.IN)
GPIO.setup(PIN_3, GPIO.IN)
GPIO.setup(PIN_4, GPIO.IN)
GPIO.setup(PIN_5, GPIO.IN)
GPIO.setup(PIN_6, GPIO.IN)
GPIO.setup(PIN_7, GPIO.IN)

# 終了
GPIO.setup(PIN_END, GPIO.IN)

btn1 = 0
btn2 = 0
btn3 = 0
btn4 = 0
btn5 = 0
btn6 = 0
btn7 = 0

while 1 :
        if GPIO.input(PIN_END):
                break;
        
        # ド
        if GPIO.input(PIN_1) == 0 :
                if btn1 == 0 :
                        btn1 = 1
                        print "DO"
                        os.system("paplay do.wav &")
        else:
                btn1 = 0

		# レ
        if GPIO.input(PIN_2) == 0:
                if btn2 == 0 :
                        btn2 = 1
                        print "RE"
                        os.system("paplay re.wav &")
        else:
                btn2 = 0

		# ミ
        if GPIO.input(PIN_3) == 0:
                if btn3 == 0 :
                        btn3 = 1
                        print "MI"
                        os.system("paplay mi.wav &")
        else:
                btn3 = 0

		# ファ
        if GPIO.input(PIN_4) == 0:
                if btn4 == 0 :
                        btn4 = 1
                        print "FA"
                        os.system("paplay fa.wav &")
        else:
                btn4 = 0

		# ソ
        if GPIO.input(PIN_5) == 0:
                if btn5 == 0 :
                        btn5 = 1
                        print "SO"
                        os.system("paplay so.wav &")
        else:
                btn5 = 0

		# ラ
        if GPIO.input(PIN_6) == 0:
                if btn6 == 0 :
                        btn6 = 1
                        print "RA"
                        os.system("paplay ra.wav &")
        else:
                btn6 = 0
                
        # GERO
        if GPIO.input(PIN_7) == 0:
                if btn7 == 0 :
                        btn7 = 1
                        print "GERO"
                        os.system("paplay gero_se.wav &")
        else:
                btn7 = 0



# GPIOピンをリセット
GPIO.cleanup()

