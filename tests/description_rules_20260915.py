def valid_description(text):
    return bool(text.strip())

assert valid_description('Food')
assert not valid_description('')
