import RPi.GPIO as GPIO
import time
import os

button_minus = 37
button_plus = 35

def setup():
       GPIO.setmode(GPIO.BOARD)
       GPIO.setup(button_plus, GPIO.IN, pull_up_down=GPIO.PUD_UP)
       GPIO.setup(button_minus, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def loop():
        while True:
              button_minus_state = GPIO.input(button_minus)
	      button_plus_state = GPIO.input(button_plus)
              if button_minus_state == False:
		  os.system('amixer set Master 5%-')
                  while GPIO.input(button_minus) == False:
                    time.sleep(0.2)
	      if button_plus_state == False:
                  os.system('amixer set Master 5%+')
                  while GPIO.input(button_minus) == False:
                    time.sleep(0.2)


def endprogram():
         GPIO.cleanup()


if __name__ == '__main__':

          setup()

          try:
                 loop()

          except KeyboardInterrupt:
                 print 'keyboard interrupt detected' 
                 endprogram()
