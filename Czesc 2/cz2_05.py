#!/usr/bin/python3
#
#5.Funkcja get_detector() zwracająca ‘active’, jeżeli marker na tarczy będzie znajdował się nad detektorem krańcowym
#oraz ‘no_active’ w przeciwnym przypadku. 


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

def get_detector():
    if det():
        return 'active'
    else:
        return 'no_active'


try:
    open()
    while(True):
        #step('right')
        #set_point(licznik)  #test 1
        #time.sleep(0.1)
        #print(get_detector())





        step('right')
        set_point(licznik) #test 2
        time.sleep(0.1)
        if get_detector() == 'active':
            break

       
finally:
    close()