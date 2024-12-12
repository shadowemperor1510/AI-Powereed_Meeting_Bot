import librosa

def preprocess_audio(file_path):
    audio, sr = librosa.load(file_path, sr=None)
    audio = librosa.effects.trim(audio)[0]  # Remove silence
    return audio, sr
