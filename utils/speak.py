
import sys
import os
sys.path.append('./..')

from cloud_service import CloudService
from voice_codes_constants import *

cloud_service = CloudService()
input_text = sys.argv[1]
input_lang = sys.argv[2]
tts_lang_code = TTS_LANGUAGE_CODE_ENGLISH
tts_voice_code = TTS_VOICE_CODE_ENGLISH

if ("ro" == input_lang):
    tts_lang_code = TTS_MICROSOFT_LANGUAGE_CODE_RO
    tts_voice_code = TTS_MICROSOFT_VOICE_CODE_RO

if ("fr" == input_lang):
    tts_lang_code = TTS_LANGUAGE_CODE_FRENCH
    tts_voice_code = TTS_VOICE_CODE_FRENCH

if ("de" == input_lang):
    tts_lang_code = TTS_LANGUAGE_CODE_GERMAN
    tts_voice_code = TTS_VOICE_CODE_GERMAN

cloud_service.speak(input_text, tts_lang_code, tts_voice_code)
