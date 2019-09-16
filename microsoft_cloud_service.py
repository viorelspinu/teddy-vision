
import os
import requests
import time
from xml.etree import ElementTree
from voice_codes_constants import *
import simplejson as json


class MicrosoftCloudService():

    __TOKEN_FILE = "microsoft_cached_token.json"
    #__TOKEN_EXPIRATION_PERIOD_SECONDS = 9 * 60
    __TOKEN_EXPIRATION_PERIOD_SECONDS = 15

    def __init__(self):

        if 'SPEECH_SERVICE_KEY' in os.environ:
            subscription_key = os.environ['SPEECH_SERVICE_KEY']
        else:
            print('Environment variable for your subscription key is not set.')
            exit()

        self.subscription_key = subscription_key
        self.timestr = time.strftime("%Y%m%d-%H%M")
        self.access_token = None

    def read_cached_token(self):
        ret = None
        try:
            with open(self.__TOKEN_FILE, "r") as f:
                ret = json.load(f)
            if ((time.time() - ret['time']) > __TOKEN_EXPIRATION_PERIOD_SECONDS):
                print("token expired")
                return None
            return ret
        except Exception as e:
            print(e)
            return None

    def save_cached_token(self, token):
        data = {"token": token, "time": time.time()}
        with open(self.__TOKEN_FILE, "w") as f:
            json.dump(data, f)

    def create_token(self):
        fetch_token_url = "https://westus.api.cognitive.microsoft.com/sts/v1.0/issueToken"
        headers = {
            'Ocp-Apim-Subscription-Key': self.subscription_key
        }
        response = requests.post(fetch_token_url, headers=headers)
        access_token = str(response.text)
        self.save_cached_token(access_token)
        return access_token

    def get_token(self):
        token = self.read_cached_token()
        print("cached token is :")
        print(token)
        if (token is None):
            token = self.create_token()
        self.access_token = token

    def speak(self, text, lang_code, voice_code, ssml=False):
        self.get_token()

        base_url = 'https://westus.tts.speech.microsoft.com/'
        path = 'cognitiveservices/v1'
        constructed_url = base_url + path
        headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'Content-Type': 'application/ssml+xml',
            'X-Microsoft-OutputFormat': 'riff-24khz-16bit-mono-pcm',
            'User-Agent': 'YOUR_RESOURCE_NAME'
        }
        xml_body = ElementTree.Element('speak', version='1.0')
        xml_body.set('{http://www.w3.org/XML/1998/namespace}lang', lang_code)
        voice = ElementTree.SubElement(xml_body, 'voice')
        voice.set('{http://www.w3.org/XML/1998/namespace}lang', lang_code)
        voice.set('name', voice_code)
        voice.text = text
        body = ElementTree.tostring(xml_body)

        response = requests.post(constructed_url, headers=headers, data=body)

        if response.status_code == 200:
            with open('out.wav', 'wb') as audio:
                audio.write(response.content)
        else:
            print("\n " + str(response) + "\n\n\n\nSomething went wrong. Check your subscription key and headers.\n")

        return "out.wav"

    def get_voices_list(self):
        base_url = 'https://westus.tts.speech.microsoft.com/'
        path = 'cognitiveservices/voices/list'
        constructed_url = base_url + path
        headers = {
            'Authorization': 'Bearer ' + self.access_token,
        }
        response = requests.get(constructed_url, headers=headers)
        if response.status_code == 200:
            print("\nAvailable voices: \n" + response.text)
        else:
            print("\nStatus code: " + str(response.status_code) + "\nSomething went wrong. Check your subscription key and headers.\n")
