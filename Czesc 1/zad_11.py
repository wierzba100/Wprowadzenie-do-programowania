#!/usr/bin/python3
#
#11. Program z poprzedniego punktu stosunkowo wolno reaguje na przyciski. Przyczyną jest stosunkowo długi czas
#wykonania funkcji but(). Zmodyfikować program tak aby wywoływał funkcję but() tylko raz na jeden obrót pętli. Jak
#modyfikacja skróciła reakcji programu na naciśnięcie przycisku? 

from board_driver_simulator import  open, close, but, pot, det, led # Simulator
import time

try:
	open()
#---------------------    
	while(True):
		if but() == 0:
			led(0)
		elif but() == 1:
			led(8)
		elif but() == 2:
			led(12)
		elif but() == 4:
			led(14)
		elif but() == 8:
			led(15)
#---------------------
finally:
	close() 
