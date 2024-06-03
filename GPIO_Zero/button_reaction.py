from gpiozero import LED, Button
from time import sleep, time
import random

T1 = Button(23, pull_up=False)
T2 = Button(24, pull_up=False)
LED = LED(22)

while True:
    LED.on()
    print('Start!')
    sleep(random.uniform(3, 8))
    LED.off()
    start = time()
    if T1.is_pressed:
        end = time()
        print('T1 win time: {end - start}s!')
    elif T2.is_pressed:
        end = time()
        print(f'T2 win time: {end - start}s!')

