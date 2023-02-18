#!/usr/bin/python3
#
#5. Zmodyfikować program tak aby korzystał z zapisu binarnego (argument funkcji „led”) 


from board_driver_simulator import  open, close, but, pot, det, led # Simulator
import time

try:
	open()
#---------------------    
	while(True):
		led(0b1001)
		time.sleep(0.25)
		led(0b0110)
		time.sleep(0.25)
#---------------------
finally:
	close() 
