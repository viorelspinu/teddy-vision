import simplejson as json
from voice_codes_constants import *
import os

class ConfigurationService:
    __CONFIGURATION_FILE = "/home/pi/teddy-vision/configuration.json"
    __instance = None

    @staticmethod
    def getInstance():
        if ConfigurationService.__instance == None:
            ConfigurationService()
        return ConfigurationService.__instance

    def __init__(self):
        ConfigurationService.__instance = self

    def write_configuration(self, data):
        with open(self.__CONFIGURATION_FILE, "w") as f:
            json.dump(data, f)

    def set_vision_language(self, language_code, reply=False):
        configuration_data = self.read_configuration()
        configuration_data['language'] = language_code
        self.write_configuration(configuration_data)
        if (language_code == TTS_LANGUAGE_CODE_ENGLISH):
            if (reply):
                os.system("aplay ./wav/english.wav")
            print("will use english")
        if (language_code == TTS_LANGUAGE_CODE_FRENCH):
            if (reply):
                os.system("aplay ./wav/french.wav")
            print("will use french")
        if (language_code == TTS_LANGUAGE_CODE_GERMAN):
            if (reply):
                os.system("aplay ./wav/german.wav")
            print("will use german")

    def set_sensitivities(self, sensitivities):
        configuration_data = self.read_configuration()
        configuration_data['sensitivities'] = sensitivities
        self.write_configuration(configuration_data)

    def read_configuration(self):
        ret = None
        with open(self.__CONFIGURATION_FILE, "r") as f:
            ret = json.load(f)
        return ret

    def validate(self):
        try:
            data = self.read_configuration()
        except Exception as e:
            print(e)
            print("configuration file not there, creating.")
            data = {"sensitivities": {"german": 5, "explore": 5, "hello": 5, "french": 5, "english": 5}, "language": "en-US"}
            self.write_configuration(data)


configuration_service = ConfigurationService()
configuration_service.validate()
