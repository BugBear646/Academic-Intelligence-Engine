import re

def extract_email(text):

    pattern = r'[\w\.-]+@[\w\.-]+\.\w+'

    matches = re.findall(pattern, text)

    return matches[0] if matches else None

def clean_text(text):

    text = re.sub(r'\s+', ' ', text)

    return text.strip()