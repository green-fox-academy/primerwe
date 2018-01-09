'use strict';
// - Write a function called `sum` that sum all the numbers until the given parameter
// - The function should return the result

function summa(a) {
    
    let x = 0;
    
    for (let i = 1; i <= a; i++) {
        x += i;
    }
    console.log(x);
}

summa(5);
