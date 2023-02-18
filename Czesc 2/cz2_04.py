#!/usr/bin/python3
#
#4. Modyfikacja funkcji step pozwalająca na określenie kierunku przesunięcia: 
#Test 1: Program: obracający krążkiem w lewo jeżeli naciśnieto przycisk ‘0’ a w prawo jeśli naciśnieto przycisk ‘1’ 

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
def step(kierunek):
    global licznik
    if kierunek == 'right':
        licznik = licznik + 1
    if kierunek == 'left':
        licznik = licznik - 1
    licznik = licznik % 4

try:
    open()
    while(True):
        if get_key() == 0:
            step('left')
            set_point(licznik)
        elif get_key() == 1:
            step('right')
            set_point(licznik)
        set_point(licznik)
        time.sleep(0.25)
       
finally:
    close()