from sonar_service import SonarService
from cloud_service import CloudService
from camera_service import CameraService
import simplejson as json


class VisionEventsLogger:

    def main(self):
        while (True):
            distance = SonarService.getInstance().measure()
            if (distance < 220):
                camera_service = CameraService()
                cloud_service = CloudService()
                camera_service.take_photo("photo.jpg")
                vision_response = cloud_service.do_vision_post("photo.jpg")
                json_vision_response = json.loads(vision_response)
                try:
                    rows = json_vision_response['responses'][0]['labelAnnotations']
                except:
                    print(json_vision_response)
                    return
                data = ""
                for item in rows:
                    data = data + str(item['description']) + ","
                print(data)


vision_logger = VisionEventsLogger()
vision_logger.main()
