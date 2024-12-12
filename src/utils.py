import os

def save_transcription(text, output_path):
    with open(output_path, 'w') as file:
        file.write(text)
