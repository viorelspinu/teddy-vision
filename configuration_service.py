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
        with open(self.__CONFIGURATION_FILE, "w") as f:
            json.dump(data, f)

    def read_configuration(self):
        ret = None
        with open(self.__CONFIGURATION_FILE, "r") as f:
            ret = json.load(f)
        return ret

    def validate(self):
        try:
            read_configuration()
        except:
            data = {"language": "en"}
            self.write_configuration(data)


configuration_service = ConfigurationService()
configuration_service.validate()