'use strict';

// Implement the selectLastEvenNumber function that takes an array and callback,
// it should call the callback immediately with the last even number on the array

function selectLastEvenNumber(array, callback) {
    let lastEvenNumber = 0;
    for (let i = 0; i < array.length; i++) {
        if (array[i] % 2 === 0){
            lastEvenNumber = array[i];
        }
    }
    callback(lastEvenNumber);
}

function printNumber(num) {
  console.log(num);
}


selectLastEvenNumber([2, 5, 7, 8, 9, 11], printNumber); // should print 8