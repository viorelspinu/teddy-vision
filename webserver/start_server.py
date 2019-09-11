
from flask import Flask
from flask import render_template
from flask import request, redirect, url_for

import sys
import os
sys.path.append('./..')


from cloud_service import CloudService

cloud_service = CloudService()


app = Flask(__name__)


def get_lang_codes():
    lang_en = {}
    lang_en['lang_code'] = CloudService.TTS_LANGUAGE_CODE_ENGLISH
    lang_en['voice_code'] = CloudService.TTS_VOICE_CODE_ENGLISH
    lang_en['name'] = "English"

    lang_fr = {}
    lang_fr['lang_code'] = CloudService.TTS_LANGUAGE_CODE_FRENCH
    lang_fr['voice_code'] = CloudService.TTS_VOICE_CODE_FRENCH
    lang_fr['name'] = "French"

    lang_de = {}
    lang_de['lang_code'] = CloudService.TTS_LANGUAGE_CODE_GERMAN
    lang_de['voice_code'] = CloudService.TTS_VOICE_CODE_GERMAN
    lang_de['name'] = "German"

    return [lang_en, lang_fr, lang_de]


languages = get_lang_codes()
selected_lang = 0


def get_lang_index(lang_code):
    print(lang_code)
    for i in range(len(languages)):
        if (languages[i]['lang_code'] == lang_code):
            return i


@app.route('/')
def hello_world():
    return render_template('home.html', languages=languages, selected_lang=selected_lang)


@app.route('/speak', methods=['POST'])
def speak():
    text = request.form['text_to_speak']
    lang_code = request.form['lang_code']
    selected_lang = get_lang_index(lang_code)    
    lang = languages[selected_lang]
    print(lang_code)
    print(text)
    input_text = text
    mp3_base64 = cloud_service.do_text_to_speech_post(input_text, lang['lang_code'], lang['voice_code'])
    cloud_service.decode_text_to_file_as_base64(mp3_base64, "out.mp3")
    os.system("ffmpeg -i ./out.mp3 out.wav -y > /dev/null 2>&1 < /dev/null")
    os.system("aplay ./out.wav")

    return redirect('/', selected_lang=selected_lang)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
