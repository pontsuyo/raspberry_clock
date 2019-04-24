import RPi.GPIO as GPIO
from datetime import datetime
import time

# table of numbers and 7 segments LED
num2lights = {
    0 : [1, 1, 1, 1, 1, 1, 0],
    1 : [0, 1, 1, 0, 0, 0, 0],
    2 : [1, 1, 0, 1, 1, 0, 1],
    3 : [1, 1, 1, 1, 0, 0, 1],
    4 : [0, 1, 1, 0, 0, 1, 1],
    5 : [1, 0, 1, 1, 0, 1, 1],
    6 : [0, 0, 1, 1, 1, 1, 1],
    7 : [1, 1, 1, 0, 0, 0, 0],
    8 : [1, 1, 1, 1, 1, 1, 1],
    9 : [1, 1, 1, 0, 0, 1, 1]
}

# used GPIOs 
pins = [
    #a, b, c, d,  e,  f,  g,  DP
     3, 5, 7, 11, 13, 15, 19, 21]
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT) # pin3
for x in range(5):
    GPIO.output(2, 1)
    time.sleep(1)
    GPIO.output(2,0)
    time.sleep(0.2)
GPIO.cleanup()

