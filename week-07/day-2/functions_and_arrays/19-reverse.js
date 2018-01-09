'use strict';
// - Create a variable named `aj`
//   with the following content: `[3, 4, 5, 6, 7]`
// - Reverse the order of the elements in `aj`
// 		- do it with the built in method
//		- do it with creating a new temp array and a loop
// - Print the elements of the reversed `aj`

let aj = [3, 4, 5, 6, 7];
//reverse with built in function

aj.reverse();
console.log(aj);

//reverse with temp array and a loop
let aj2 = [3, 4, 5, 6, 7];
let ja = [];

for (let i = aj2.length - 1; i >= 0; i--) {
    ja.push(aj2[i]);
}

console.log(ja);