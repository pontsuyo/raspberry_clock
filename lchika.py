import RPi.GPIO as GPIO
from datetime import datetime
import time

GPIO.setmode(GPIO.BOARD) 
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
    9 : [1, 1, 1, 1, 0, 1, 1]
}

# used GPIOs 
pins = [
    #a, b, c, d,  e,  f,  g,  DP
     15, 13, 7, 5, 3, 19, 21, 11
     ]

# make int separate
def separate_digits(n):
    n1 = int(n/10)
    n2 = n - n1 * 10
    return (n1, n2)

# ==== retrieve time ===
time_now = datetime.now().time()
h = time_now.hour
m = time_now.minute
s = time_now.second

s1, s2 = separate_digits(s)

# === only SECOND version ===
GPIO.setup(pins, GPIO.OUT)

def show_num(no):  
    ns = num2lights[no] 
    for i, n in enumerate(ns): 
        n = 1 if n == 0 else 0 
        GPIO.output(pins[i], n)

for i in range(0, 10): 
    print(i) 
    show_num(i)
    time.sleep(1) 

GPIO.cleanup()