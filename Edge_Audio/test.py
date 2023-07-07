import pyaudio
import wave
import simple_websocket

import pyaudio
import wave

CHUNK = 52920*10
FORMAT = pyaudio.paInt16
CHANNELS = 4
RATE = 44100
RECORD_SECONDS = 1.2
OUTPUT_FILENAME = "output.wav"

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
        data = stream.read(52920)
        ws.send(data)

        
    
except KeyboardInterrupt:
    pass
stream.stop_stream()
stream.close()
p.terminate()
