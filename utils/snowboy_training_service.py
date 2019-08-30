import sys
import base64
import requests

def get_wave(fname):
    with open(fname) as infile:
        return base64.b64encode(infile.read())

endpoint = "https://snowboy.kitt.ai/api/v1/train/"

#your snowboy api key, get it from https://snowboy.kitt.ai/dashboard
#check https://pimylifeup.com/raspberry-pi-snowboy/ if not clear how to do that
token = os.environ['SNOWBOY_API_KEY']
if (token == None):
    print ("export SNOWBOY_API_KEY=__api_key__")


hotword_name = "teddy"

language = "en"
age_group = "20_29"
gender = "M"
microphone = "usb microphone"

if __name__ == "__main__":
    try:
        [_, wav1, wav2, wav3, out] = sys.argv
    except ValueError:
        print "Usage: %s wave_file1 wave_file2 wave_file3 out_model_name" % sys.argv[0]
        sys.exit()

    data = {
        "name": hotword_name,
        "language": language,
        "age_group": age_group,
        "gender": gender,
        "microphone": microphone,
        "token": token,
        "voice_samples": [
            {"wave": get_wave(wav1)},
            {"wave": get_wave(wav2)},
            {"wave": get_wave(wav3)}
        ]
    }

    response = requests.post(endpoint, json=data)
    if response.ok:
        with open(out, "w") as outfile:
            outfile.write(response.content)
        print "Saved model to '%s'." % out
    else:
        print "Request failed."
        print response.text