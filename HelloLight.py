# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11, GPIO.OUT)

while True:
    GPIO.output(11, True)
    print("the light on")
    time.sleep(1)
    GPIO.output(11, False)
    print("the light off")
    time.sleep(1)
    
GPIO.cleanup()