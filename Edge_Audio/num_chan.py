import wave

def get_channel_count(filename):
    with wave.open(filename, 'rb') as wav_file:
        return wav_file.getnchannels()

# Example usage
filename = 'output.wav'
channel_count = get_channel_count(filename)
print(f"The file '{filename}' has {channel_count} channel(s).")
