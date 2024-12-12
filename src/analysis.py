def analyze_productivity(transcript):
    keywords = ['decision', 'action', 'plan']
    productive_segments = [line for line in transcript.split('.') if any(kw in line for kw in keywords)]
    return {"productive_segments": productive_segments, "count": len(productive_segments)}

def detect_topics(transcript):
    topics = ["project", "deadline", "feedback"]
    detected_topics = {topic: transcript.count(topic) for topic in topics}
    return detected_topics
