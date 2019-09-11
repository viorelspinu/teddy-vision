import sys
import os
import socket
from cloud_service import CloudService


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip_address = s.getsockname()[0]
print(ip_address)
s.close()


cloud_service = CloudService()
input_text = "<speak>my ip address is" + ip_address.replace(".", "<break time=\"0.5s\"/>") + "</speak>"
mp3_base64 = cloud_service.do_text_to_speech_post(input_text, CloudService.TTS_LANGUAGE_CODE_ENGLISH, CloudService.TTS_VOICE_CODE_ENGLISH, ssml=True)
cloud_service.decode_text_to_file_as_base64(mp3_base64, "out.mp3")
os.system("ffmpeg -i ./out.mp3 out.wav -y > /dev/null 2>&1 < /dev/null")
os.system("aplay ./out.wav")
print("file saved as 'out.wav'")
