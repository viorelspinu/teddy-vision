import RPi.GPIO as GPIO


class DigitalSensorDistanceService:
    __instance = None

    @staticmethod
    def getInstance():
        if DigitalSensorDistanceService.__instance == None:
            DigitalSensorDistanceService()
        return DigitalSensorDistanceService.__instance

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.SENSOR_PIN = 27
        GPIO.setup(self.SENSOR_PIN, GPIO.IN)
        DigitalSensorDistanceService.__instance = self

    def measure(self):
        return GPIO.input(self.SENSOR_PIN)

    def cleanup(self):
        GPIO.cleanup()
