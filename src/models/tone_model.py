from transformers import AutoModelForSequenceClassification, AutoTokenizer

def train_tone_model(data):
    model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=3)
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
    # Add training logic
    return model
