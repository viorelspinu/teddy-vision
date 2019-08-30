#!/bin/bash
cd ./conf
./restore_sound_volume.sh
cd ..
amixer sset 'PCM' 100%

while true
do
python ./wait_for_hotword_snowboy.py
aplay ./wav/yes_sir.wav
./push_to_talk.sh
sleep 0.5
done