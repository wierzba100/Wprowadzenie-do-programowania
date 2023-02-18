#!/usr/bin/python3
#
#13. Program pozwalający na ustawianie potencjometrem pozycji punktu świetlnego. Wykorzystać cały zakres
#potencjometru. 

from board_driver_simulator import  open, close, but, pot, det, led # Simulator
import time

try:
	open()
#---------------------    
	while(True):
		state = pot()
		if state<250:
			led(0x1)
		elif state<500:
			led(0x2)
		elif state<750:
			led(0x4)
		else:
			led(0x8)
		
#---------------------
finally:
	close() 
