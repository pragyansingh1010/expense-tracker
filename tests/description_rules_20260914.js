function validDescription(value) {
  return typeof value === 'string' && value.trim().length > 0;
}

console.assert(validDescription('Lunch'));
console.assert(!validDescription(''));
console.assert(!validDescription('   '));
console.log('Expense description rules passed');
