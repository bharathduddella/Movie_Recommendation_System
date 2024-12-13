import re

def clean_text(text):
    """Remove special characters and lowercase the text."""
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text.lower()
