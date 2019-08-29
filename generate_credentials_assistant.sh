ECHO "go to https://console.actions.google.com, create a project and register a device"

ECHO "do not forget to set OAuth consent in https://console.developers.google.com/apis/credentials/consent?project=teddy-assistant&duration=P1D"

pip install --upgrade google-auth-oauthlib[tool] --user

export PATH=$PATH://home/pi/.local/bin/

export FILE_SECRETS_PATH=""

google-oauthlib-tool --scope https://www.googleapis.com/auth/assistant-sdk-prototype \
      --scope https://www.googleapis.com/auth/gcm \
      --save --headless --client-secrets $FILE_SECRETS_PATH

