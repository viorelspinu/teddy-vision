import sys
import os
import socket
from cloud_service import CloudService
from voice_codes_constants import *


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip_address = s.getsockname()[0]
print(ip_address)
s.close()


cloud_service = CloudService()
input_text = "<speak>my ip address is" + ip_address.replace(".", "<break time=\"0.5s\"/>") + "</speak>"
cloud_service.speak(input_text, TTS_LANGUAGE_CODE_ENGLISH, TTS_VOICE_CODE_ENGLISH, ssml=True)

