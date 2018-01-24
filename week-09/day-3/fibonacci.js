'use strict';

function fibonacci(number) {
  if (typeof number !== 'number') {
    throw new Error('The argument is not a number!!!');
  }
  return number < 1 ? 0 :
    number <= 2 ? 1 :
    fibonacci(number - 1) + fibonacci(number - 2);
}

//console.log(fibonacci(8));

module.exports = fibonacci;
