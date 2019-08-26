# coding: utf-8
import time
import RPi.GPIO as GPIO
from camera import Camera
from cloud_processor import CloudProcessor
from rgb import RGBLed
from sound import SoundProcessor

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGECHO = 15


camera = Camera()
cloud_processor = CloudProcessor()
led = RGBLed()


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


led.set_color(0, 0, 0)
hint_closer_triggered = False

try:
    while True:
        distance = measure()
#        print(distance)
        if (distance < 35):
            led.set_color(0, 1, 0)
            SoundProcessor.getInstance().play("./mp3/keep_it_still.mp3", True)
            camera.take_photo()
            led.set_color(1, 0, 0)
            SoundProcessor.getInstance().play("./mp3/done_have_to_think.mp3", True)
            cloud_processor.process_photo()
        else:
            led.set_color(0, 0, 1)
            if (distance < 70):
                if (not hint_closer_triggered):
                    print(SoundProcessor.getInstance().done_playing())
                    SoundProcessor.getInstance().play("./mp3/close_please.mp3", False)
                    hint_closer_triggered = True
            else:
                hint_closer_triggered = False
        time.sleep(0.01)

except KeyboardInterrupt:
    print("Stop")
    GPIO.cleanup()
