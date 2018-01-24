'use strict';

const test = require('tape');
const countLetters = require('./countletters.js');


test('test for empty string', function (t) {
  let actual = countLetters('');
  let expected = {};

  t.deepEqual(actual, expected);
  t.end();
});

test('test for a letter', function (t) {
  let actual = countLetters('a');
  let expected = {
    a: 1
  };

  t.deepEqual(actual, expected);
  t.end();
});

test('test for string', function (t) {
  let actual = countLetters('apple apple');
  let expected = {
    a: 2,
    p: 4,
    l: 2,
    e: 2,
    ' ': 1
  };

  t.deepEqual(actual, expected);
  t.end();
});

test('test for non-strings', function (t) {
  t.throws(countLetters.bind(this, 123456), Error);
  t.end();
});
