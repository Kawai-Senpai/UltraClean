import re
import emoji

def cleanup(
    data,
    remove_weird_chars=True,
    remove_links=True,
    remove_emails=True,
    remove_phones=True,
    remove_underscores=True,
    remove_unicode=True,
    remove_multi_dots=True,
    remove_extra_spaces=True,
    remove_hashtags=True,
    remove_emojis=True,
    remove_numbers=False,
    remove_currencies=True,
    remove_punctuation=False,
    remove_html=True,
    remove_latex=True
):
    if not isinstance(data, str):
        return data

    if remove_weird_chars:
        # Extended list of unwanted characters
        unwanted_chars = [
            '\n', '\t', '\r', '\v', '\f', '\a', '\b',
            '\u200b', '\u200c', '\u200d', '\u2060', '\ufeff',
            '℠', '™', '®', '©', '�'
        ]
        for char in unwanted_chars:
            data = data.replace(char, ' ')

    if remove_links:
        # Enhanced URL pattern
        data = re.sub(r'(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?', '', data, flags=re.IGNORECASE)

    if remove_emails:
        # Enhanced email pattern
        data = re.sub(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', '', data)

    if remove_phones:
        # Enhanced phone pattern (international format support)
        data = re.sub(r'[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}', '', data)
        data = re.sub(r'[\+]?\d{10,}', '', data)

    if remove_underscores:
        # Extended list of special characters
        remove_items = ['_', '•', '⁃', '⁎', '‣', '⁕', '⁜', '⁂', '⁋', '‿', '❧', '☙', '➤', '⇒', '⇨', '→', '⟶']
        for item in remove_items:
            data = data.replace(item, '')

    if remove_unicode:
        # Extended unicode replacements
        unicode_chars = {
            'â€¢': '', 'â€': '', 'â€™': "'", 'â€œ': '"', 'â€"': '-',
            '\u2013': '-', '\u2014': '-', '\u2015': '-', '\u2017': '_',
            '\u2018': "'", '\u2019': "'", '\u201a': ',', '\u201b': "'",
            '\u201c': '"', '\u201d': '"', '\u201e': '"', '\u201f': '"',
            '\u2026': '...', '\u2027': '.', '\u2032': "'", '\u2033': '"'
        }
        for char, replacement in unicode_chars.items():
            data = data.replace(char, replacement)

    if remove_emojis:
        data = emoji.replace_emoji(data, '')

    if remove_numbers:
        data = re.sub(r'\d+', '', data)

    if remove_currencies:
        currency_symbols = ['$', '€', '£', '¥', '₹', '₽', '₪', '₱', '₿']
        for symbol in currency_symbols:
            data = data.replace(symbol, '')

    if remove_punctuation:
        punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
        for p in punctuation:
            data = data.replace(p, '')

    if remove_html:
        # Remove HTML tags
        data = re.sub(r'<[^>]+>', '', data)

    if remove_latex:
        # Remove LaTeX commands
        data = re.sub(r'\\[a-zA-Z]+', '', data)

    if remove_multi_dots:
        data = re.sub(r'\.{2,}', '.', data)

    if remove_extra_spaces:
        # Enhanced whitespace handling
        data = re.sub(r'\s+', ' ', data)
        data = data.strip()

    if remove_hashtags:
        data = re.sub(r'#\w+', '', data)

    return data
