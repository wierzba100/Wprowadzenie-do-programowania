#!/usr/bin/python3
#
#2. Zmodyfikować funkcję set_point tak aby korzystała z portu wyjściowego. Użyć przesunięcia bitowego.
#Test: Funkcjonalność z poprzedniego zadania. 

from board_driver_simulator import  open, close, but, pot, det, led, set_port, get_port # Simulator
import time

def set_point(x):
    if x == 0:
        set_port(1<<13)
    elif x == 1:
        set_port(1<<5)
    elif x == 2:
        set_port(1<<9)
    elif x == 3:
        set_port(1<<17)
    else:
        set_port(0x0)

try:
    open()
    while(True):
        set_point(0)
        time.sleep(0.25)
        set_point(1)
        time.sleep(0.25)
        set_point(2)
        time.sleep(0.25)
        set_point(3)
        time.sleep(0.25)


finally:
    close()