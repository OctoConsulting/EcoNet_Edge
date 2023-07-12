import pyaudio
import wave
import simple_websocket

import pyaudio
import wave
import os
import sys
from datetime import datetime

CHUNK = 115200*10
FORMAT = pyaudio.paInt16
CHANNELS = 4
RATE = 96000
audios = []

start_time = datetime.now().strftime("%H-%M-%S")

ws = simple_websocket.Client('ws://192.168.50.203:5000/api/detection/audio')

p = pyaudio.PyAudio()

device_index = 1  # Specify the index of the input device you want to use

input_info = p.get_device_info_by_index(device_index)
print(f"Using input device: {input_info['name']}")

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                input_device_index=device_index,
                frames_per_buffer=CHUNK)


print("Recording started...")

try:
    i = 0
    while True:
        data = stream.read(115200)

        timestamp = datetime.now().strftime("%H-%M-%S")

        output = f'{str(timestamp)}_audio.wav'

        file_path = os.path.join("./audio_archive/clips", output)

        f = open(file_path, "x")
        f.close()
        
        with wave.open(file_path, 'wb') as f:
            f.setnchannels(4)
            f.setsampwidth(p.get_sample_size(FORMAT))
            f.setframerate(96000)
            f.writeframes(data)

        audios.append(data)

        ws.send(data)
        ws.send(str(timestamp))

        
    
except KeyboardInterrupt:
    # end_time = datetime.now().strftime("%H-%M-%S")

    # output = f'{start_time}_to_{end_time}_audio.wav'

    # file_path = os.path.join("./audio_archive/full_audio", output)

    # full = b''.join(audios)

    # f = open(file_path, "x")
    # f.close()

    # with wave.open(file_path) as f:
    #     f.setnchannels(4)
    #     f.setsampwidth(p.get_sample_size(FORMAT))
    #     f.setframerate(96000)
    #     f.writeframes(b''.join(audios))
    
    # stream.stop_stream()
    # stream.close()
    # p.terminate()

    sys.exit()






