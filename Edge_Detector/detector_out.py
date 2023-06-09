from flask import Flask, request, jsonify
from flask_sock import Sock
import random
import sys
import shutil
import os

app = Flask(__name__)
sock = Sock(app)

#write to standard out and send to standard in "stdout" and "stdin"
#return a dictionary with the contents of the file as a byte array and a boolean
def main():
    try:
        # Do any processing on the audio data here
        # For demonstration purposes, this example simply copies the input file to a new output file
        global output_filename
        global final_output
        randomN = random.randint(0, 1)
        directory_path = ""
        
        filename = "output.txt"
        with open(filename, "w") as f:
            if randomN == 1:
                f.write(str("Shot Detected!"))
            else:
                f.write(str("No Shot Detected!"))

        with open(filename, 'r')as f:
            contents = f.read()

        output_filename = filename.rsplit('.', 1)[0]  # Remove the extension
        output_path = output_filename + '_processed.txt'
        final_output = directory_path + output_path
        shutil.copyfile(filename, final_output)
    except Exception as e:
        sys.stderr.write(str(e))
        sys.exit(1)

if __name__ == '__main__':
    # if len(sys.argv) != 2:
    #     sys.stderr.write('Usage: python audioPlayer.py <input_wav_file>\n')
    #     sys.exit(1)
    #takes in argument from client.py

    #shotD = sys.argv[1]

    #sends the argument to the function

    #process_audio(shotD)
    #sends the argument back into stdout to be read by mian
    main()
    sys.stdout.write(final_output)

