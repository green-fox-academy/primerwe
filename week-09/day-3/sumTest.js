'use strict';

const test = require('tape');
const total = require('./sum.js');


test('return summa of a list of integers', function (t) {
  let actual = total([3, 4, 5, 6, 7]);
  let expected = 25;

  t.equal(actual, expected);
  t.end();
});

test('test with empty list', function (t) {
  let actual = total([]);
  let expected = 0;

  t.equal(actual, expected);
  t.end();
});

test('test with one element', function (t) {
  let actual = total([5]);
  let expected = 5;

  t.equal(actual, expected);
  t.end();
});

test('test with a null', function (t) {
  t.throws(total.bind(this, [null]), Error);
  t.end();
})

test('test with a string', function (t) {
  t.throws(total.bind(this, ['x']), Error);
  t.end();
});
