function validAmount(value) {
  return Number.isFinite(value) && value >= 0;
}

console.assert(validAmount(0));
console.assert(validAmount(125.5));
console.assert(!validAmount(-1));
console.assert(!validAmount(NaN));
console.log('Expense tracker amount tests passed');
