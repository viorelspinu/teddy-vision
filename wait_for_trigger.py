
import sys
sys.path.append('./snowboy')

import os
import snowboydecoder
from local_communication_service import LocalCommunicationService as local_communication_service
from sonar_service import SonarService


class WaitForTriggerService:
    __interrupted = False

    def detected_teddy(self):
        print "Teddy Detected"
        local_communication_service.getInstance().write_hotword("teddy")
        self.terminate_detector()

    def detected_explore(self):
        print "Explore Detected"
        local_communication_service.getInstance().write_hotword("explore")
        self.terminate_detector()

    def terminate_detector(self):
        self.__interrupted = True
        self.detector.terminate()

    def interrupt_callback(self):
        return self.__interrupted

    def main(self):
        sonar_service = SonarService.getInstance()

        models = ["./snowboy_models/teddy.mdl", "./snowboy_models/explore.mdl"]
        self.detector = snowboydecoder.HotwordDetector(models, sensitivity=0.5, audio_gain=1)

        callbacks = [detected_teddy,
                     detected_explore]

        detector.start(detected_callback=callbacks, interrupt_check=self.interrupt_callback)


wait_for_trigger_service = WaitForTriggerService()
wait_for_trigger_service.main()
