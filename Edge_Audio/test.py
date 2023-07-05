import pyaudio
import wave

# p = pyaudio.PyAudio()
# for i in range(p.get_device_count()):
#     if p.get_device_info_by_index(i)['']
#     print(p.get_device_info_by_index(i))

import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 4
RATE = 44100
RECORD_SECONDS = 1.2
OUTPUT_FILENAME = "output.wav"

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

frames = []

print("Recording started...")

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Recording finished.")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

print(f"Audio saved to {OUTPUT_FILENAME}.")
