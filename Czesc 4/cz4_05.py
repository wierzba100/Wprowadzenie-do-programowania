#!/usr/bin/python3
#
#5. Zmodyfikować funkcję get_key tak aby korzystała z portu wejściowego. W funkcji powinno znajdować się tyko jedno
#wywołanie funkcji get_port. Funkcja powinna używać przesunięcia binarnego.
#Test: Program zapalający diodę odpowiadającą naciśnietemu przyciskowi. 

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

def get_key():
    position = get_port()
    if position == (1<<18):
        return 0
    elif position == (1<<12):
        return 1
    elif position == (1<<15):
        return 2
    elif position == (1<<20):
        return 3

try:
    open()
    while(True):
        if get_key() == 0:
            led(1)
        elif get_key() == 1:
            led(2)
        elif get_key() == 2:
            led(4)
        elif get_key() == 3:
            led(8)
        else:
            led(0)


finally:
    close()