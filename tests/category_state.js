function normalizeCategory(value) {
  return typeof value === 'string' ? value.trim() : '';
}

console.assert(normalizeCategory('  Food  ') === 'Food');
console.assert(normalizeCategory('') === '');
console.assert(normalizeCategory(null) === '');
console.log('Expense category tests passed');
