#!/usr/bin/python3
#
#4. Zmodyfikować funkcję get_detector tak aby korzystała z portu wejściowego.
#Test: Dodać do testu z zadania 2 funkcjonalność polegającą na wyświetlanie na ekranie napisu „bingo!” w momencie
#zrównania się markera z detektorem. 

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

def get_detector():
    x = get_port()
    maska = 1 << 30
    x =x & maska
    if x:
        return 'active'

try:
    open()
    while(True):
        set_point(0)
        print(get_detector())
        time.sleep(0.25)
        set_point(1)
        print(get_detector())
        time.sleep(0.25)
        set_point(2)
        print(get_detector())
        time.sleep(0.25)
        set_point(3)
        print(get_detector())
        time.sleep(0.25)


finally:
    close()