'use strict';

//let total = function(item) {
//  return item.reduce((a,b) => a+b, 0);
//} 

//console.log(total([3, 4, 5, 6, 7]))

let total = function(item) {
  let summa = 0;
  item.forEach(number => {
    if (typeof number !== 'number') {
      throw new Error(`'${number}' is not a number`);
    }
    summa += number;
  });
  return summa;
}

module.exports = total;
