'use strict';
// - Create (dynamically*) a two dimensional list
//   with the following matrix**. Use a loop!
//
//   0 0 0 1
//   0 0 1 0
//   0 1 0 0
//   1 0 0 0
//
// - Print this two dimensional list to the console
//
// * size should depend on a variable
// ** Relax, a matrix is just like an array

let matrix = [[]];
let size = 4;

for (let i = 0; i < size; i++) {
    let row = '';
    matrix[i] = [0]
    for (let j = 0; j < size; j++) {
        if (i + j === size - 1) {
            row += matrix[i][j] = [1] + ' ';
        } else {
            row += matrix[i][j] = [0] + ' ';
        }
    }
    console.log(row);
}
