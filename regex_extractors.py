import re

def get_emails(text):
    return re.findall(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', text)

def get_urls(text):
    return re.findall(r'https?://[^\s]+', text)

def get_phone_numbers(text):
    return re.findall(r'\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}', text)

def get_credit_cards(text):
    return re.findall(r'\b(?:\d{4}[- ]?){3}\d{4}\b', text)

def get_times(text):
    return re.findall(r'\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b', text)

def get_html_tags(text):
    return re.findall(r'<[^>]+>', text)

def get_hashtags(text):
    return re.findall(r'#\w+', text)

def get_currency_amounts(text):
    return re.findall(r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?', text)
