#!/bin/bash

export PYTHONIOENCODING=UTF-8

cd /home/pi/teddy-vision
export PATH=$PATH:/home/pi/.local/bin 

sudo killall python 
cd ./conf
./restore_sound_volume.sh
cd ..

./set_volume.sh

#go to https://console.developers.google.com/apis/credentials
export GOOGLE_API_KEY=__YOUR_GOOGLE_API_KEY___

#go to https://portal.azure.com 
export SPEECH_SERVICE_KEY=__YOUR_MICROSOFT_COGNITIVE_SERVICES_API_KEY


aplay ./wav/up_and_running.wav
python ./configuration_service.py  >> /home/pi/configuration_service.log 2>&1
#python ./say_ip_address.py
python ./start_server.py  >> /home/pi/start_server.log 2>&1 &

./start_websocket_client.sh  >> /home/pi/start_websocket_client.log 2>&1 &

while true
do
python ./wait_for_trigger.py >> /home/pi/wait_for_trigger.log 2>&1

python ./run_action_on_hotword.py >> /home/pi/run_action_on_hotword.log 2>&1

sleep 0.5

done