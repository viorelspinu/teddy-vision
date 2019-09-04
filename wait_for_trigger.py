
import sys
sys.path.append('./snowboy')
import snowboydecoder
import os
import threading
import time
from local_communication_service import LocalCommunicationService as local_communication_service
from digital_sensor_distance_service import DigitalSensorDistanceService
from sonar_service import SonarService
from rgb_led_service import RGBLedService


class WaitForTriggerService:
    __interrupted = False
    __will_stop = False
    __small_distance_sonar_counter = 0
    __very_small_distance_sonar_counter = 0
    __digital_distance_counter = 0

    def detected_teddy(self):
        self.__will_stop = True
        print "Teddy Detected"
        local_communication_service.getInstance().write_hotword("teddy")
        RGBLedService.getInstance().set_color(1, 0, 0)
        self.terminate_detector()

    def detected_explore(self):
        self.__will_stop = True
        print "Explore Detected"
        local_communication_service.getInstance().write_hotword("explore")
        RGBLedService.getInstance().set_color(1, 0, 0)
        self.terminate_detector()

    def detected_french(self):
        self.__will_stop = True
        print "French Detected"
        local_communication_service.getInstance().write_hotword("french")
        RGBLedService.getInstance().set_color(1, 0, 0)
        self.terminate_detector()

    def detected_english(self):
        self.__will_stop = True
        print "English Detected"
        local_communication_service.getInstance().write_hotword("english")
        RGBLedService.getInstance().set_color(1, 0, 0)
        self.terminate_detector()

    def detected_german(self):
        self.__will_stop = True
        print "German Detected"
        local_communication_service.getInstance().write_hotword("german")
        RGBLedService.getInstance().set_color(1, 0, 0)
        self.terminate_detector()

    def detected_shutdown(self):
        self.__will_stop = True
        print "Shutdown Detected"
        local_communication_service.getInstance().write_hotword("shutdown")
        RGBLedService.getInstance().set_color(1, 0, 0)
        self.terminate_detector()

    def terminate_detector(self):
        self.__interrupted = True
        self.detector.terminate()

    def interrupt_callback(self):
        return self.__interrupted

    def watch_distance_sensor(self):
        while (not self.__interrupted and not self.__will_stop):
            active = not self.digital_distance_sensor.measure()

            if (active):
                self.__digital_distance_counter = self.__digital_distance_counter + 1
            else:
                self.__digital_distance_counter = 0

            print(self.__digital_distance_counter)

            if (self.__digital_distance_counter > 50):
                print("detected tedy")
                print(self.__digital_distance_counter)
                #self.detected_teddy()
            time.sleep(0.01)

    def watch_sonar(self):
        while (not self.__interrupted and not self.__will_stop):
            distance = self.sonar_service.measure()
            # print(distance)
            if (distance < 15):
                RGBLedService.getInstance().set_color(1, 1, 1)
                self.__very_small_distance_sonar_counter = self.__very_small_distance_sonar_counter + 1
            else:
                self.__very_small_distance_sonar_counter = 0
                if(distance < 55):
                    RGBLedService.getInstance().set_color(0, 1, 0)
                    self.__small_distance_sonar_counter = self.__small_distance_sonar_counter + 1
                else:
                    RGBLedService.getInstance().set_color(0, 0, 1)
                    self.__small_distance_sonar_counter = 0

            if (self.__small_distance_sonar_counter > 3):
                print("self.__small_distance_sonar_counter > 3")
                self.detected_explore()

            if (self.__very_small_distance_sonar_counter > 3):
                self.detected_teddy()

    def main(self):
        RGBLedService.getInstance().set_color(0, 0, 1)
        self.sonar_service = SonarService.getInstance()
        self.digital_distance_sensor = DigitalSensorDistanceService.getInstance()

        sonar_thread = threading.Thread(target=self.watch_sonar)
        sonar_thread.daemon = True
        sonar_thread.start()

        distance_thread = threading.Thread(target=self.watch_distance_sensor)
        distance_thread.daemon = True
        distance_thread.start()


        models = ["./snowboy_models/listen.mdl", "./snowboy_models/explore.mdl", "./snowboy_models/french.mdl",
                  "./snowboy_models/english.mdl", "./snowboy_models/shutdown.mdl", "./snowboy_models/german.mdl"]

        sensitivity = [0.4, 0.4, 0.4, 0.4, 0.4, 0.4]

        self.detector = snowboydecoder.HotwordDetector(models, sensitivity=sensitivity, audio_gain=1)

        callbacks = [self.detected_teddy,
                     self.detected_explore,
                     self.detected_french,
                     self.detected_english,
                     self.detected_shutdown,
                     self.detected_german,
                     ]

        self.detector.start(detected_callback=callbacks, interrupt_check=self.interrupt_callback)


wait_for_trigger_service = WaitForTriggerService()
wait_for_trigger_service.main()
