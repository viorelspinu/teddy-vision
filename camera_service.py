from time import sleep
from picamera import PiCamera


class CameraService:
    __instance = None

    @staticmethod
    def getInstance():
        if CameraService.__instance == None:
            CameraService()
        return CameraService.__instance

    def __init__(self):
        self.camera = PiCamera()
        self.camera.iso = 100
        # Wait for the automatic gain control to settle
        sleep(2)
        # Now fix the values
        self.camera.shutter_speed = self.camera.exposure_speed
        self.camera.exposure_mode = 'off'
        g = self.camera.awb_gains
        self.camera.awb_mode = 'off'
        self.camera.awb_gains = g
        CameraService.__instance = self

    def take_photo(self, file_path):
        print("PHOTO START")
        self.camera.resolution = (1024, 768)
        self.camera.start_preview()
        sleep(1)
        self.camera.capture(file_path)
        print("PHOTO DONE")
