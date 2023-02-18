#!/usr/bin/python3
#
#4. Zmodyfikować program tak aby na przemian zapalał diody pierwszą i ostania oraz dwie środkowe (1001/0110) 

from board_driver_simulator import  open, close, but, pot, det, led # Simulator
import time

try:
	open()
#---------------------    
	while(True):
		led(9)
		time.sleep(0.25)
		led(6)
		time.sleep(0.25)
#---------------------
finally:
	close() 
