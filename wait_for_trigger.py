import sys
sys.path.append('./snowboy')
from rgb_led_service import RGBLedService
from sonar_service import SonarService
from local_communication_service import LocalCommunicationService as local_communication_service
import time
import threading
import os
import snowboydecoder



class WaitForTriggerService:
    __interrupted = False
    __will_stop = False
    __small_distance_sonar_counter = 0
    __very_small_distance_sonar_counter = 0    

    def detected_teddy(self):
        self.__will_stop = True
        RGBLedService.getInstance().set_color(1, 0, 0)
        print "Teddy Detected"
        local_communication_service.getInstance().write_hotword("teddy")
        self.terminate_detector()

    def detected_explore(self):
        self.__will_stop = True
        RGBLedService.getInstance().set_color(1, 0, 0)
        print "Explore Detected"
        local_communication_service.getInstance().write_hotword("explore")
        self.terminate_detector()

    def detected_french(self):  
        self.__will_stop = True      
        RGBLedService.getInstance().set_color(1, 0, 0)
        print "French Detected"
        local_communication_service.getInstance().write_hotword("french")
        self.terminate_detector()

    def detected_english(self):
        self.__will_stop = True
        RGBLedService.getInstance().set_color(1, 0, 0)
        print "English Detected"
        local_communication_service.getInstance().write_hotword("english")
        self.terminate_detector()

    def detected_shutdown(self):   
        #self.__will_stop = True     
        #RGBLedService.getInstance().set_color(1, 0, 0)
        print "Shutdown Detected"
        #local_communication_service.getInstance().write_hotword("shutdown")
        #self.terminate_detector()

    def terminate_detector(self):
        self.__interrupted = True
        self.detector.terminate()

    def interrupt_callback(self):
        return self.__interrupted

    def watch_sonar(self):
        print (self.__will_stop)
        while (not self.__interrupted and not self.__will_stop):
            distance = self.sonar_service.measure()
            #print(distance)
            if (distance < 15):
                RGBLedService.getInstance().set_color(1, 1, 1)
                self.__very_small_distance_sonar_counter = self.__very_small_distance_sonar_counter + 1
            else:
                self.__very_small_distance_sonar_counter = 0
                if(distance < 55):
                    RGBLedService.getInstance().set_color(0, 1, 0)
                    self.__small_distance_sonar_counter = self.__small_distance_sonar_counter + 1
                else:
                    #RGBLedService.getInstance().set_color(0, 0, 1)
                    self.__small_distance_sonar_counter = 0

            if (self.__small_distance_sonar_counter > 3):
                print ("self.__small_distance_sonar_counter > 3")
                self.detected_explore()

            if (self.__very_small_distance_sonar_counter > 3):
                self.detected_teddy()

    def main(self):
        RGBLedService.getInstance().set_color(0, 0, 1)
        self.sonar_service = SonarService.getInstance()

        sonar_thread = threading.Thread(target=self.watch_sonar)
        sonar_thread.daemon = True
        sonar_thread.start()

        models = ["./snowboy_models/teddy.mdl", "./snowboy_models/explore.mdl", "./snowboy_models/french.mdl", "./snowboy_models/english.mdl", "./snowboy_models/shutdown.mdl"]
        self.detector = snowboydecoder.HotwordDetector(models, sensitivity=0.5, audio_gain=1)

        callbacks = [self.detected_teddy,
                     self.detected_explore,
                     self.detected_french,
                     self.detected_english,
                     self.detected_shutdown]

        self.detector.start(detected_callback=callbacks, interrupt_check=self.interrupt_callback)


wait_for_trigger_service = WaitForTriggerService()
wait_for_trigger_service.main()
