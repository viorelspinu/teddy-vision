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
            
    def take_photo(self):
        print("PHOTO START")
        self.camera.resolution = (1024, 768)
        self.camera.start_preview()
        sleep(1)
        self.camera.capture("photo.jpg")        
        print("PHOTO DONE")
