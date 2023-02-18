#!/usr/bin/python3
#
#2. Zmodyfikować program 1 tak aby na przemian zapalał diodę 0 i 1 (01,10,01…), i zapisać jako nowy program

from board_driver_simulator import  open, close, but, pot, det, led # Simulator
import time

try:
	open()
#---------------------    
	while(True):
		led(1)
		led(2)
#---------------------
finally:
	close() 

