from lomond import WebSocket
from cloud_service import CloudService
from voice_codes_constants import *

websocket = WebSocket('http://116.203.129.161:8080/chat')
cloud_service = CloudService()

for event in websocket:
    if event.name == "ready":
        print ("ready")
    elif event.name == "text":
        print(event.text)
        cloud_service.speak(event.text, TTS_LANGUAGE_CODE_ENGLISH)