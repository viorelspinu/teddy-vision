from lomond import WebSocket
from lomond.persist import persist
from cloud_service import CloudService
from datetime import datetime
from voice_codes_constants import *

websocket = WebSocket('http://116.203.129.161:80/chat')
cloud_service = CloudService()

for event in persist(websocket):
    if event.name == "ready":
        print("ready")
    elif event.name == "text":
        text = str(event.text)
        print(text)
        if (text.startswith("__SPEAK__")):
            text = text.replace("__SPEAK__", "")
            parts = text.split("_#_#_")
            cloud_service.speak(parts[1], parts[0])
            now = datetime.now()
            date_string = now.strftime("%d/%m/%Y %H:%M:%S")
            with open("remote_speech_log.txt", "a") as myfile:
                myfile.write(date_string + ": " + event.text + "\r\n")
                myfile.close()

        if (text.startswith("__SENSITIVITY__")):
            text = text.replace("__SENSITIVITY__", "")
            print(text)
