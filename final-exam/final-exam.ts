// 20.
// Create a function that takes a list of numbers and returns the second biggest element from it
'use strict';

let array = [4, 2, 5, 1, 3];

let secondBiggestElement = function (arr) {
  const secondBiggest = arr.sort((a, b) => b - a)[1];
  return secondBiggest;
};

console.log('The second biggest number is: ' + secondBiggestElement(array));

module.exports = secondBiggestElement;
