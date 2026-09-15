def clean_category(value):
    return value.strip().lower()

assert clean_category(' Food ') == 'food'
assert clean_category('TRAVEL') == 'travel'
