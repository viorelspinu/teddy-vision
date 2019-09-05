echo "go to https://console.actions.google.com, create a project and register a device"
echo "do not forget to set OAuth consent in https://console.developers.google.com/apis/credentials/consent?project=teddy-assistant&duration=P1D"

echo "download the json credentials file for your project from https://console.actions.google.com/project/teddy-assistant/deviceregistration/"
echo "copy the downloaded json file to raspberry pi and export the FILE_SECRETS_PATH variable to point to the json file"

pip install --upgrade google-auth-oauthlib[tool] --user

export PATH=$PATH:/home/pi/.local/bin/


cd ..

google-oauthlib-tool --scope https://www.googleapis.com/auth/assistant-sdk-prototype \
      --scope https://www.googleapis.com/auth/gcm \
      --save --headless --client-secrets $FILE_SECRETS_PATH

sudo mkdir /root/.config/
sudo mkdir /root/.config/google-oauthlib-tool/
sudo cp  /home/pi/.config/google-oauthlib-tool/credentials.json  /root/.config/google-oauthlib-tool/credentials.json