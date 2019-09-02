if [ -z "$1" ] 
then
    echo "record.sh _output_file_name_"
    exit 1
fi
arecord -Dac108 -f S32_LE -r 16000 -c 4 -d 2 $1

sox -t wav $1 -t wav -r 16000 -b 16 -e signed-integer -c 1 $1_p