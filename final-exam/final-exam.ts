// 20.
// Create a function that takes a list of numbers and returns the second biggest element from it
'use strict';

let numbers = [4, 2, 5, 1, 3];

let secondBiggestElement = function (arr) {
  const secondBiggest = arr.sort((a, b) => b - a);
  return secondBiggest[1];
};

console.log('The second biggest number is: ' + secondBiggestElement(numbers));

module.exports = secondBiggestElement;
