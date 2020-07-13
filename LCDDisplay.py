#!/usr/bin/python
#-*-coding: UTF-8 -*
import lcddriver
import alsaaudio
import time
import RPi.GPIO as GPIO
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 23
GPIO_ECHO = 24

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

GPIO.output(GPIO_TRIGGER, False)

display = lcddriver.lcd()
display.lcd_clear()

first_launch = True

try:
	def display_distance():
		int_distance = int(distance())
		if int_distance < 101:
			display.lcd_clear()
	        	long_string(display, 'Recomm vol: ' + str(int_distance), 2)
                	long_string(display, 'Current vol: ' + str(alsaaudio.Mixer().getvolume()[0]), 1)
		elif first_launch:
			long_string(display, 'Recomm vol: ' + str(100), 2)
			long_string(display, 'Current vol: ' + str(alsaaudio.Mixer().getvolume()[0]), 1)

	def display_song_info():
		long_string(display, sys.argv[2].encode('utf-8', 'ignore').decode('utf-8'), 2)
		long_string(display, sys.argv[1].encode('utf-8', 'ignore').decode('utf-8'), 1)

	def distance():
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


	def long_string(display, text = '', num_line = 1, num_cols = 16):
		if(len(text) > num_cols):
			display.lcd_display_string(text[:num_cols],num_line)
			time.sleep(1)
			for i in range(len(text) - num_cols + 1):
				text_to_print = text[i:i+num_cols]
				display.lcd_display_string(text_to_print,num_line)
				time.sleep(0.2)
			time.sleep(1)
		else:
			display.lcd_display_string(text,num_line)

	while True:
		if len(sys.argv) == 4:
			display_distance()
		else:
			display_song_info()
		first_launch = False
		time.sleep(1)

except KeyboardInterrupt:
	print("Cleaning up!")
	display.lcd_clear()


