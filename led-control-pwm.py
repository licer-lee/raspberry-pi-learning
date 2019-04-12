#!/usr/bin/env python
# encoding: utf-8

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)

pwm = GPIO.PWM(8, 80)

pwm.start(0)


try:
    while 1:
        for i in range(0,101,1):
            pwm.ChangeDutyCycle(i)
            time.sleep(.02)
            
        for i in range(100, -1, -1):
            pwm.ChangeDutyCycle(i)
            time.sleep(.02)
            
except KeyboardInterrupt:
    pass

pwm.stop()

GPIO.cleanup()