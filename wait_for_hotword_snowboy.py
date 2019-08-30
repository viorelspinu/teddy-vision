import snowboydecoder
import os

interrupted = False


def detected_teddy():
    print "Teddy Detected"
    detector.terminate()
    global interrupted
    interrupted = True
    print "terminate on teddy"


def detected_explore():
    print "Explore Detected"
    detector.terminate()
    global interrupted
    interrupted = True
    print "terminate on explore"


def interrupt_callback():
    global interrupted
    return interrupted


models = ["./t.model", "./explore.mdl"]

detector = snowboydecoder.HotwordDetector(models, sensitivity=0.5, audio_gain=1)

callbacks = [lambda: detected_teddy,
             lambda: detected_explore]

detector.start(detected_callback=callbacks, interrupt_check=interrupt_callback)
