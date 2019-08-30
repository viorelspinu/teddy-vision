diskutil list

if [ "$SD_PATH" = "" ]; then
    echo "run export SD_PATH=/dev/disk_??? first"
    exit 1
fi

#/Users/viorels/Desktop/raspberrypi.dmg

if [ "$IMAGE_FILE" = "" ]; then
    echo "run export IMAGE_FILE=_image_file_path first"
    exit 1
fi


sudo dd of=$SD_PATH if=$IMAGE_FILE bs=1m