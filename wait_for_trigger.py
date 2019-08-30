
import sys
sys.path.append('./snowboy')


from sonar_service import SonarService
from local_communication_service import LocalCommunicationService as local_communication_service
import snowboydecoder
import os


class WaitForTriggerService:
    self.interrupted = False

    def detected_teddy(self):
        print "Teddy Detected"
        local_communication_service.getInstance().write_hotword("teddy")
        terminate_detector()

    def detected_explore(self):
        print "Explore Detected"
        local_communication_service.getInstance().write_hotword("explore")
        terminate_detector()

    def terminate_detector(self):
        detector.terminate()
        global interrupted
        interrupted = True

    def interrupt_callback(self):
        global interrupted
        return interrupted

    def main(self):
        sonar_service = SonarService.getInstance()

        models = ["./snowboy_models/teddy.mdl", "./snowboy_models/explore.mdl"]
        detector = snowboydecoder.HotwordDetector(models, sensitivity=0.5, audio_gain=1)

        callbacks = [detected_teddy,
                     detected_explore]

        detector.start(detected_callback=callbacks, interrupt_check=interrupt_callback)


wait_for_trigger_service = WaitForTriggerService()
wait_for_trigger_service.main()