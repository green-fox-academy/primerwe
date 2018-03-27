// 20.
// Create a function that takes a list of numbers and returns the second biggest element from it
'use strict';

export function returnSecondBiggestNumber(arr: any[]): any {
  return arr.sort((a, b) => b - a)[1];
};
