const test = require('tape');
const returnSecondBiggestItem = require('./final-exam.ts');

test('return the second biggest number', (t) => {
  const actual = returnSecondBiggestItem([9, -1, 5, 4, 8]);
  const expected = 8;

  t.equal(actual, expected);
  t.end();
});

test('test with string', (t) => {
  const actual = returnSecondBiggestItem(['9', '1', '5', '4', '8']);
  const expected = '8';

  t.equal(actual, expected);
  t.end();
});
