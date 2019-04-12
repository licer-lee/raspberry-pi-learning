# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

# use BCM mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

for x in range(3):
    GPIO.output(14, True)
    time.sleep(1)
    GPIO.output(14, False)
    time.sleep(1)
    
GPIO.cleanup()