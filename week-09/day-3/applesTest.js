'use strict';

const test = require('tape');
const apple = require('./apples.js');

test('return apple', function (t) {
  let actual = apple.getApple();
  let expected = 'apple';

  t.equal(actual, expected);
  t.end();
});
