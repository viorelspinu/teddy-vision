import board
import neopixel
from time import sleep


class LedController:
    pixels = None

    def __init__(self):
        self.pixels = neopixel.NeoPixel(board.D18, 1,  brightness=1)
        self.pixels[0] = (255, 255, 255)
        print("LEDS INIT DONE")

    def setColor(self, r, g, b):
        self.pixels[0] = (r, g, b)
