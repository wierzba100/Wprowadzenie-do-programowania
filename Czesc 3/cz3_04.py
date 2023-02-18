#!/usr/bin/python3
#
#Zmodyfikować funkcję wait_for_key() tak aby dodatkowo zwracała numer naciśnietego przycisku.
#Test: Program obracający tarczą po każdym naciśnięciu przycisku. Kierunek obrotu i liczba kroków zależna od
#naciśniętego przycisku w sposób nast.: 

from board_driver_simulator import  open, close, but, pot, det, led # Simulator
import time
from my_board import step_prawo, get_key, licznik, set_point, get_detector, step_lewo, steps

x = licznik

def wait_for_key2(x):
    if x != 0:
        if x == 1:
            return 0
        elif x == 2:
            return 1
        elif x == 4:
            return 2
        else:
            return 3
    else:
        return -1



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
