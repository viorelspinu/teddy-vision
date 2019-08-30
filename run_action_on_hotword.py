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
            os.system("aplay ./wav/french.wav")
            print("will update configuration file with French")

        if ("english" == hotword):
            os.system("aplay ./wav/english.wav")
            print("will update configuration file with English")


run_action_on_hotword = RunActionOnHotword()
run_action_on_hotword.run()
