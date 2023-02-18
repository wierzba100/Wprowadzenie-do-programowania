#!/usr/bin/python3
#
#Funkcja wait_for_key() oczekująca na naciśniecie dowolnego przycisku.
#Test 1: Jakiś program z funkcją print
#Test 2: Program obracający tarczę o 12 kroków w prawo po każdym naciśnięciu dowolnego przycisku. 

from board_driver_simulator import  open, close, but, pot, det, led # Simulator
import time
from my_board import step_prawo, get_key, licznik, set_point, get_detector

x = licznik

def wait_for_key():
    if but() != 0:
        return True
    else:
        return False

try:
    open()
    while(True):

        #if(wait_for_key()):
        #    print("Naciskasz teraz przycisk") #test1

        if(wait_for_key()):
            i = 0
            while(i < 12):        #test2
                print("weszlo")
                x = step_prawo(x)
                set_point(x)
                i=i + 1


finally:
    close()
