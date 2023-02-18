#!/usr/bin/python3
#
#9. Program ‘zapalający’ diodę 2 (i tylko 2) tylko w momencie naciśnięcia przycisku 3 (w przeciwnym razie dioda ma być zgaszona). Pozostałe przyciski mają pozostać nieaktywne. 

from board_driver_simulator import  open, close, but, pot, det, led # Simulator
import time

try:
	open()
#---------------------    
	while(True):
		if but() == 8:
			led(2)
		else:
			led(0)
#---------------------
finally:
	close() 
