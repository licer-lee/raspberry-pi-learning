# _*_ coding: utf-8 _*_
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

try:
    for num in range(30, 40):
        # the operation danger, cause the host death 
        #GPIO.setup(num, GPIO.IN)
        #val = GPIO.input(num)
        #print("GPIO port value: %s" %val)    
        print("number %d" %num)

# catch interrupt
except KeyboardInterrupt:
    pass

# cleanup
GPIO.cleanup()