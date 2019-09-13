from sonar_service import SonarService

class VisionEventsLogger:

    def main(self):
        while (True):
            distance = SonarService.getInstance().measure()
            print(distance)