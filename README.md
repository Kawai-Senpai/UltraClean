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

The `cleanup` function provides a comprehensive set of options for cleaning text data. Below is a detailed description of its arguments and usage.

#### Arguments

- `data` (str): The text data to be cleaned.
- `remove_weird_chars` (bool): Remove unwanted characters like newlines, tabs, etc. Default is `True`.
- `remove_links` (bool): Remove URLs from the text. Default is `True`.
- `remove_emails` (bool): Remove email addresses from the text. Default is `True`.
- `remove_phones` (bool): Remove phone numbers from the text. Default is `True`.
- `remove_underscores` (bool): Remove underscores and other special characters. Default is `True`.
- `remove_unicode` (bool): Remove or replace certain unicode characters. Default is `True`.
- `remove_multi_dots` (bool): Replace multiple dots with a single dot. Default is `True`.
- `remove_extra_spaces` (bool): Remove extra spaces from the text. Default is `True`.
- `remove_hashtags` (bool): Remove hashtags from the text. Default is `True`.
- `remove_emojis` (bool): Remove emojis from the text. Default is `True`.
- `remove_numbers` (bool): Remove numbers from the text. Default is `False`.
- `remove_currencies` (bool): Remove currency symbols from the text. Default is `True`.
- `remove_punctuation` (bool): Remove punctuation from the text. Default is `False`.
- `remove_html` (bool): Remove HTML tags from the text. Default is `True`.
- `remove_latex` (bool): Remove LaTeX commands from the text. Default is `True`.

#### Example

```python
from ultraclean.clean import cleanup

text = "Congratulations! You've won a free trip to Hawaii. Click here to claim your prize. This is not a scam."
cleaned_text = cleanup(text)
print(cleaned_text)
```

### Spam Detection

The `Spam` class provides methods for detecting and filtering spam text using a pre-trained model.

#### Methods

- `__init__(self, cache_dir=None, device=None)`: Initialize the spam detector with optional cache directory and device (CPU or GPU).
- `predict(self, text)`: Predict if the given text is spam. Returns `True` if spam, otherwise `False`.
- `filter(self, paragraph)`: Filter out spam sentences from a paragraph. Returns the cleaned paragraph.

#### Example

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

Sample Output:

```plaintext
Is the text spam? Yes
Congratulations! You've won a free trip to Hawaii. This is not a scam.
```

## When to Use

- Use UltraClean for preprocessing text data before feeding it into AI/ML models.
- Use the `cleanup` function to remove unwanted characters and standardize text data.
- Use the `Spam` class to detect and filter out spam content from text data.

## When Not to Use

- Do not use UltraClean for tasks that require preserving the original formatting of text data.
- Avoid using the `cleanup` function with all options enabled if you need to retain specific types of information (e.g., links, emails).

## License

This project is licensed under the MIT License with attribution requirement.

## Author

Ranit Bhowmick • [bhowmickranitking@duck.com](mailto:bhowmickranitking@duck.com)
