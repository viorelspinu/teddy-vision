import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)


while (True):
    print "LED on"
    GPIO.output(18,random.randint(0,1))
    GPIO.output(23,random.randint(0,1))
    GPIO.output(24,random.randint(0,1))
    time.sleep(1)
print "LED off"
GPIO.output(18,GPIO.LOW)
GPIO.output(23,GPIO.LOW)
GPIO.output(24,GPIO.LOW)