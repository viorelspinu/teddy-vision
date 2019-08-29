#!/bin/bash

while true
do
cd ./snowboy
python ./snowboy_sample.py
cd ..
omxplayer ./wav/yes_sir.wav
./push_to_talk.sh
sleep 0.5
done