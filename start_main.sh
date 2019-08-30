#!/bin/bash
cd ./conf
./restore_sound_volume.sh
cd ..
amixer sset 'PCM' 100%

while true
do
python ./wait_for_hotword_snowboy.py


python ./run_action_on_hotword.py

sleep 0.5

done