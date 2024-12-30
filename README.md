# UltraClean

UltraClean is a fast and efficient Python library for cleaning and preprocessing text data, specifically designed for AI/ML tasks and data processing.

![UltraClean Thumbnail](https://github.com/Kawai-Senpai/UltraClean/blob/c5d769d553412071e3160a32cf390bf8b90e555e/Assets/UltraClean%20Thumbnail.png)

## Features

- Remove unwanted characters, links, emails, phone numbers, underscores, unicode characters, emojis, numbers, currencies, punctuation, HTML tags, LaTeX commands, and more.
- Handle multi-dots, extra spaces, and hashtags.
- Batch processing for efficient text cleaning.
- Spam detection and filtering using pre-trained models.

## Installation

You can install UltraClean using pip:

```bash
pip install ultraclean
```

## Usage

### Text Cleaning

```python
from ultraclean.clean import cleanup

text = "Congratulations! You've won a free trip to Hawaii. Click here to claim your prize. This is not a scam."
cleaned_text = cleanup(text)
print(cleaned_text)
```

### Spam Detection

```python
from ultraclean.predict import Spam

spam_detector = Spam()
text = "Congratulations! You've won a free trip to Hawaii. Click here to claim your prize."
is_spam = spam_detector.predict(text)
print(f"Is the text spam? {'Yes' if is_spam else 'No'}")

paragraph = "Congratulations! You've won a free trip to Hawaii. Click here to claim your prize. This is not a scam."
cleaned_paragraph = spam_detector.filter(paragraph)
print(cleaned_paragraph)
```

## License

This project is licensed under the MIT License with attribution requirement.

## Author

Ranit Bhowmick - [bhowmickranitking@duck.com](mailto:bhowmickranitking@duck.com)
