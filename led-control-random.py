# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import random
import time

# use GPIO board mode
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)

for x in range(30):
#    t = random.randint(0,1)
    t = random.random()
    print(t)
    GPIO.output(8, True)
    time.sleep(t)
    
    t = random.random()
    print(t)
    GPIO.output(8, False)
    time.sleep(t)
    
GPIO.cleanup()
