import RPi.GPIO as GPIO
import time
import random


class RGBLedService:
    __instance = None

    @staticmethod
    def getInstance():
        if (RGBLedService.__instance == None):
            RGBLedService()
        return RGBLedService.__instance

    def __init__(self):
        RGBLedService.__instance = self        
        self.GPIO_TRIGECHO = 15
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(25, GPIO.OUT)
        GPIO.setup(23, GPIO.OUT)
        GPIO.setup(24, GPIO.OUT)

    def set_color(self, r, g, b):
        GPIO.output(23, r)
        GPIO.output(24, g)
        GPIO.output(25, b)
