from google_cloud_service import GoogleCloudService
from microsoft_cloud_service import MicrosoftCloudService
from voice_codes_constants import *


class CloudService:

    def __init__(self):
        print("init")

    def do_vision_post(self, image_path):
        google_cloud_service = GoogleCloudService()
        return google_cloud_service.do_vision_post(image_path)

    def do_translate_post(self, text, language_code):
        google_cloud_service = GoogleCloudService()
        return google_cloud_service.do_translate_post(text, language_code)

    def do_text_to_speech_post(self, text, language_code, voice_code, ssml=False):
        google_cloud_service = GoogleCloudService()
        return google_cloud_service.do_text_to_speech_post(text, language_code, voice_code, ssml)

    def process_photo(self, photo_file, mp3_out_file):
        google_cloud_service = GoogleCloudService()
        return google_cloud_service.process_photo(photo_file, mp3_out_file)

    def speak(self, input_text, language_code, voice_code):
        cloud_service = None
        if (TTS_MICROSOFT_LANGUAGE_CODE_RO == language_code):
            cloud_service = MicrosoftCloudService()
        else:
            cloud_service = GoogleCloudService()

        cloud_service.speak(input_text, language_code, voice_code)
