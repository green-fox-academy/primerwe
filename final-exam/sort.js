'use strict';

const sortMyArray = function sortArray(arr) {
  const len = arr.length;
  for (let i = 0; i < len; i++) {
    let maxIndex = i;
    for (let j = i + 1; j < len; j++) {
      if (arr[j] > arr[maxIndex]) {
        maxIndex = j;
      }
    }
    const temp = arr[i];
    arr[i] = arr[maxIndex];
    arr[maxIndex] = temp;
  }
  return arr;
};

module.export = sortMyArray;
