from regex_extractors import (
    get_emails,
    get_urls,
    get_phone_numbers,
    get_credit_cards,
    get_times,
    get_html_tags,
    get_hashtags,
    get_currency_amounts
)

def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def show(label, items):
    print(f"\n{label}:")
    if items:
        for i in set(items):
            print(f" - {i}")
    else:
        print(" - None found")

data = load_text("sample_input.txt")

show("Email Addresses", get_emails(data))
show("URLs", get_urls(data))
show("Phone Numbers", get_phone_numbers(data))
show("Credit Card Numbers", get_credit_cards(data))
show("Times", get_times(data))
show("HTML Tags", get_html_tags(data))
show("Hashtags", get_hashtags(data))
show("Currency Amounts", get_currency_amounts(data))
