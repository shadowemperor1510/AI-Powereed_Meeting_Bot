from flask import Flask, request
from transcription import transcribe_audio
from analysis import analyze_productivity, detect_topics

app = Flask(__name__)

@app.route('/transcribe', methods=['POST'])
def transcribe():
    file = request.files['file']
    text = transcribe_audio(file)
    return {"transcription": text}

@app.route('/analyze', methods=['POST'])
def analyze():
    transcript = request.json['transcript']
    productivity = analyze_productivity(transcript)
    topics = detect_topics(transcript)
    return {"productivity": productivity, "topics": topics}

if __name__ == '__main__':
    app.run(debug=True)
