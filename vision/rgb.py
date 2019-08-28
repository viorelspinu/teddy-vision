import RPi.GPIO as GPIO
import time
import random


class RGBLed:

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(23, GPIO.OUT)
        GPIO.setup(24, GPIO.OUT)

    def set_color(self, r, g, b):      
        GPIO.output(23, r)
        GPIO.output(24, g)
        GPIO.output(18, b)
        