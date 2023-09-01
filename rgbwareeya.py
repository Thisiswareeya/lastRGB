from machine import Pin
import time

p1 = Pin(2, Pin.OUT) #ประกาศขา led 
p2 = Pin(3, Pin.OUT)
p3 = Pin(4, Pin.OUT)
bt1 = Pin(6, Pin.IN, Pin.PULL_UP) #ประกาศขา button
bt2 = Pin(7, Pin.IN, Pin.PULL_UP)
bt3 = Pin(8, Pin.IN, Pin.PULL_UP)

while True:
    bts = bt1.value()  #สร้างตัวแปรมาเพื่อเก็บตัวแปร Value ของปุ่ม
    bts2 = bt2.value()
    bts3 = bt3.value()
    
    if bts == 0:   
        print("R")
        p1.value(1)
        p2.value(0)
        p3.value(0)
    elif bts2 == 0:
        print("G")
        p1.value(0)
        p2.value(1)
        p3.value(0)
    elif bts3 == 0:
        print("Y")
        p1.value(0)
        p2.value(0)
        p3.value(1)
    else:
        p1.value(0)
        p2.value(0)
        p3.value(0)

    time.sleep(0.1)
    # Add a small delay to avoid rapid button presses