// 20.
// Create a function that takes a list of numbers and returns the second biggest element from it
'use strict';

let items;
let sortMyArray;
items = [4, 2, 5, 1, 3];

sortMyArray = (arr) => {
  return arr.sort((a, b) => b - a)[1];
};

console.log('The second biggest element is: ' + sortMyArray(items));

module.exports = sortMyArray;
