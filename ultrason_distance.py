import RPi.GPIO as GPIO
import time
import alsaaudio

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 23
GPIO_ECHO = 24

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

GPIO.output(GPIO_TRIGGER, False)

def distance():
	#GPIO.output(GPIO_TRIGGER, False)
	#time.sleep(2)

	GPIO.output(GPIO_TRIGGER, True)
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER, False)

	startTime = time.time()
	stopTime = time.time()
		
	while GPIO.input(GPIO_ECHO) == 0:
		startTime == time.time()

	while GPIO.input(GPIO_ECHO) == 1:
		stopTime = time.time()
	
	timeElapsed = stopTime - startTime
	
	distance = round((stopTime - startTime) * 340 * 100 / 2, 1) 

	return distance

if __name__ == '__main__':
	try:
		while True:
			#m = alsaaudio.Mixer()
			#current_volume = m.getvolume()
			#print "Voluem", current_volume
			dist = distance()
			if(dist < 100):
				print("Distance : %.1f cm" % dist)
			time.sleep(1)
	except KeyboardInterrupt:
		print("Fini de jouer")
		GPIO.cleanup()
