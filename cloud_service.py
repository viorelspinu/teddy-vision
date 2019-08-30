from time import sleep
import base64
import requests
import os
import simplejson as json
import time
import numpy as np
from sound_service import SoundService

API_KEY = os.environ['GOOGLE_API_KEY']

DUTCH_TRANSLATE_LANGUAGE_CODE = 'nl'
FRENCH_TRANSLATE_LANGUAGE_CODE = 'fr'

VISION_URL = "https://vision.googleapis.com/v1/images:annotate?key=" + API_KEY
TRANSLATE_URL = "https://translation.googleapis.com/language/translate/v2?key=" + API_KEY
TEXT_TO_SPEECH_URL = "https://texttospeech.googleapis.com/v1/text:synthesize?key=" + API_KEY


class CloudService:

    def __init__(self):
        self.sound_service = SoundService.getInstance()

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

    def do_text_to_speech_post(self, text):
        json_data = {
            "input": {"text": text},
            "voice": {
                "languageCode": "en-US",
                "name": "en-US-Wavenet-D",
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

    def process_photo(self, photo_file):
        vision_response = self.do_vision_post(photo_file)
        json_vision_response = json.loads(vision_response)
        try:
            rows = json_vision_response['responses'][0]['labelAnnotations']
        except:
            print(json_vision_response)
            return
        data = ""
        for item in rows:
            data = data + str(item['description']) + ","
        print(data)

        #data_translated = self.do_translate_post(data, DUTCH_LANGUAGE_CODE)
        # print(data_translated)

        mp3_base64 = self.do_text_to_speech_post("I have seen:" + data)
        self.decode_text_to_file_as_base64(mp3_base64, "out.mp3")
        self.sound_service.play("./out.mp3")
