#!/usr/bin/python3
#
#Wstawić zdefiniowane funkcje do modułu „my_board”.
#Test: Test z zad. 4. 

from board_driver_simulator import  open, close, but, pot, det, led
import time
from my_board import step_prawo, get_key, licznik, set_point, get_detector, step_lewo, steps, wait_for_key2

x = licznik

try:
    open()
    while(True):
        x = but()
        if wait_for_key2(x) == 0:
            steps('left',12); time.sleep(0.5)
        elif wait_for_key2(x) == 1:
            steps('left',3); time.sleep(0.5)
        elif wait_for_key2(x) == 2:
            steps('right',3); time.sleep(0.5)
        elif wait_for_key2(x) == 3:
            steps('right',12); time.sleep(0.5)


finally:
    close()
