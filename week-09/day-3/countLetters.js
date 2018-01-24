'use strict';

let countLetters = function (string) {
  if (typeof string !== 'string') {
    throw new Error('"string" is not a string!');
  };
  let letters = {};
  string.split('').forEach(function (letter) {
    if (letters[letter] > 0) {
      letters[letter]++;
    } else {
      letters[letter] = 1;
    }
  });
  return letters;
};

module.exports = countLetters;
