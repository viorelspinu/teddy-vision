# coding: utf-8
import time
import RPi.GPIO as GPIO
from camera import Camera
from cloud_processor import CloudProcessor

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGECHO = 15


# Set pins as output and input
GPIO.setup(GPIO_TRIGECHO, GPIO.OUT)  # Initial state as output

# Set trigger to False (Low)
GPIO.output(GPIO_TRIGECHO, False)

camera = Camera()
cloud_processor = CloudProcessor()


def measure():
  # This function measures a distance
  # Pulse the trigger/echo line to initiate a measurement
    GPIO.output(GPIO_TRIGECHO, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGECHO, False)
  # ensure start time is set in case of very quick return
    start = time.time()

  # set line to input to check for start of echo response
    GPIO.setup(GPIO_TRIGECHO, GPIO.IN)
    while GPIO.input(GPIO_TRIGECHO) == 0:
        start = time.time()

  # Wait for end of echo response
    while GPIO.input(GPIO_TRIGECHO) == 1:
        stop = time.time()

    GPIO.setup(GPIO_TRIGECHO, GPIO.OUT)
    GPIO.output(GPIO_TRIGECHO, False)

    elapsed = stop-start
    distance = (elapsed * 34300)/2.0
    time.sleep(0.1)
    return distance

try:

    while True:
        distance = measure()
        #print "  Distance : %.1f cm" % distance
        if (distance < 25):
            camera.take_photo()
            cloud_processor.process_photo()
        time.sleep(0.01)

except KeyboardInterrupt:
    print("Stop")
    GPIO.cleanup()
