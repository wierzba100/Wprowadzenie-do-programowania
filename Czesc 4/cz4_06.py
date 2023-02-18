#!/usr/bin/python3
#
#6. Napisać funkcję get_pot działającą tak samo jak funkcja pot ale korzystającą z portu wejściowego.
#Test: Program wyświetlający na ekranie stan potencjometru w kodzie binarnym a następnie dziesiętnym. Działanie
#programów sprawdzić obracając potencjometrem. 

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

def get_pot():
    x = get_port()
    x = x & 1023
    return x

try:
    open()
    while(True):
        print(bin(get_pot()), ' ', get_pot())

finally:
    close()