def category(value):
    return value.strip().lower() or 'other'

assert category('Food') == 'food'
assert category(' Travel ') == 'travel'
assert category('') == 'other'
print('Category normalization passed')
