import pygame
import time

class SoundProcessor:
    __instance = None

    @staticmethod
    def getInstance():
        if SoundProcessor.__instance == None:
            SoundProcessor()
        return SoundProcessor.__instance

    def __init__(self):
        if SoundProcessor.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            SoundProcessor.__instance = self

    def play(self, mp3_file_path, blocking=True):
        print("playing")
        pygame.mixer.init()
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
