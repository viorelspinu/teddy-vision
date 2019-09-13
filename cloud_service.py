from google_cloud_service import GoogleCloudService


class CloudService:

    def __init__(self):
        print("init")

    def do_vision_post(self, image_path):
        google_cloud_service = GoogleCloudService()
        return google_cloud_service.do_vision_post(image_path)

    def do_translate_post(self, text, language_code):
        google_cloud_service = GoogleCloudService()
        return google_cloud_service.do_translate_post(text, language_code)

    def do_text_to_speech_post(self, text, language_code, voice_code, ssml=False):
        google_cloud_service = GoogleCloudService()
        return google_cloud_service.do_text_to_speech_post(text, language_code, voice_code, ssml)

    def process_photo(self, photo_file, mp3_out_file):
        google_cloud_service = GoogleCloudService()
        return google_cloud_service.process_photo(photo_file, mp3_out_file)

    def speak(self, input_text, language_code, voice_code):
        google_cloud_service = GoogleCloudService()
        google_cloud_service.speak(input_text, language_code, voice_code)
