#!/usr/bin/python3
#
#3. Poniżej pokazano fragment kodu wyświetlający stan portu wejściowego w kodzie binarnym. Wstawić kod do
#programu. Przy użyciu programu zweryfikować przyporządkowanie peryferiów do bitów portu wejściowego (rysunek
#we wprowadzeniu). 

from board_driver_simulator import  open, close, but, pot, det, led, set_port, get_port # Simulator
import time

def set_point(x):
    if x == 0:
        set_port(1<<13)
    elif x == 1:
        set_port(1<<5)
    elif x == 2:
        set_port(1<<9)
    elif x == 3:
        set_port(1<<17)
    else:
        set_port(0x0)

try:
    open()
    while(True):
        port_state=get_port()
        print(f"{port_state:032b}") # wyświetla wszystkie 32 bity zmiennej port_state

finally:
    close()