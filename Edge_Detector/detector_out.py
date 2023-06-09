from flask import jsonify
import json
import random
import sys
import shutil
import os

#write to standard out and send to standard in "stdout" and "stdin"
#return a dictionary with the contents of the file as a byte array and a boolean
def main():
    try:
        # Do any processing on the audio data here
        # For demonstration purposes, this example simply copies the input file to a new output file
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

        shot = False
        if randomN == 1:
             shot = True

        resp = {}
        resp["shot"] = shot
        resp["filePath"] = final_output

        r = json.dumps(resp)

        return r
        
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
    sys.stdout.write(main())

#curl -X POST http://127.0.0.1:8003/api/detectShot
#curl -X POST http://127.0.0.1:8000/api/detection/detectShot

# self._status, self._status_code = self._clean_status(value)
# shot_detect         |   File "/usr/local/lib/python3.9/site-packages/werkzeug/sansio/response.py", line 197, in _clean_status
# shot_detect         |     value = value.strip()
# shot_detect         | AttributeError: 'Response' object has no attribute 'strip'
# shot_detect         | 172.18.0.4 - - [09/Jun/2023 20:10:51] "POST /api/detectShot HTTP/1.1" 500 -
# api                 | 172.18.0.1 - - [09/Jun/2023 20:10:51] "POST /api/detection/detectShot HTTP/1.1" 200 
