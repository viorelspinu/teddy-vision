import sys
import os
sys.path.append('./..')

from cloud_service import CloudService
from voice_codes_constants import *


cloud_service = CloudService()
input_text = sys.argv[1]
cloud_service.speak(input_text, TTS_LANGUAGE_CODE_ENGLISH, TTS_VOICE_CODE_ENGLISH)