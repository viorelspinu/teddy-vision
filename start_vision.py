from camera import Camera
from sound_processor import SoundProcessor
from cloud_processor import CloudProcessor
from rgb import RGBLed
from sonar import Sonar


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
