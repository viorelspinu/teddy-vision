import os
from local_communication_service import LocalCommunicationService as local_communication_service
from vision_service import VisionService
from configuration_service import ConfigurationService
from rgb_led_service import RGBLedService


class RunActionOnHotword:

    def __init__(self):
        self.configuration_service = ConfigurationService()

    def run(self):
        hotword = local_communication_service.getInstance().read_hotword()
        RGBLedService.getInstance().set_color(1, 0, 0)
        if ("teddy" == hotword):
            os.system("aplay ./wav/yes.wav")
            os.system("./run_assistant_instance.sh")

        if ("explore" == hotword):
            vision_service = VisionService()
            vision_service.do_vision()

        if ("french" == hotword):
            configuration_data = self.configuration_service.read_configuration()
            configuration_data['language'] = "fr"
            self.configuration_service.write_configuration(configuration_data)
            os.system("aplay ./wav/french.wav")
            print("will use french")

        if ("english" == hotword):
            configuration_data = self.configuration_service.read_configuration()
            configuration_data['language'] = "en"
            self.configuration_service.write_configuration(configuration_data)
            os.system("aplay ./wav/english.wav")
            print("will use english")

        if ("shutdown" == hotword):
            os.system("aplay ./wav/shutdown_response.wav")
            print("shutdown now")
            #os.system("sudo shutdown -h now")


run_action_on_hotword = RunActionOnHotword()
run_action_on_hotword.run()
