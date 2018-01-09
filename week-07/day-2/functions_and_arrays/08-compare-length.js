'use strict';
// - Create a variable named `p1`
//   with the following content: `[1, 2, 3]`
// - Create a variable named `p2`
//   with the following content: `[4, 5]`
// - Log to the console if `p2` has more elements than `p1`

let p1 = [1, 2, 3];
let p2 = [4, 5];

if (p1.length > p2.length) {
    console.log('p1 has more elements than p2');
} else if (p1.length === p2.length) {
    console.log('p1 has same elements as p2');
} else {
    console.log('p2 has more elements than p1');
}