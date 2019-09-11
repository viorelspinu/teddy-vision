from flask import Flask
from flask import render_template
from flask import request

import sys
import os
sys.path.append('./..')
from cloud_service import CloudService

cloud_service = CloudService()


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/speak', methods=['POST'])
def speak():
    text = request.form['text_to_speak']
    print(text)
    input_text = text
    mp3_base64 = cloud_service.do_text_to_speech_post(input_text, CloudService.TTS_LANGUAGE_CODE_ENGLISH, CloudService.TTS_VOICE_CODE_ENGLISH)
    cloud_service.decode_text_to_file_as_base64(mp3_base64, "out.mp3")
    os.system("ffmpeg -i ./out.mp3 out.wav -y > /dev/null 2>&1 < /dev/null")
    os.system("aplay ./out.wav")
    
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
