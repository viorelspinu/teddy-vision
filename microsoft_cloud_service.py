
import os
import requests
import time
from xml.etree import ElementTree
from voice_codes_constants import *


class MicrosoftCloudService():
    
    def __init__(self):
        
        if 'SPEECH_SERVICE_KEY' in os.environ:
            subscription_key = os.environ['SPEECH_SERVICE_KEY']
        else:
            print('Environment variable for your subscription key is not set.')
            exit()

        self.subscription_key = subscription_key
        self.timestr = time.strftime("%Y%m%d-%H%M")
        self.access_token = None

    def get_token(self):
        fetch_token_url = "https://westus.api.cognitive.microsoft.com/sts/v1.0/issueToken"
        headers = {
            'Ocp-Apim-Subscription-Key': self.subscription_key
        }
        response = requests.post(fetch_token_url, headers=headers)
        self.access_token = str(response.text)

    def speak(self, text):
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
        xml_body.set('{http://www.w3.org/XML/1998/namespace}lang', TTS_MICROSOFT_LANGUAGE_CODE_RO)
        voice = ElementTree.SubElement(xml_body, 'voice')
        voice.set('{http://www.w3.org/XML/1998/namespace}lang', TTS_MICROSOFT_LANGUAGE_CODE_RO)
        voice.set('name', TTS_MICROSOFT_VOICE_CODE_RO)
        voice.text = text
        body = ElementTree.tostring(xml_body)

        response = requests.post(constructed_url, headers=headers, data=body)

        if response.status_code == 200:
            with open('sample-' + self.timestr + '.wav', 'wb') as audio:
                audio.write(response.content)
                print("\nStatus code: " + str(response.status_code) + "\nYour TTS is ready for playback.\n")
        else:
            print("\nStatus code: " + str(response.status_code) + "\nSomething went wrong. Check your subscription key and headers.\n")

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


if __name__ == "__main__":
    app = TextToSpeech(subscription_key)
    app.get_token()
    app.speak("salut, imi place cum iti sta azi !")
    # Get a list of voices https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/rest-text-to-speech#get-a-list-of-voices
    # app.get_voices_list()
