import sys
sys.path.append('./snowboy')

import os
import snowboydecoder
from local_communication_service import LocalCommunicationService as local_communication_service


interrupted = False


def detected_teddy():
    print "Teddy Detected"
    local_communication_service.getInstance().write_hotword("teddy")
    terminate_detector()


def detected_explore():
    print "Explore Detected"
    local_communication_service.getInstance().write_hotword("explore")
    terminate_detector()


def terminate_detector():
    detector.terminate()
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted


models = ["./teddy.mdl", "./explore.mdl"]

detector = snowboydecoder.HotwordDetector(models, sensitivity=0.5, audio_gain=1)

callbacks = [detected_teddy,
             detected_explore]

detector.start(detected_callback=callbacks, interrupt_check=interrupt_callback)
