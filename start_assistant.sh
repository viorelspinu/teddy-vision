#!/bin/bash
cd ./conf
./restore_sound_volume.sh
cd ..

while true
do
cd ./snowboy
python ./snowboy_sample.py
cd ..
aplay ./wav/yes_sir.wav
./push_to_talk.sh
sleep 0.5
done