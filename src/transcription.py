from transformers import pipeline
from audio_processing import preprocess_audio

def transcribe_audio(file_path):
    audio, _ = preprocess_audio(file_path)
    model = pipeline("automatic-speech-recognition", model="openai/whisper-base")
    transcription = model(audio)
    return transcription['text']
