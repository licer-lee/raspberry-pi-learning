# _*_ coding: utf-8 _*_
import time


try:
    while(True):
        # open file
        file = open("/sys/class/thermal/thermal_zone0/temp")

        temp = float(file.read()) / 1000
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        print("The CPU temp: %.3f "%temp)
        print("-------------------------")
        # close file
        file.close()
        
        time.sleep(10)

except KeyboardInterrupt:
    pass

