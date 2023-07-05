import wave
from flask import Flask, request, jsonify, send_file
from flask_sock import Sock
import pyaudio

app = Flask(__name__)
sock = Sock(app)

#################################
# get audio from mic
#################################
@sock.route('/audio', methods=['GET'])
def get_audio(ws):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 4
    RATE = 44100

    RECORD_SECONDS = 1.2
    OUTPUT_FILENAME = "output.wav"

    p = pyaudio.PyAudio()

    device_index = 1  

    input_info = p.get_device_info_by_index(device_index)
    print(f"Using input device: {input_info['name']}")

    stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                input_device_index=device_index,
                frames_per_buffer=CHUNK)

    try:
        i = 0
        while True:
            data = stream.read(52920)
            ws.send(data)
            
            # wf = wave.open(f"audio{i}.wav", 'wb')
            # wf.setnchannels(channels)
            # wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
            # wf.setframerate(44100)
            # wf.writeframes(data)

            # duration_seconds = wf.getnframes() / wf.getframerate()
            # print(duration_seconds)
            # wf.close
            # i += 1
        
    except KeyboardInterrupt:
        pass
    stream.stop_stream()
    stream.close()
    p.terminate()
