#!/usr/bin/env python3
#-- coding: utf-8 --

import RPi.GPIO as GPIO #Importe la bibliothèque pour contrôler les GPIOs

GPIO.setmode(GPIO.BOARD) #Définit le mode de numérotation (Board)
GPIO.setwarnings(False) #On désactive les messages d'alerte

LED_RED = 38 #Définit le numéro du port GPIO qui alimente la led
LED_GREEN = 40

GPIO.setup(LED_GREEN, GPIO.OUT) #Active le contrôle du GPIO
GPIO.setup(LED_RED, GPIO.OUT)

GPIO.output(LED_GREEN, GPIO.HIGH)
GPIO.output(LED_RED, GPIO.LOW)
