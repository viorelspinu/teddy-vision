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
        parts = event.text.split("_#_#_")
        cloud_service.speak(parts[1], parts[0])
