import os
from local_communication_service import LocalCommunicationService as local_communication_service
from vision_service import VisionService


class RunActionOnHotword:

    def run(self):
        hotword = local_communication_service.getInstance().read_hotword()
        if ("teddy" == hotword):
            os.system("aplay ./wav/yes.wav")
            os.system("./push_to_talk.sh")

        if ("explore" == hotword):
            vision_service = VisionService()
            vision_service.do_vision()

        if ("french" == hotword):
            print("will update configuration file with French")


run_action_on_hotword = RunActionOnHotword()
run_action_on_hotword.run()
