import os
from local_communication_service import LocalCommunicationService as local_communication_service
from camera import Camera
from sound_processor import SoundProcessor
from cloud_processor import CloudProcessor
from rgb import RGBLed
from sonar import Sonar
import time

hotword = local_communication_service.getInstance().read_hotword()


if ("teddy" == hotword):
    SoundProcessor.getInstance().play("./wav/yes.wav", True)
    os.system("./push_to_talk.sh")

if ("explore" == hotword):
    camera = Camera()
    cloud_processor = CloudProcessor()
    led = RGBLed()
    led.set_color(0, 1, 0)
    SoundProcessor.getInstance().play("./wav/keep_it_still.wav", True)
    camera.take_photo()
    led.set_color(1, 0, 0)
    SoundProcessor.getInstance().play("./wav/done_have_to_think.wav", True)
    cloud_processor.process_photo()
