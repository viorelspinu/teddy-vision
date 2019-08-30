import snowboydecoder
import os

interrupted = False


def detected_teddy():
    print "Teddy Detected"
    write_hotword("teddy")
    terminate_detector()


def detected_explore():
    print "Explore Detected"
    write_hotword("explore")
    terminate_detector()


def terminate_detector():
    detector.terminate()
    global interrupted
    interrupted = True

def write_hotword(hotword):
    f = open("hotword.txt", "w")
    f.write(hotword)
    f.close()


def interrupt_callback():
    global interrupted
    return interrupted


models = ["./t.model", "./explore.mdl"]

detector = snowboydecoder.HotwordDetector(models, sensitivity=0.5, audio_gain=1)

callbacks = [detected_teddy,
             detected_explore]

detector.start(detected_callback=callbacks, interrupt_check=interrupt_callback)
