from lomond import WebSocket
from lomond.persist import persist
from cloud_service import CloudService
from datetime import datetime
from voice_codes_constants import *
import simplejson as json
from configuration_service import ConfigurationService
from subprocess import Popen, PIPE
import time
import requests

websocket = WebSocket('http://116.203.129.161:80/chat')
cloud_service = CloudService()
configuration_service = ConfigurationService.getInstance()

for event in persist(websocket):
    if event.name == "ready":
        print("ready")
    elif event.name == "text":
        text = event.text
        print(text)
        if (text.startswith("__SPEAK__")):
            text = text.replace("__SPEAK__", "")
            parts = text.split("_#_#_")
            cloud_service.speak(parts[1], parts[0])
            now = datetime.now()
            date_string = now.strftime("%d/%m/%Y %H:%M:%S")
            with open("remote_speech_log.txt", "a") as myfile:
                myfile.write(date_string + ": " + event.text + "\r\n")
                myfile.close()

        if (text.startswith("__SENSITIVITY__")):
            text = text.replace("__SENSITIVITY__", "")
            json_sensitivity = json.loads(text)
            configuration_service.set_sensitivities(json_sensitivity)

        if (text.startswith("__REQUEST_CONFIGURATION__")):
            text = text.replace("__REQUEST_CONFIGURATION__", "")
            websocket.send_text("__REQUEST_RESPONSE__" + json.dumps(configuration_service.read_configuration()).decode('utf8'))

        if (text.startswith("__NGROK__")):
            ngrok_path = "./start_ngrok.sh"
            p = Popen(["nohup", ngrok_path])
            time.sleep(5)

            r = requests.get("http://localhost:4040/api/tunnels")
            tunnel = r.json()["tunnels"][0]["public_url"]            
            ssh_message = "ssh vertigo@{} -p {}".format(tunnel[6:tunnel.index(':', 5)], tunnel[tunnel.index(':', 5)+1:])
            print (ssh_message)
