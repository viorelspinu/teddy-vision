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
        parts = event.text.split("_#_#_")
        cloud_service.speak(parts[1], parts[0])
        with open("remote_speech_log.txt", "a") as myfile:
            myfile.write(event.text + "\r\n")
            myfile.close()
