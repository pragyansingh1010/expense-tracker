def valid_category(value):
    return isinstance(value, str) and bool(value.strip())

assert valid_category('Food')
assert valid_category('Bills')
assert not valid_category('')
print('Expense category rules passed')
