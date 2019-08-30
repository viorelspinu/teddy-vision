class LocalCommunicationService:
    __hotword_file = "/home/pi/teddy-vision/hotword.txt"
    __instance = None

    @staticmethod
    def getInstance():
        if LocalCommunicationService.__instance == None:
            LocalCommunicationService()
        return LocalCommunicationService.__instance

    def __init__(self):
        LocalCommunicationService.__instance = self

    def write_hotword(hotword):
        with open(self.__hotword_file, "w") as f:
            f.write(hotword)

    def read_hotword():
        ret = None
        with open(self.__hotword_file, "r") as f:
            ret = f.readline()
        return ret
