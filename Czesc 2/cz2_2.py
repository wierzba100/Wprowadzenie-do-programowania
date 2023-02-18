#!/usr/bin/python3
#
#2. Funkcja get_key(), zwracająca informację o numerze naciskanego przycisku (0-3).
#Jeżeli żaden przycisk nie jest naciśniety lub jeżeli naciśniety jest więcej niż jeden przycisk funkcja powinna zwracać
#wartość ‘-1’.
#Test 1: Program wyświetlający numer naciśnietego przycisku.
#Test 2: Test z punktu 1. 

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


try:
    open()
    while(True):
        key = get_key()
        if key != -1:
            print("Nacisnieto przycisk",key)
        set_point(key)
       
finally:
    close()