import time
import RPi.GPIO as GPIO


class SonarService:
    __instance = None

    @staticmethod
    def getInstance():
        if SonarService.__instance == None:
            SonarService()
        return SonarService.__instance

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.GPIO_TRIGECHO = 15
        SonarService.__instance = self

    def measure(self):
        start = time.time()

        GPIO.setup(self.GPIO_TRIGECHO, GPIO.IN)
        while GPIO.input(self.GPIO_TRIGECHO) == 0:
            start = time.time()

        while GPIO.input(self.GPIO_TRIGECHO) == 1:
            stop = time.time()

        elapsed = stop-start
        distance = (elapsed * 34300)/2.0
        time.sleep(0.1)
        return distance
    
    def cleanup(self):
        GPIO.cleanup()
