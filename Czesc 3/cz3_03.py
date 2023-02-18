#!/usr/bin/python3
#
#Funkcja steps, pozwalająca na określenie liczby kroków do wykonania. 

from board_driver_simulator import  open, close, but, pot, det, led # Simulator
import time
from my_board import step_prawo, get_key, licznik, set_point, get_detector, step_lewo

x = licznik

def steps(kierunek, n):
    i=0
    global x
    if kierunek == 'right':
        while i < n:
            x = step_prawo(x)
            set_point(x)
            i=i+1
    elif kierunek == 'left':
        while i < n:
            x = step_lewo(x)
            set_point(x)
            i=i+1
    else:
        print("Blad")



try:
    open()
    while(True):
        steps('right',6); time.sleep(0.5)
        steps('right',12); time.sleep(0.5)
        steps('right',12); time.sleep(0.5)
        steps('right',6); time.sleep(0.5) 


finally:
    close()
