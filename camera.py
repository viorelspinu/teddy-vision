from time import sleep
from picamera import PiCamera

class Camera:
    camera = PiCamera()

    def take_photo(self):
        print("PHOTO START")
        self.camera.resolution = (1024, 768)
        self.camera.start_preview()
        sleep(1)
        self.camera.capture("photo.jpg")        
        print("PHOTO DONE")