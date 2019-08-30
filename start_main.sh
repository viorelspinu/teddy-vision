#!/bin/bash
cd ./conf
./restore_sound_volume.sh
cd ..
amixer sset 'PCM' 85%

#go to https://console.developers.google.com/apis/credentials
export GOOGLE_API_KEY=__YOUR_GOOGLE_API_KEY___


while true
do
python ./wait_for_hotword_snowboy.py


python ./run_action_on_hotword.py

sleep 0.5

done