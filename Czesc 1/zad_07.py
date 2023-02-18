#!/usr/bin/python3
#
#7. Program wyświetlający na ekranie stan przycisków (w postaci dziesiętnej). Działanie programu sprawdzić naciskając
#przycisk 0 potem 3 a następnie jednocześnie 0 i 3. 


from board_driver_simulator import  open, close, but, pot, det, led # Simulator
import time

try:
	open()
#---------------------    
	while(True):
		state = but()
		print(state)
#---------------------
finally:
	close() 
