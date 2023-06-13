import base64

def read_wav_file(file_path):
    with open(file_path, 'rb') as file:
        wav_data = file.read()
    return bytearray(wav_data)

def convert_to_base64(byte_array):
    base64_bytes = base64.b64encode(byte_array)
    return base64_bytes.decode('utf-8')

def write_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

# Specify the path to your .wav file
file_path = 'input_processed.wav'

# Read the .wav file and convert it to a byte array
wav_byte_array = read_wav_file(file_path)

# Convert the byte array to a Base64-encoded string
base64_string = convert_to_base64(wav_byte_array)

output_file_path = "out.txt"

write_to_file(output_file_path, base64_string)