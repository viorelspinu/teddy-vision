sys.path.append('./snowboy')
from local_communication_service import LocalCommunicationService as local_communication_service
import snowboydecoder
import os
import sys



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


models = ["./snowboy_models/teddy.mdl", "./snowboy_models/explore.mdl"]

detector = snowboydecoder.HotwordDetector(models, sensitivity=0.5, audio_gain=1)

callbacks = [detected_teddy,
             detected_explore]

detector.start(detected_callback=callbacks, interrupt_check=interrupt_callback)