#!/usr/bin/python3
#
#Test 1: Cześć II, Zadanie 4, Test 1
#Test 2: Cześć II, Zadanie 5, Test 2 

from board_driver_simulator import  open, close, but, pot, det, led # Simulator
import time
from my_board import step_prawo, get_key, licznik, set_point, get_detector

x = licznik

try:
    open()
    while(True):
        #x = step_prawo(x) #test1
        #set_point(x)
        #time.sleep(0.25)

        x = step_prawo(x)
        set_point(x)        #test 2
        time.sleep(0.1)
        if get_detector() == 'active':
            break


finally:
    close()