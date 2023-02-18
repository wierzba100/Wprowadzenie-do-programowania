#!/usr/bin/python3
#
#1. Napisać program który będzie cyklicznie przesuwał punkt świetlny (0,1,2,3,0,1,…) co ok. ¼ sekundy. 

from board_driver_simulator import  open, close, but, pot, det, led, set_port, get_port # Simulator
import time
from my_board import step_prawo, get_key, licznik, set_point, get_detector, step_lewo

try:
    open()
    while(True):
        set_port(1<<13)
        time.sleep(0.25)
        set_port(1<<5)
        time.sleep(0.25)
        set_port(1<<9)
        time.sleep(0.25)
        set_port(1<<17)
        time.sleep(0.25)


finally:
    close()