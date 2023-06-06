import io
import wave
from flask import Flask, request
from base64 import b64encode

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert():
    # Get the byte array from the request body
    byte_array = request.data

    # Create a file-like object in memory
    file = io.BytesIO(byte_array)

    # Open the file-like object as a wave file
    with wave.open('snesw.wav', 'wb') as wave_file:
        wave_file.setnchannels(1)
        wave_file.setsampwidth(2)
        wave_file.setframerate(44100)

        # Write the byte array to the wave file
        wave_file.writeframes(byte_array)

    # Write the byte array to a binary file
    with open('snesw.bin', 'wb') as f:
        f.write(byte_array)

    # Return the byte array as a response
    return byte_array

if __name__ == '__main__':
    app.run()