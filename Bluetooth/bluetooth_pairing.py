#!usr/bin/env python

from gpiozero import Button
import time
import os

button = Button(18, hold_time=2)

def super_print():
	os.system('python led_pairing.py')
	os.system('sh BT_script.sh &')

def loop():
	button.when_released = super_print

def endprogram():
         GPIO.cleanup()


if __name__ == '__main__':

          try:
                 loop()
		 while True:
		 	button.wait_for_release()

          except KeyboardInterrupt:
                 print 'keyboard interrupt detected' 
                 endprogram()
