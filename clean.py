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

    if remove_multi_dots:
        data = re.sub(r'\.{2,}', '.', data)

    if remove_weird_chars:
        # Extended list of unwanted characters
        unwanted_chars = [
            # Control and formatting characters
            '\n', '\t', '\r', '\v', '\f', '\a', '\b', '\x1C', '\x1D', '\x1E', '\x1F',
            
            # Zero-width and invisible characters
            '\u200b', '\u200c', '\u200d', '\u200e', '\u200f', '\u2060', '\ufeff', 
            '\u2061', '\u2062', '\u2063', '\u2064', '\u206a', '\u206b', '\u206c',
            '\u206d', '\u206e', '\u206f',
            
            # Special whitespace
            '\u2000', '\u2001', '\u2002', '\u2003', '\u2004', '\u2005', '\u2006',
            '\u2007', '\u2008', '\u2009', '\u200a', '\u2028', '\u2029', '\u202f',
            '\u205f', '\u3000',
            
            # Special characters and symbols
            '℠', '™', '®', '©', '�', '•', '⁃', '⁎', '‣', '⁕', '⁜', '⁂', '⁋', '‿',
            '❧', '☙', '➤', '⇒', '⇨', '→', '⟶'
        ]
        for char in unwanted_chars:
            data = data.replace(char, ' ')

    if remove_links:
        data = re.sub(r'(?i)\bhttps?:\/\/\S+?\b', '', data)  # Made non-greedy with ?

    if remove_emails:
        data = re.sub(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b', '', data)

    if remove_phones:
        data = re.sub(r'\b[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}\b', '', data)
        data = re.sub(r'\b[\+]?\d{10,}\b', '', data)

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
        data = re.sub(r'<[^>]+?>', '', data)  # Made non-greedy with ?

    if remove_latex:
        data = re.sub(r'\b\\[a-zA-Z]+\b', '', data)

    if remove_extra_spaces:
        # Enhanced whitespace handling
        data = re.sub(r'\s+', ' ', data)
        data = data.strip()

    if remove_hashtags:
        data = re.sub(r'#\w+', '', data)

    return data