import pyaudio
import wave
import struct
import math


class RecordAudioService:

    RESPEAKER_RATE = 16000
    RESPEAKER_CHANNELS = 4
    RESPEAKER_WIDTH = 2
    # run getDeviceInfo.py to get index
    RESPEAKER_INDEX = 2
    CHUNK = 1024
    RECORD_SECONDS = 30
    WAVE_OUTPUT_FILENAME = "hello.wav"

    SHORT_NORMALIZE = (1.0/32768.0)
    chunk = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 11250
    swidth = 2

    def __init__(self):
        self.p = pyaudio.PyAudio()

    def record(self):
        self.stream = self.p.open(
            rate=self.RESPEAKER_RATE,
            format=self.p.get_format_from_width(self.RESPEAKER_WIDTH),
            channels=self.RESPEAKER_CHANNELS,
            input=True,
            input_device_index=self.RESPEAKER_INDEX,)
        self.frames = []

        silence_count = 0

        for i in range(0, int(self.RESPEAKER_RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = self.stream.read(self.CHUNK)
            rms_value = self.rms(data)
            self.frames.append(data)
            print(rms_value)
            if (rms_value < 90):
                silence_count = silence_count + 1
            else:
                silence_count = 0

            if (silence_count > 5):
                if (i > 30):
                    break

        print("* done recording")

        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

        wf = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(self.RESPEAKER_CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.p.get_format_from_width(self.RESPEAKER_WIDTH)))
        wf.setframerate(self.RESPEAKER_RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

    def rms(self, frame):
        count = len(frame) / self.swidth
        format = "%dh" % (count)
        shorts = struct.unpack(format, frame)

        sum_squares = 0.0
        for sample in shorts:
            n = sample * self.SHORT_NORMALIZE
            sum_squares += n * n
        rms = math.pow(sum_squares / count, 0.5)

        return rms * 1000


record_audio_service = RecordAudioService()
record_audio_service.record()