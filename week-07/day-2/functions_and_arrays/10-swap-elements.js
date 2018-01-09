'use strict';
// - Create a variable named `abc` with the following content: `["Arthur", "Boe", "Chloe"]`
// - Swap the first and the third element of `abc`

//swap with the hard way
let abc = ["Arthur", "Boe", "Chloe"];

let x = abc.pop();
let y = abc.shift();

abc.push(y);
abc.unshift(x);

console.log(abc);

//swap with reverse()

let abc2 = ["Arthur", "Boe", "Chloe"];

abc2.reverse();

console.log(abc2);