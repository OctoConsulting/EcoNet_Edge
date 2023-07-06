import sys
import logging
#from pydub import AudioSegment
import numpy as np
import pywt
import pywt.data
import librosa 
import array
import soundfile 

log_file = 'conversion.log'
logging.basicConfig(level=logging.INFO, filename=log_file, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')

import sys
if 'debug' not in ''.join(sys.argv): 
    sys.stderr = open('./stderr.txt', 'a')

# * I copied and pasted many of these methods from the soundUtil.py and wavelet.py files that is why there are so many


def denoise(input_file, output_file):

    #audio = AudioSegment.from_file(input_file)
    #dec_audio = decompose(audio)
    
    dec_audio, sr = soundfile.read(input_file, always_2d=1)
    dec_audio = dec_audio.T

    #wavelet denoising only active for 1 channel audio
    if dec_audio.shape[0] == 1:
        f=.5
        dec_audio = wavelet_denoise(dec_audio, [0*f, 0*f, 0*f, 10*f, 15.8*f, 22*f, 44.65*f], "hard", "rbio6.8")
    
    #Note must include sample rate for the audio data.
    cleaned_array = spectral_subtraction(np.array(dec_audio))

#    recomposed = recompose(cleaned_array, audio.frame_rate * 2, audio.sample_width)
    print(cleaned_array.shape)
    #AudioSegment.export(recomposed, output_file, format="wav")
    soundfile.write(output_file, cleaned_array.T, sr)
    
    logging.info("Denoised audio written to {}".format(output_file))

# #Coby Cockrell / Pete Downey
# based off of Coby's SpectralSubttraction_4Channel_optimized.py file
# edited to take in a slightly differnt output/input so its consistent with the other met


import numpy as np
from scipy.io import wavfile

def array_to_wav(array, sample_rate, output_file):
    """Converts an array of audio data to a WAV file.

    Args:
        array (ndarray): Array of audio data in the form [channel][time].
        sample_rate (int): Sample rate of the audio.
        output_file (str): Output file path for the WAV file.

    Returns:
        None
    """
    # Transpose the array to have shape [time][channel]
    transposed_array = np.transpose(array)

    # Scale the audio data to the range [-1, 1]
    normalized_array = transposed_array / np.max(np.abs(transposed_array))

    # Convert the audio data to the appropriate data type for writing to a WAV file
    wav_data = np.int16(normalized_array * 32767)

    # Write the WAV file
    wavfile.write(output_file, sample_rate, wav_data)


#This sections just converts the wav file into the decomposed audio array
import soundfile as sf
import numpy as np

def decompose_wav_to_array(input_file):
    # Load the multichannel audio using soundfile into audio and sample_rate
    audio, sample_rate = sf.read(input_file)
    print(sample_rate)

    # Transpose the audio to have shape [channel][time]
    audio = np.transpose(audio)

    return audio

import numpy as np
import librosa




#SPECTRAL SUBTRACTION
def spectral_subtraction(decAudio):
    """Runs spectral subtraction on deconstructed audio.

    Args:
        decAudio (arraylike): Deconstructed audio of form [channel][time]
        AudioSampleRate (int): Rate at which the audio samples.

    Returns:
        arraylike: Cleaned decAudio of form [channel][time].
    """
    # Convert audio to complex spectrogram
    compspectrogram = librosa.stft(decAudio)

    # Compute the magnitude and phase of the spectrogram
    magnitude = np.abs(compspectrogram)
    phase = np.angle(compspectrogram)

    clean_spectrogram = np.zeros_like(compspectrogram)

    # Apply spectral subtraction for each channel individually
    for ch in range(compspectrogram.shape[0]):
        # Estimate the noise floor and subtract it from the magnitude spectrogram
        noise_floor = np.min(magnitude[ch])
        clean_magnitude = np.maximum(magnitude[ch] - noise_floor, 0.0)

        # Reconstruct the complex spectrogram with the clean magnitude and original phase for the current channel
        clean_spectrogram[ch] = clean_magnitude * np.exp(1j * phase[ch])

    # Inverse STFT to obtain the cleaned audio
    clean_audio = librosa.istft(clean_spectrogram)

    # Normalize the data
    clean_audio /= np.max(np.abs(clean_audio))

    return clean_audio

# Example use:
#input_file = 'h3vr_white_102_0_932281.WAV'
#audio_array = decompose_wav_to_array(input_file)
#cleaned_array = spectral_subtraction(audio_array, 96000)

#array_to_wav(audio_array, 96000, 'outputReconstructedAudio.wav')

def wavelet_denoise(dec_audio, thresh_mult, type="hard", fam="db1"):
    """denoises audio using custom method

    Args:
        dec_audio (arraylike): audio of form [channel][time]
        thresh_mult (arraylike): multiplies sigma by this value to find cutoff values
        type (str, optional): type of thresholding. Defaults to "hard".
        fam (str, optional): faimly of wavelets used. Defaults to "db1".

    Returns:
        arraylike: denoised dec_audio
    """
    
    trans_audio = transform(dec_audio, len(thresh_mult)-1, fam)
    
    sigma = find_sigma(trans_audio)
    
    thres_values = compute_thresh(sigma, thresh_mult)
    
    trans_filtered_audio = _fast_denoise(trans_audio, thres_values, type)
    
    dec_filtered_audio = untransform(trans_filtered_audio, fam)

    return dec_filtered_audio

def _fast_denoise(trans_audio, thresh_values, type="hard"):
    """ \"Fast\" version of denoiser method works mainly by having precomputed sigma, trans_audio values
        this method should only be directly accessed if the same audio needs to be denoised multiple times
        is also used internally

    Args:
        trans_audio (arraylike): transformed audio of form [channel][passes][time]
        thresh_mult (arraylike): list of parameters of form [passes] that multiplies to find cutoff values

    Returns:
        arraylike: denoised tranformed audio of form [channel][passes][time]
    """
    channels = len(trans_audio)
    denoised_pass_C = [None]*channels
    
    for channels in range(len(trans_audio)):
        # pass 1 -> lowest C | pass N -> highest C
        #thresholds all passes in each channel
        denoised_pass_C[channels] = [pywt.threshold(trans_audio[channels][passes], 
                                                    thresh_values[channels][passes], mode=type) 
                                     for passes in range(len(trans_audio[channels]))]

    return denoised_pass_C

def find_sigma(trans_audio):
    """Finds sigma of an array of type [channel][passes]

     Args:
        trans_audio (arraylike): wavelet array of type [channel][passes][time]

    Returns:
        arraylike: sigma values of array type [channel][passes]
    """
    return [[np.median(np.absolute(passes - np.median(passes))) for passes in channel] for channel in trans_audio]

def compute_thresh(sigmoid, thresh_mult):
    """_summary_

    Args:
        sigmoid (arrylike): sigmoid values of form [channel][passes]
        thresh_mult (arraylike): threshold multiple values of form [passes]
    """
    thresh_values = [None] * len(sigmoid)
    for channel_index in range(len(sigmoid)):
        thresh_values[channel_index] = [sigmoid[channel_index][passes] * thresh_mult[passes] for passes in range(len(thresh_mult))]

    return thresh_values

def decompose(audio):
    """decomposes audiosegmant into raw audio

    Args:
        audio (AudioSegmant): audio file

    Returns:
        arraylike: raw audio of form [channel][time]
    """
    return [np.array(audio.split_to_mono()[channel].get_array_of_samples()) for channel in range(audio.channels)]

def recompose(audio, framerate, sample_width):
    """recomposes raw audio to Audiosegmant

    Args:
        audio (arraylike): decomposed audio of form [channel][time]
        framerate (float): framerate of audio
        sample_width (float): samplewidth of audio

    Returns:
        AudioSegment: returns the audiosegmant object
    """
    channels = len(audio)
    mono_channel_audio = [AudioSegment(array.array('i', np.array(channel).astype(int)), 
                              sample_width=sample_width, frame_rate=framerate,channels=1) 
                              for channel in audio]


    reconstucted_audio = mono_channel_audio[0]

    if (channels==2):
        reconstucted_audio = AudioSegment.from_mono_audiosegments(mono_channel_audio[0], mono_channel_audio[1])

    elif( channels == 4):
        reconstucted_audio = AudioSegment.from_mono_audiosegments(mono_channel_audio[0], mono_channel_audio[1], mono_channel_audio[2], mono_channel_audio[3]) 

    return reconstucted_audio

def untransform(trans_audio, fam="db1"):
    """Takes a wavelet array of the type [channel][passes][time] and reconstructs raw audio

    Args:
        trans_audio (arraylike): wavelet array of type [channel][passes][time]

    Returns:
        arraylike: reconstructs raw audio
    """
    return  [pywt.waverec(channel, fam, "smooth") for channel in trans_audio]


def transform(dec_audio, passes, fam="db1"):
    """Takes raw audio of form [channel][time] and desconstructs into wavelets
    Args:
        dec_audio (arraylike): audio of form [channel][time]
        passes (int): how many frequency passes the audio should be broken into

    Returns:
        arraylike: array of wavelets of form [channel][passes][time]
    """
    
    return [pywt.wavedec(channel, fam, 'smooth', level=passes) for channel in dec_audio]

if __name__ == "__main__":
    with open('stderr.txt', 'a'): 
        print('\n'*4)

    assert len(sys.argv) == 3 or 'debug' in ''.join(sys.argv), logging.error("Incorrect paramerters - Usage: python file.py input.wav output.wav")
    
    
        # Get the input and output file names from command-line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

        # Call the denoise function
    denoise(input_file, output_file)
    