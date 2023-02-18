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

def step_prawo(licznik):
    licznik = licznik + 1
    return licznik % 4

def step_lewo(licznik):
    licznik = licznik - 1
    return licznik % 4

def get_detector():
    if det():
        return 'active'
    else:
        return 'no_active'

licznik = 0
x = licznik

def wait_for_key():
    if but() != 0:
        return True
    else:
        return False

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

