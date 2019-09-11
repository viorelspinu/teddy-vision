from cloud_service import CloudService
from flask import Flask
from flask import render_template
from flask import request

import sys
import os
sys.path.append('./..')

cloud_service = CloudService()


app = Flask(__name__)


def get_lang_codes():
    lang_en = {}
    lang_en.code = CloudService.TTS_LANGUAGE_CODE_ENGLISH
    lang_en.name = "English"
    lang_fr = {}
    lang_fr.code = CloudService.TTS_LANGUAGE_CODE_FRENCH
    lang_fr.name = "French"
    lang_de = {}
    lang_de.code = CloudService.TTS_LANGUAGE_CODE_GERMAN
    lang_de.name = "German"

    return [lang_en, lang_fr, lang_de]


@app.route('/')
def hello_world():
    return render_template('home.html', lang_codes=get_lang_codes())


@app.route('/speak', methods=['POST'])
def speak():
    text = request.form['text_to_speak']
    print(text)
    input_text = text
    mp3_base64 = cloud_service.do_text_to_speech_post(input_text, CloudService.TTS_LANGUAGE_CODE_ENGLISH, CloudService.TTS_VOICE_CODE_ENGLISH)
    cloud_service.decode_text_to_file_as_base64(mp3_base64, "out.mp3")
    os.system("ffmpeg -i ./out.mp3 out.wav -y > /dev/null 2>&1 < /dev/null")
    os.system("aplay ./out.wav")

    return render_template('home.html', lang_codes=get_lang_codes())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
