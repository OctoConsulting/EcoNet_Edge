import sys
import shutil
import os
def process_audio(input_path):
    try:
        # Read the input WAV file
        # Do any processing on the audio data here
        # For demonstration purposes, this example simply copies the input file to a new output file
        directory_path = 'big/subprocess/'
        output_filename = input_path.rsplit('.', 1)[0]  # Remove the extension
        output_path = output_filename + '_processed.wav'
        #file_path = os.path.join(directory_path, output_path)
        global Finalout
        Finalout = directory_path + output_path
        #CODE IS USED TO ASSMUME DIFFRENT NAME OF FILE AND SAVE IN CORRECT DIRECTORY
        shutil.copyfile(input_path, Finalout)

      

    except Exception as e:
        sys.stderr.write(str(e))
        sys.exit(1)

if __name__ == '__main__':
    # Expecting the input WAV file path as a command-line argument
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: python audioPlayer.py <input_wav_file>\n')
        sys.exit(1)
    #takes in argument from client.py
    input_wav = sys.argv[1]
    #sends the argument to the function
    process_audio(input_wav)
    #sends the argument back into stdout to be read by mian
    sys.stdout.write(Finalout)


###GET ABSOLUTE PATH