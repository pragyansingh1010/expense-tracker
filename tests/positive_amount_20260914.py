def valid_amount(value):
    return isinstance(value, (int, float)) and value > 0

assert valid_amount(10)
assert valid_amount(10.5)
assert not valid_amount(0)
assert not valid_amount(-2)
print('Tracker amount rules passed')
