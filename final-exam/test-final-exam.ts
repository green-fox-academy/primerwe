import { test } from 'tape';
import { returnSecondBiggestNumber } from './final-exam';

test('return the second biggest number', t => {
  const actual = returnSecondBiggestNumber([9, -1, 5, 4, 8]);
  const expected = 8;

  t.equal(actual, expected);
  t.end();
});

test('test with string', t => {
  const actual = returnSecondBiggestNumber(['9', '1','5', '4', '8']);
  const expected = '8';

  t.equal(actual, expected);
  t.end(); 
});
