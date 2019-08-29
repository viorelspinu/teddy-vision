../conf/restore_sound_volume.sh
python ./record_respearker.py
ffmpeg -i ./hello.wav -ar 11025 -ac 2 output.wav -y
omxplayer ./wav/one_sec.wav
export PROJECT_ID=teddy-8b681
export DEVICE_ID=teddy-8b681-teddy-google-assistant-dlmtw8
googlesamples-assistant-pushtotalk --project-id $PROJECT_ID --device-model-id $DEVICE_ID --input-audio-file ./output.wav --output-audio-file ./response.wav
aplay ./response.wav
sleep 0.5