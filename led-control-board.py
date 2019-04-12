# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

# use GPIO board mode
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)

for x in range(3):
    GPIO.output(8, True)
    time.sleep(1)
    GPIO.output(8, False)
    time.sleep(1)
    
GPIO.cleanup()