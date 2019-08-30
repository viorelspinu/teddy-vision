import os
from local_communication_service import LocalCommunicationService as local_communication_service
from camera_service import CameraService
from sound_service import SoundService
from cloud_service import CloudService
from rgb_led_service import RGBLedService


class VisionService:

    def do_vision(self):
        camera_service = CameraService()
        cloud_processor = CloudService()
        led_service = RGBLedService.getInstance()
        led_service.set_color(0, 1, 0)
        SoundService.getInstance().play("./wav/keep_it_still.wav", True)
        camera_service.take_photo("photo.jpg")
        led_service.set_color(1, 0, 0)
        SoundService.getInstance().play("./wav/done_have_to_think.wav", True)
        cloud_processor.process_photo("photo.jpg", "vision_out.mp3")
        os.system("ffmpeg -i ./vision_out.mp3 ./vision_out.wav")
        os.system("aplay ./vision_out.wav")

