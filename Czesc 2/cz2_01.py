#!/usr/bin/python3
#
#1. Napisać funkcję set_point(position), która zaświeci diodę świecącą o zadanej pozycji (od 0 do 3).
#Pozostałe diody powinny być zgaszone.
#Podanie argumentu z poza zakresu 0-3 powinno skutkować zgaszeniem wszystkich diod.
#Użyć sekwencji if,elif,elif.. 

from board_driver_simulator import  open, close, but, pot, det, led # Simulator
import time

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

try:
	open()
#---------------------    
	while(True):
		x = but()
		if x == 1:
			set_point(0)
		elif x == 2:
			set_point(1)
		elif x == 4:
			set_point(2)
		elif x == 8:
			set_point(3)
		else:
			set_point(6)		


#---------------------
finally:
	close() 
