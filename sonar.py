# coding: utf-8
import time
import RPi.GPIO as GPIO
from camera import Camera
from cloud_processor import CloudProcessor
import random

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGECHO = 15


camera = Camera()
cloud_processor = CloudProcessor()


def measure():
    start = time.time()

  # set line to input to check for start of echo response
    GPIO.setup(GPIO_TRIGECHO, GPIO.IN)
    while GPIO.input(GPIO_TRIGECHO) == 0:
        start = time.time()

  # Wait for end of echo response
    while GPIO.input(GPIO_TRIGECHO) == 1:
        stop = time.time()

    elapsed = stop-start
    distance = (elapsed * 34300)/2.0
    time.sleep(0.1)
    return distance

try:
    while True:
        distance = measure()
        print(distance)
        if (distance < 35):
            camera.take_photo()
            cloud_processor.process_photo()
        time.sleep(0.01)

except KeyboardInterrupt:
    print("Stop")
    GPIO.cleanup()
