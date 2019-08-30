import time
import os


class SoundService:
    __instance = None

    @staticmethod
    def getInstance():
        if SoundService.__instance == None:
            SoundService()
        return SoundService.__instance

    def __init__(self):
        if SoundService.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            SoundService.__instance = self
            pygame.mixer.init()

    def play(self, file_path):
        os.system("aplay ./" + file_path)
        