import sys
import shutil

def process_audio(input_path):
    try:
        # Read the input WAV file
        # Do any processing on the audio data here
        # For demonstration purposes, this example simply copies the input file to a new output file
        global output_filename
        output_filename = input_path.rsplit('.', 1)[0]  # Remove the extension
        output_path = output_filename + '_processed.wav'
        shutil.copyfile(input_path, output_path)
    except Exception as e:
        sys.stderr.write(str(e))
        sys.exit(1)

if __name__ == '__main__':
    # Expecting the input WAV file path as a command-line argument
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: python audioPlayer.py <input_wav_file>\n')
        sys.exit(1)

    input_wav = sys.argv[1]
    process_audio(input_wav)
    sys.stdout.write(output_filename)
