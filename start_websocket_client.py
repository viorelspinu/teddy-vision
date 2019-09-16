from lomond import WebSocket
from lomond.persist import persist
from cloud_service import CloudService
from voice_codes_constants import *

websocket = WebSocket('http://116.203.129.161:80/chat')
cloud_service = CloudService()

for event in persist(websocket):
    if event.name == "ready":
        print("ready")
    elif event.name == "text":
        print(event.text)
        cloud_service.speak(event.text, TTS_LANGUAGE_CODE_ENGLISH)
