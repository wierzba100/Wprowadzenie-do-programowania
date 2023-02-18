#!/usr/bin/python3
#
#6. Zmodyfikować program tak aby korzystał z zapisu heksadecymalnego 

from board_driver_simulator import  open, close, but, pot, det, led # Simulator
import time

try:
	open()
#---------------------    
	while(True):
		led(0x9)
		time.sleep(0.25)
		led(0x6)
		time.sleep(0.25)
#---------------------
finally:
	close() 
