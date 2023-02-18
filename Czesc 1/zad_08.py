#!/usr/bin/python3
#
#8. Zmodyfikować program tak aby wyświetlał stan przycisków w postaci binarnej a następnie heksadecymalnej 

from board_driver_simulator import  open, close, but, pot, det, led # Simulator
import time

try:
	open()
#---------------------    
	while(True):
		state = but()
		print (state,bin(state),hex(state))
#---------------------
finally:
	close() 
