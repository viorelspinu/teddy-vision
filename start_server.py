import os
from flask import Flask
from flask import render_template
from flask import request, redirect, url_for

from cloud_service import CloudService
from configuration_service import ConfigurationService
from voice_codes_constants import *

cloud_service = CloudService()
configuration_service = ConfigurationService()

app = Flask(__name__)


def get_lang_codes():
    lang_en = {}
    lang_en['lang_code'] = TTS_LANGUAGE_CODE_ENGLISH
    lang_en['voice_code'] = TTS_VOICE_CODE_ENGLISH
    lang_en['name'] = "English"

    lang_fr = {}
    lang_fr['lang_code'] = TTS_LANGUAGE_CODE_FRENCH
    lang_fr['voice_code'] = TTS_VOICE_CODE_FRENCH
    lang_fr['name'] = "French"

    lang_de = {}
    lang_de['lang_code'] = TTS_LANGUAGE_CODE_GERMAN
    lang_de['voice_code'] = TTS_VOICE_CODE_GERMAN
    lang_de['name'] = "German"

    return [lang_en, lang_fr, lang_de]


languages = get_lang_codes()
selected_lang = 0


def get_lang_index(lang_code):
    print(lang_code)
    for i in range(len(languages)):
        if (languages[i]['lang_code'] == lang_code):
            return i


vision_selected_lang = get_lang_index(configuration_service.read_configuration()['language'])


@app.route('/')
def hello_world():
    global selected_lang
    return render_template('home.html', languages=languages, selected_lang=selected_lang, vision_selected_lang=vision_selected_lang)


@app.route('/speak', methods=['POST'])
def speak():
    text = request.form['text_to_speak']
    lang_code = request.form['lang_code']
    global selected_lang
    selected_lang = get_lang_index(lang_code)
    lang = languages[selected_lang]
    input_text = text
    mp3_base64 = cloud_service.do_text_to_speech_post(input_text, lang['lang_code'], lang['voice_code'])
    cloud_service.decode_text_to_file_as_base64(mp3_base64, "out.mp3")
    os.system("ffmpeg -i ./out.mp3 out.wav -y > /dev/null 2>&1 < /dev/null")
    os.system("aplay ./out.wav")

    return redirect('/')


@app.route('/save_settings', methods=['POST'])
def save_settings():
    lang_code = request.form['lang_code']
    global vision_selected_lang
    vision_selected_lang = get_lang_index(lang_code)
    lang = languages[vision_selected_lang]
    lang_code = lang['lang_code']
    print(lang_code)
    configuration_service.set_vision_language(lang_code)

    return redirect('/')


@app.route('/shutdown', methods=['POST'])
def shutdown():
    os.system("aplay ./wav/shutdown_response.wav")
    os.system("sudo shutdown -h now")
    return redirect('/')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
