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
        CameraService.__instance = self

    def take_photo(self, file_path):
        print("PHOTO START")
        self.camera.resolution = (1024, 768)
        self.camera.start_preview()
        sleep(0.5)
        self.camera.capture(file_path)
        print("PHOTO DONE")
