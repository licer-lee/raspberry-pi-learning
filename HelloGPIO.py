# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

print('GPIO version is:', GPIO.VERSION)

# GPIO mode: BOARD / BCM
GPIO.setmode(GPIO.BOARD)
mode = GPIO.getmode()
print("GPIO mode is:", mode)

# set channel in/out mode: GPIO.IN/GPIO.OUT
GPIO.setup(11, GPIO.IN)
GPIO.setup(12, GPIO.OUT)
# set default value
GPIO.setup(13, GPIO.OUT, initial=GPIO.HIGH)

# output
channel_12 = GPIO.output(12, 1)
print("channel_12:", channel_12)

# input
channel_11_value = GPIO.input(11)
print("channel_11_value:",channel_11_value)

# release
GPIO.cleanup()

