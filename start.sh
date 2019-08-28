#!/bin/bash

while true
do
python ./snowboy_sample.py
omxplayer ../wav/yes_sir.wav
./push_to_talk.sh
sleep 0.5
done