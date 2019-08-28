from camera import Camera
from sound_processor import SoundProcessor
from cloud_processor import CloudProcessor
from rgb import RGBLed
from sonar import Sonar
import time
import RPi.GPIO as GPIO

sonar = Sonar.getInstance()
camera = Camera()
cloud_processor = CloudProcessor()
led = RGBLed()

led.set_color(0, 0, 0)
hint_closer_triggered = False

try:
    while True:
        distance = Sonar.getInstance().measure()
        print(distance)
        if (distance < 35):
            led.set_color(0, 1, 0)
            SoundProcessor.getInstance().play("./wav/keep_it_still.wav", True)
            camera.take_photo()
            led.set_color(1, 0, 0)
            SoundProcessor.getInstance().play("./wav/done_have_to_think.wav", True)
            cloud_processor.process_photo()
        else:
            led.set_color(0, 0, 1)
            if (distance < 70):
                if (not hint_closer_triggered):
                    print(SoundProcessor.getInstance().done_playing())
                    SoundProcessor.getInstance().play("./wav/close_please.wav", False)
                    hint_closer_triggered = True
            else:
                hint_closer_triggered = False
        time.sleep(0.01)

except KeyboardInterrupt:
    print("Stop")
    GPIO.cleanup()
