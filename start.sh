#!/bin/bash

cd /home/pi/teddy-vision
export PATH=$PATH:/home/pi/.local/bin 

sudo kilall python

cd ./conf
./restore_sound_volume.sh
cd ..

./set_volume.sh

#go to https://console.developers.google.com/apis/credentials
export GOOGLE_API_KEY=__YOUR_GOOGLE_API_KEY___

aplay ./wav/up_and_running.wav
python ./configuration_service.py
python ./say_ip_address.py
python ./start_server.py &

while true
do
python ./wait_for_trigger.py

python ./run_action_on_hotword.py

sleep 0.5

done