import pygame
import time


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

    def play(self, mp3_file_path, blocking=True):
        print("playing")
        pygame.mixer.music.load(mp3_file_path)
        pygame.mixer.music.play()
        if (blocking):
            while pygame.mixer.music.get_busy() == True:
                time.sleep(0.1)
        print("done playing")

    def done_playing(self):
        try:
            return pygame.mixer.music.get_busy()
        except:
            return True