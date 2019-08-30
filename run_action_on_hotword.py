import os
from local_communication_service import LocalCommunicationService as local_communication_service
from vision_service import VisionService as vision_service


class RunActionOnHotword:

    def run():
        self.hotword = local_communication_service.getInstance().read_hotword()
        if ("teddy" == hotword):
            os.system("aplay ./wav/yes.wav")
            os.system("./push_to_talk.sh")

        if ("explore" == hotword):
            vision_service.getInstance().do_vision()

    if __name__ == '__main__':
        run()
