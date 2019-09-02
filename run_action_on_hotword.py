import os
from local_communication_service import LocalCommunicationService as local_communication_service
from vision_service import VisionService


class RunActionOnHotword:

    def run(self):
        hotword = local_communication_service.getInstance().read_hotword()
        if ("teddy" == hotword):
            os.system("aplay ./wav/yes.wav")
            os.system("./run_assistant_instance.sh")

        if ("explore" == hotword):
            vision_service = VisionService()
            vision_service.do_vision()

        if ("french" == hotword):
            os.system("aplay ./wav/french.wav")
            os.system("rm use_english")
            os.system("touch use_french")
            print("will update configuration file with French")

        if ("english" == hotword):
            os.system("aplay ./wav/english.wav")
            os.system("touch use_english")
            os.system("rm use_french")
            print("will update configuration file with English")

        if ("shutdown" == hotword):
            os.system("aplay ./wav/shutdown_response.wav")
            print("shutdown now")
            os.system("sudo shutdown -h now")
            

run_action_on_hotword = RunActionOnHotword()
run_action_on_hotword.run()
