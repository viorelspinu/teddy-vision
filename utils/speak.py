from cloud_service import CloudService
import sys
import os
sys.path.append('./..')


cloud_service = CloudService()
input_text = sys.argv[1]
mp3_base64 = cloud_service.do_text_to_speech_post(input_text, CloudService.TTS_LANGUAGE_CODE_ENGLISH, CloudService.TTS_VOICE_CODE_ENGLISH)
cloud_service.decode_text_to_file_as_base64(mp3_base64, "out.mp3")
os.system("ffmpeg -i ./out.mp3 out.wav -y > /dev/null 2>&1 < /dev/null")
os.system("aplay ./out.wav")
print("file saved as 'out.wav'")
