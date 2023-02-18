#!/usr/bin/python3
#
#10. Program zapalający pasek diod. Długość paska zależna od naciśnietego przycisku (But0->1000, But1->1100, But2-
#>1110, But3->1111). Jeżeli nie będzie naciśnięty żaden przycisk wszystkie diody powinny być zgaszone. Użyć zapisu
#heksadecymalnego. W instrukcji warunkowej użyć wywołania funkcji but() (5 razy)

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
