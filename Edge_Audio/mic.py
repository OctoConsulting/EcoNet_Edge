import pyaudio
import wave
import time
import os
import glob

CHUNK = 52920 * 10
FORMAT = pyaudio.paInt16
CHANNELS = 4
RATE = 44100
RECORD_SECONDS = 1.2
OUTPUT_FOLDER = "Edge_Audio/savedSegments/"
OUTPUT_FILENAME = "segment"

p = pyaudio.PyAudio()

device_index = 1  # Specify the index of the input device you want to use

input_info = p.get_device_info_by_index(device_index)
print(f"Using input device: {input_info['name']}")

stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    input_device_index=device_index,
    frames_per_buffer=CHUNK,
)

print("Recording started...")
segments = []  # List to store the filenames of audio segments

try:
    i = 0
    while True:
        data = stream.read(int(RATE * RECORD_SECONDS))

        # Save the audio segment to a file
        timestamp = str(int(time.time()))  # Using UNIX timestamp as part of the file name
        output_filename = f"{OUTPUT_FILENAME}_{timestamp}.wav"
        output_filepath = os.path.join(OUTPUT_FOLDER, output_filename)
        with wave.open(output_filepath, 'wb') as f:
            f.setnchannels(CHANNELS)
            f.setsampwidth(p.get_sample_size(FORMAT))
            f.setframerate(RATE)
            f.writeframes(data)

        segments.append(output_filepath)  # Add filepath to the segments list
        print(f"Segment {i}: {output_filepath}")
        i += 1

except KeyboardInterrupt:
    pass

stream.stop_stream()
stream.close()
p.terminate()

OUTPUT_FOLDER = "Edge_Audio/Final/"
OUTPUT_FILENAME = "Final"
timestamp = str(int(time.time()))  # Using UNIX timestamp as part of the file name
output_filename = f"{OUTPUT_FILENAME}_{timestamp}.wav"
output_filepath = os.path.join(OUTPUT_FOLDER, output_filename)

# Combine audio segments into a single file
with wave.open(output_filepath, "wb") as output_file:
    for audio_filepath in segments:
        with wave.open(audio_filepath, "rb") as segment:
            if not output_file.getnframes():
                # Set the output file's parameters based on the first segment
                output_file.setparams(segment.getparams())
            output_file.writeframes(segment.readframes(segment.getnframes()))

print("Combined segments into", f"{OUTPUT_FILENAME}.wav")
