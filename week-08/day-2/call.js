'use strict';

function factorialTillLimitWithCallback(limit, callback) {
  var factorial = 1;
  for (var i = 1; i <= limit; ++i) {
    callback(factorial);
    factorial *= i;
  }
}

function functionWhatWeCallBack (value) {
    console.log(value);
}
// Create a function and pass it as a parameter to the factorialTillLimitWithCallback
// function, and print all the factorial numbers till 20

let myFunction = factorialTillLimitWithCallback(20, functionWhatWeCallBack);