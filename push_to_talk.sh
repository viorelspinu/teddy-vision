cd conf
./restore_sound_volume.sh
cd ..
python ./record_audio_service.py
ffmpeg -i ./hello.wav -ar 11025 -ac 2 output.wav -y
aplay ./wav/one_sec.wav
export PROJECT_ID=teddy-assistant
export DEVICE_ID=teddy-assistant-teddy-o07wiz
googlesamples-assistant-pushtotalk --project-id $PROJECT_ID --device-model-id $DEVICE_ID --input-audio-file ./output.wav --output-audio-file ./assistant_response.wav
ffmpeg -i assistant_response.wav -filter:a "volume=7dB" assistant_response_loud.wav
aplay ./assistant_response_loud.wav
sleep 0.1