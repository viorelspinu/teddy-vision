import sys
from cloud_processor import CloudProcessor

cloud_processor = CloudProcessor()
input_text = sys.argv[1]
mp3_base64 =  cloud_processor.do_text_to_speech_post(input_text)
cloud_processor.decode_text_to_file_as_base64(mp3_base64, "out.mp3")