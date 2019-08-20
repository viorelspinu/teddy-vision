import picamera
import os
import numpy as np
from picamera.array import PiMotionAnalysis
from time import sleep
from photo import CloudProcessor

camera = picamera.PiCamera()

class MotionDetector(PiMotionAnalysis):
    take_photo = False
    count = 0
    def motion_detected(self):
        self.take_photo = True
    def analyse(self, a):
        a = np.sqrt(
            np.square(a['x'].astype(np.float)) +
            np.square(a['y'].astype(np.float))
            ).clip(0, 255).astype(np.uint8)
        vector_count = (a > 25).sum()
        if (vector_count > 2):
            print(vector_count)
        if vector_count > 15:
            self.count = self.count + 1
            if (self.count > 5):
            	self.motion_detected()
        else:
           self.count = 0
try:
    motion_detector = MotionDetector(camera)
    while True:
        if not camera.recording:
            camera.resolution = (640, 320)
            camera.framerate = 24
            camera.start_recording(os.devnull, format='h264', motion_output=motion_detector)
        if camera.recording:
            camera.wait_recording(0.1)
            if motion_detector.take_photo:
                camera.stop_recording()
                print ("PHOTO START !")
                sleep(1)
                camera.resolution = (2592, 1944)
                camera.capture('photo.jpg')
                print ("PHOTO DONE !")
                CloudProcessor().process_photo()
                motion_detector.take_photo = False

finally:
    print("end")
    camera.stop_recording()