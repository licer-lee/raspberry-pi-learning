# _*_ coding: utf-8 _*_
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

fengshan_id = 3
#fengshan2_id = 4

GPIO.setup(fengshan_id, GPIO.IN)
#GPIO.setup(fengshan2_id, GPIO.OUT)
try:
    
    fengshan_val = GPIO.input(fengshan_id)
    print("fengshan_id: %s" %fengshan_val)
    
    #GPIO.output(fengshan2_id, GPIO.LOW)
    #fengshan2_val = GPIO.input(fengshan2_id)
    #print("fengshan2_val: %s" %fengshan2_val)

except ValueError:
    print("catch the ex")
finally:
    GPIO.cleanup()
