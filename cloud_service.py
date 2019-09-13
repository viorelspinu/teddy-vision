from google_cloud_service import GoogleCloudService
from microsoft_cloud_service import MicrosoftCloudService
from voice_codes_constants import *
from HTMLParser import HTMLParser
import os

class CloudService:

    def do_vision_post(self, image_path):
        google_cloud_service = GoogleCloudService()
        return google_cloud_service.do_vision_post(image_path)

    def do_translate_post(self, text, language_code):
        google_cloud_service = GoogleCloudService()
        return google_cloud_service.do_translate_post(text, language_code)

    def do_text_to_speech_post(self, text, language_code, voice_code, ssml=False):
        google_cloud_service = GoogleCloudService()
        return google_cloud_service.do_text_to_speech_post(text, language_code, voice_code, ssml)

    def process_photo(self, photo_file):
        google_cloud_service = GoogleCloudService()
        return google_cloud_service.process_photo(photo_file)

    def translate(self, text, target_language):
        cloud_service = GoogleCloudService()

        translate_language_code = TRANSLATE_LANGUAGE_CODE_ENGLISH
        tts_voice_code = TTS_VOICE_CODE_ENGLISH
        tts_language_code = TTS_LANGUAGE_CODE_ENGLISH

        if (TTS_LANGUAGE_CODE_FRENCH == target_language):
            translate_language_code = TRANSLATE_LANGUAGE_CODE_FRENCH

        if (TTS_LANGUAGE_CODE_GERMAN == target_language):
            translate_language_code = TRANSLATE_LANGUAGE_CODE_GERMAN

        if (TTS_MICROSOFT_LANGUAGE_CODE_RO == target_language):
            translate_language_code = TRANSLATE_LANGUAGE_CODE_ROMANIAN

        data_translated = cloud_service.do_translate_post(text, translate_language_code).decode('utf-8')
        html_parser = HTMLParser()
        data_translated = html_parser.unescape(data_translated)

        return data_translated

    def speak(self, input_text, language_code, voice_code=False, ssml=False):
        cloud_service = None
        if (False == voice_code):
            if (TTS_LANGUAGE_CODE_ENGLISH == language_code):
                voice_code = TTS_VOICE_CODE_ENGLISH
            if (TTS_LANGUAGE_CODE_FRENCH == language_code):
                voice_code = TTS_VOICE_CODE_FRENCH
            if (TTS_LANGUAGE_CODE_GERMAN == language_code):
                voice_code = TTS_VOICE_CODE_GERMAN
            if (TTS_MICROSOFT_LANGUAGE_CODE_RO == language_code):
                voice_code = TTS_MICROSOFT_VOICE_CODE_RO

        if (TTS_MICROSOFT_LANGUAGE_CODE_RO == language_code):
            cloud_service = MicrosoftCloudService()
        else:
            cloud_service = GoogleCloudService()

        wav_file_path = cloud_service.speak(input_text, language_code, voice_code, ssml)
        os.system("aplay " + wav_file_path)
