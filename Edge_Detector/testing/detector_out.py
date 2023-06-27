from flask import jsonify
import json
import random
import sys
import shutil
import os
import time

#write to standard out and send to standard in "stdout" and "stdin"
#return a dictionary with the contents of the file as a byte array and a boolean
def main(file):
    try:
        # Do any processing on the audio data here
        # For demonstration purposes, this example simply copies the input file to a new output file
        randomN = random.randint(0, 1)
                
        output_filename = file.rsplit('.', 1)[0]  # Remove the extension
        output_path = output_filename + '_processed.wav'
        
        global Finalout
        Finalout = output_path
        #CODE IS USED TO ASSMUME DIFFRENT NAME OF FILE AND SAVE IN CORRECT DIRECTORY
        shutil.copyfile(file, Finalout)

        shot = False
        if randomN == 1:
             shot = True

        resp = {}
        resp['shot'] = shot
        resp['audio'] = Finalout

        r = json.dumps(resp)
        time.sleep(11)
        return r
        
    except Exception as e:
        sys.stderr.write(str(e))
        sys.exit(1)

if __name__ == '__main__':
    sys.stdout.write(main(sys.argv[1]))