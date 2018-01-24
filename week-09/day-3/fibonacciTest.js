'use strict';

const test = require('tape');
const fibonacci = require('./fibonacci.js');

test('test for a number', function (t) {
  let actual = fibonacci(8);
  let expected = 21;

  t.equal(actual, expected);
  t.end();
});

test('test for a string', function (t) {
  t.throws(fibonacci.bind(this, 'hello'), Error);
  t.end();
});

test('test for null', function (t) {
  t.throws(fibonacci.bind(this, null), Error);
  t.end();
});