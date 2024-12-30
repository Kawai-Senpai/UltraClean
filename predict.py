from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import warnings
import os
import logging

# Suppress warnings
warnings.filterwarnings("ignore")

# Suppress TensorFlow logs
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
logging.getLogger('tensorflow').setLevel(logging.FATAL)

# Suppress transformers logging
logging.getLogger('transformers').setLevel(logging.ERROR)

class Spam:
    def __init__(self, cache_dir=None, device=None):
        self.device = device if device else torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained("ZachBeesley/Spam-Detector", cache_dir=cache_dir)
        try:
            self.model = AutoModelForSequenceClassification.from_pretrained("ZachBeesley/Spam-Detector", cache_dir=cache_dir).to(self.device)
        except EnvironmentError:
            try:
                self.model = AutoModelForSequenceClassification.from_pretrained("ZachBeesley/Spam-Detector", cache_dir=cache_dir, from_tf=True).to(self.device)
            except ValueError as e:
                if "Keras 3" in str(e):
                    raise ValueError("Your currently installed version of Keras is Keras 3, but this is not yet supported in Transformers. Please install the backwards-compatible tf-keras package with `pip install tf-keras`.")
                else:
                    raise e

    def predict(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True).to(self.device)
        outputs = self.model(**inputs)
        logits = outputs.logits
        probabilities = torch.softmax(logits, dim=1)
        spam_score = probabilities[0][1].item()
        return True if spam_score > 0.5 else False

    def filter(self, paragraph):
        sentences = paragraph.split('. ')
        inputs = self.tokenizer(sentences, return_tensors="pt", truncation=True, padding=True).to(self.device)
        outputs = self.model(**inputs)
        logits = outputs.logits
        probabilities = torch.softmax(logits, dim=1)
        spam_scores = probabilities[:, 1].tolist()
        non_spam_sentences = [sentence for sentence, score in zip(sentences, spam_scores) if score <= 0.5]
        return '. '.join(non_spam_sentences)

