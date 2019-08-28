import snowboydecoder
import os

interrupted = False


def detected_callback():
    print "Hotword Detected"
    detector.terminate()
    global interrupted
    interrupted = True
    print "terminate"


def interrupt_callback():
    global interrupted
    return interrupted


detector = snowboydecoder.HotwordDetector("./t.model", sensitivity=0.5, audio_gain=1)

detector.start(detected_callback, interrupt_check=interrupt_callback)
