import argparse
import json
import sys
import torch
import torchaudio
from torchvision.transforms import Compose, Normalize
from cnn import CNNNetwork


class AudioClassifier:
    def __init__(self, audio_file):
        # Define the transforms for preprocessing the audio
        transforms = Compose([
            torchaudio.transforms.Resample(orig_freq=44100, new_freq=22050),
            torchaudio.transforms.MelSpectrogram(sample_rate=22050, n_fft=1024, hop_length=512, n_mels=64),
            torchaudio.transforms.AmplitudeToDB(),
            Normalize(mean=[-14.92], std=[19.03])  # Adjust with appropriate mean and std
        ])

        # Set the device for model inference
        device = torch.device("cpu")

        # Load the PyTorch model
        model = CNNNetwork().to(device)
        model.load_state_dict(torch.load('./ShotDetectorPredictor/model_1.2.pt', map_location=torch.device('cpu')))

        # Load the audio file
        waveform, _ = torchaudio.load(audio_file)

        # Mix audio channels down to one
        mixed_waveform = waveform.mean(dim=0, keepdim=True)

        # Preprocess the audio
        input_tensor = transforms(mixed_waveform).unsqueeze(0).to(device)

        # Enable evaluation mode for the model
        model.eval()

        # Perform inference
        with torch.no_grad():
            output = model(input_tensor)

        # Get the predicted label
        predicted_label = torch.argmax(output, 1).item()

        # Create a JSON object
        output_json = {
            "shot": predicted_label == 6  # True if predicted label is 6, False otherwise
        }

        # Print the JSON object to stdout
        sys.stdout.write(json.dumps(output_json))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("audio_file", help="Path to the input .wav audio file")
    args = parser.parse_args()

    audio_classifier = AudioClassifier(args.audio_file)
