'use strict';

var fruits = [
  'melon',
  'apple',
  'strawberry',
  'blueberry',
  'pear',
  'banana'
];

// Create a new array of consists numbers that shows how many times the 'e' letter
// occurs in the word stored under the same index at the fruits array!
// Please use the map method.

let countLetterEs = fruits.map(function(fruit){
    let countEr = 0;
    let letters = fruit.split('');
    for (let i = 0; i < fruits.length; i++){
        if (letters[i] === 'e') {
            countEr++;
        }
    }
    return countEr;
});

console.log(countLetterEs);