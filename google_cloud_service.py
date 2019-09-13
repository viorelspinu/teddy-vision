from time import sleep
import base64
import requests
import os
import simplejson as json
import time
import numpy as np
import os.path
from HTMLParser import HTMLParser
from configuration_service import ConfigurationService
from voice_codes_constants import *

API_KEY = os.environ['GOOGLE_API_KEY']


VISION_URL = "https://vision.googleapis.com/v1/images:annotate?key=" + API_KEY
TRANSLATE_URL = "https://translation.googleapis.com/language/translate/v2?key=" + API_KEY
TEXT_TO_SPEECH_URL = "https://texttospeech.googleapis.com/v1/text:synthesize?key=" + API_KEY


class GoogleCloudService:

    def __init__(self):
        self.configuration_service = ConfigurationService()

    def encode_file_as_base64(self, image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read())

    def decode_text_to_file_as_base64(self, text, file_path):
        with open(file_path, "wb") as out_file:
            out_file.write(base64.b64decode(text))
            out_file.close()

    def do_vision_post(self, image_path):
        json_data = {
            "requests": [
                {
                    "image": {
                        "content": self.encode_file_as_base64(image_path)
                    },
                    "features": [
                        {
                            "type": "LABEL_DETECTION",  # other options: LABEL_DETECTION FACE_DETECTION LOGO_DETECTION CROP_HINTS WEB_DETECTION
                            "maxResults": 10
                        }
                    ]
                }
            ]
        }
        r = requests.post(VISION_URL, data=json.dumps(json_data))
        return r.text

    def do_translate_post(self, text, language_code):
        json_data = {
            "q": text,
            "target": language_code
        }
        r = requests.post(TRANSLATE_URL, data=json.dumps(json_data))
        r_json = r.json()
        r_text = r_json['data']['translations'][0]['translatedText'].encode('utf-8')
        return r_text

    def do_text_to_speech_post(self, text, language_code, voice_code, ssml=False):
        text_tag = "text"
        if (ssml):
            text_tag = "ssml"
        json_data = {
            "input": {text_tag: text.encode('utf-8')},
            "voice": {
                "languageCode": language_code,
                "name": voice_code,
                "ssmlGender": "MALE"
            },
            "audioConfig": {
                "audioEncoding": "MP3"
            }
        }
        r = requests.post(TEXT_TO_SPEECH_URL, data=json.dumps(json_data))
        r_json = r.json()
        try:
            r_text = r_json['audioContent'].encode('utf-8')
        except:
            print("Something went wrong when calling the TTS API. Server response below:")
            print(r_json)

        return r_text

    def speak(self, input_text, language_code, voice_code, ssml=False):
        mp3_base64 = self.do_text_to_speech_post(input_text, language_code, voice_code, ssml)
        self.decode_text_to_file_as_base64(mp3_base64, "out.mp3")
        os.system("ffmpeg -i ./out.mp3 out.wav -y > /dev/null 2>&1 < /dev/null")
        os.system("aplay ./out.wav")

    def process_photo(self, photo_file, mp3_out_file):
        vision_response = self.do_vision_post(photo_file)
        json_vision_response = json.loads(vision_response)
        try:
            rows = json_vision_response['responses'][0]['labelAnnotations']
        except:
            print(json_vision_response)
            return
        data = "I have seen "
        for item in rows:
            data = data + str(item['description']) + ","

        translate_language_code = TRANSLATE_LANGUAGE_CODE_ENGLISH
        tts_voice_code = TTS_VOICE_CODE_ENGLISH
        tts_language_code = TTS_LANGUAGE_CODE_ENGLISH

        if (TTS_LANGUAGE_CODE_FRENCH == self.configuration_service.read_configuration()['language']):
            translate_language_code = TRANSLATE_LANGUAGE_CODE_FRENCH
            tts_voice_code = TTS_VOICE_CODE_FRENCH
            tts_language_code = TTS_LANGUAGE_CODE_FRENCH

        if (TTS_LANGUAGE_CODE_GERMAN == self.configuration_service.read_configuration()['language']):
            translate_language_code = TRANSLATE_LANGUAGE_CODE_GERMAN
            tts_voice_code = TTS_VOICE_CODE_GERMAN
            tts_language_code = TTS_LANGUAGE_CODE_GERMAN

        data_translated = self.do_translate_post(data, translate_language_code).decode('utf-8')
        html_parser = HTMLParser()
        data_translated = html_parser.unescape(data_translated)

        # print(data_translated)

        mp3_base64 = self.do_text_to_speech_post(data_translated, tts_language_code, tts_voice_code)

        self.decode_text_to_file_as_base64(mp3_base64, mp3_out_file)
