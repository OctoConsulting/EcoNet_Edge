import pyaudio
import wave
import time

audio_format = pyaudio.paInt16

channels = 1 
sample_rate = 44100
chunk_size = 512

audio = pyaudio.PyAudio()

stream = audio.open(format=audio_format, channels=channels, rate=sample_rate, input=True, frames_per_buffer=chunk_size, input_device_index=0)

frame = []

#Start Recording

print("Recording Started. Press Ctrl + C to stop recording")
try:
        while True:

                data = stream.read(80)
                #print(data)
                #print("-----")
                #data = ws.receive()
                                #wf.writeframes(data)
                frame.append(data)

except KeyboardInterrupt:
        pass
stream.stop_stream()
stream.close()
audio.terminate()

##################################
##################################
##################################
##################################
##################################
wf = wave.open("Testing.wav", 'wb')
wf.setnchannels(channels)
wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
wf.setframerate(44100)
wf.writeframes(b''.join(frame))
wf.close
print("Recording Stopped.")
