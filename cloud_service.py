from time import sleep
import base64
import requests
import os
import simplejson as json
import time
import numpy as np
import os.path
from HTMLParser import HTMLParser

API_KEY = os.environ['GOOGLE_API_KEY']

TRANSLATE_LANGUAGE_CODE_ENGLISH = "en"
TTS_VOICE_CODE_ENGLISH = "en-US-Wavenet-D"
TTS_LANGUAGE_CODE_ENGLISH = "en-US"

TRANSLATE_LANGUAGE_CODE_FRENCH = "fr"
TTS_VOICE_CODE_FRENCH = "fr-FR-Standard-D"
TTS_LANGUAGE_CODE_FRENCH = "fr-FR"


VISION_URL = "https://vision.googleapis.com/v1/images:annotate?key=" + API_KEY
TRANSLATE_URL = "https://translation.googleapis.com/language/translate/v2?key=" + API_KEY
TEXT_TO_SPEECH_URL = "https://texttospeech.googleapis.com/v1/text:synthesize?key=" + API_KEY


class CloudService:

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

    def do_text_to_speech_post(self, text, language_code, voice_code):
        json_data = {
            "input": {"text": text.encode('utf-8')},
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

    def process_photo(self, photo_file, mp3_out_file):
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

        translate_language_code = TRANSLATE_LANGUAGE_CODE_ENGLISH
        tts_voice_code = TTS_VOICE_CODE_ENGLISH
        tts_language_code = TTS_LANGUAGE_CODE_ENGLISH

        if (os.path.exists("use_french")):
            translate_language_code = TRANSLATE_LANGUAGE_CODE_FRENCH
            tts_voice_code = TTS_VOICE_CODE_FRENCH
            tts_language_code = TTS_LANGUAGE_CODE_FRENCH

        data_translated = self.do_translate_post(data, translate_language_code).decode('utf-8')
        html_parser = HTMLParser()
        data_translated = html_parser.unescape(unicode(data_translated))

        print(data_translated)

        mp3_base64 = self.do_text_to_speech_post(data_translated, tts_language_code, tts_voice_code)

        self.decode_text_to_file_as_base64(mp3_base64, mp3_out_file)
