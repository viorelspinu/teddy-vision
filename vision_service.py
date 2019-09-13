import os
from local_communication_service import LocalCommunicationService as local_communication_service
from camera_service import CameraService
from sound_service import SoundService
from cloud_service import CloudService
from rgb_led_service import RGBLedService
from configuration_service import ConfigurationService
from voice_codes_constants import *


class VisionService:

    def do_vision(self):
        camera_service = CameraService()
        cloud_processor = CloudService()
        led_service = RGBLedService.getInstance()
        led_service.set_color(0, 1, 0)
        SoundService.getInstance().play("./wav/keep_it_still.wav")
        camera_service.take_photo("photo.jpg")
        led_service.set_color(1, 0, 0)
        SoundService.getInstance().play("./wav/done_have_to_think.wav")
        labels = cloud_processor.process_photo("photo.jpg")

        vision_language_code = ConfigurationService.getInstance().read_configuration['language']

        if (not (TTS_LANGUAGE_CODE_ENGLISH == vision_language_code)):
            labels = cloud_processor.translate(labels, vision_language_code)

        cloud_processor.speak(labels, vision_language_code)
