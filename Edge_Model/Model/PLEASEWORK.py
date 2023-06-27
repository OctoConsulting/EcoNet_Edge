import pyaudio
import numpy as np
import time
import subprocess
import os
import sys
import torch





def callback(in_data, frame_count, time_info, flag):

    model = torch.load(MODEL_PATH, map_location=torch.device('cpu'))

    audio_data = np.frombuffer(in_data, dtype=np.float32)
    audio_data = librosa.resample(audio_data, 44100, 22050)
    ringBuffer.append(audio_data)

    # Convert audio data to a PyTorch tensor
    audio_tensor = torch.from_numpy(np.array(ringBuffer.get())).unsqueeze(0).unsqueeze(0)

    # Normalize the audio tensor if needed
    # audio_tensor = normalize(audio_tensor)

    # Make predictions using the PyTorch model
    predictions = model(audio_tensor)

    # Process the predictions as needed
    # ...

    return (in_data, pyaudio.paContinue)

pa = pyaudio.PyAudio()

stream = pa.open(format=pyaudio.paFloat32,
                 channels=1,
                 rate=44100,
                 output=False,
                 input=True,
                 frames_per_buffer=22050,  # Adjust the frame size to 1 second (22050 samples for 1 second at 22050 Hz)
                 stream_callback=callback)

# Start the stream
stream.start_stream()

i = 0  # This is just an alternative to breaking the loop

while stream.is_active():
    time.sleep(0.25)

    i += 1

    if i >= 100:
        break

stream.close()
pa.terminate()

play(QUIET_TRACK)
subprocess.getoutput(PAUSE_COMMAND)
print("Program terminated.\n")
