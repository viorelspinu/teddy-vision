cd conf
./restore_sound_volume.sh
cd ..
python ./record_audio_service.py
(($? != 0)) && { printf '%s\n' "Command exited with non-zero"; exit 1; }
ffmpeg -i ./hello.wav -ar 11025 -ac 2 output.wav -y > /dev/null 2>&1 < /dev/null
aplay ./wav/one_sec.wav
export PROJECT_ID=teddy-assistant
export DEVICE_ID=teddy-assistant-teddy-o07wiz
googlesamples-assistant-pushtotalk --project-id $PROJECT_ID --device-model-id $DEVICE_ID --input-audio-file ./output.wav --output-audio-file ./assistant_response.wav
ffmpeg -i assistant_response.wav -filter:a "volume=7dB" assistant_response_loud.wav -y > /dev/null 2>&1 < /dev/null
aplay ./assistant_response_loud.wav
sleep 0.1


#cp --backup ./assistant_response_loud.wav ./audio-logs/