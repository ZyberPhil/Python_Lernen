from gpiozero import LED, Button
from time import sleep, time

T1 = Button(23, pull_up=False)
T2 = Button(24, pull_up=False)

countT1 = 0
countT2 = 0

print('Lost gehts!')
start_time = time()
while time()-start_time < 10:
    if T1.is_pressed:
        countT1 += 1
        print('+1')
        while T1.is_pressed:
            sleep(0.01)
    elif T2.is_pressed:
        countT2 += 1
        print('+1')
        while T2.is_pressed:
            sleep(0.01)

print(f'Taster 1 wurde {countT1} mal gedrückt')
print(f'Taster 2 wurde {countT2} mal gedrückt')
