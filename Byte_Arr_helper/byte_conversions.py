import base64

# this is a function that converts a byte array to base64 (this is needed to be able to send in JSON)
def convert_to_base64(byte_array):
    base64_bytes = base64.b64encode(byte_array)
    return base64_bytes.decode('utf-8')

# convert from base64 to a byte array
def convert_to_bytes(base64_bytes):
    return base64.b64decode(base64_bytes)


# this is how you make .wav file from byte array
# this is not a function this is just an example

    # with open('myfile.wav', mode='wb') as f:
    #     f.write(my_bytes)