'use strict';

const test = require('tape');
const anagram = require('./anagram.js');


test('return is Anagram', function (t) {
  let actual = anagram('hello', 'holle');

  t.ok(actual, 'is anagram');
  t.end();
});

test('test for spaces', function (t) {
  let actual = anagram('hel lo', 'oh l le');

  t.ok(actual, 'is still anagram');
  t.end();
});

test('test for not equal length', function (t) {
  t.throws(anagram.bind(this, ('hello', 'ello')), Error);
  t.end();
});

test('test for numbers', function (t) {
  t.throws(anagram.bind(this, (123, 321)), Error);
  t.end();
})