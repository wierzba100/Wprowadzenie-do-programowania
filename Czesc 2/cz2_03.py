#!/usr/bin/python3
#
#3. Funkcja step() przesuwająca punkt świetlny o jeden ‘w górę’

from board_driver_simulator import  open, close, but, pot, det, led # Simulator
import time

def get_key():
    position = but()
    if position == 1:
        return 0
    elif position == 2:
        return 1
    elif position == 4:
        return 2
    elif position == 8:
        return 3

    return -1

def set_point(position):
    if position == 0:
        led(1)
    elif position == 1:
        led(2)
    elif position == 2:
        led(4)
    elif position == 3:
        led(8)
    else:
        led(0)

licznik = 0
def step():
    global licznik
    licznik = licznik + 1
    licznik = licznik % 4

try:
    open()
    while(True):
        step()
        set_point(licznik)
        time.sleep(0.25)
       
finally:
    close()