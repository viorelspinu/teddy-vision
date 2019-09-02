import simplejson as json


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
        with open(self.__hotword_file, "w") as f:
            json.dump(data, f)

    def read_configuration(self):
        ret = None
        with open(self.__CONFIGURATION_FILE, "r") as f:
            ret = json.load(json_data_file)
        return ret

    def create_default(self):
        try:
            read_configuration()
        except:
            data = {"language": "english"}
            self.write_configuration(data)
