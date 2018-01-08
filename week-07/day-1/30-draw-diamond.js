'use strict';

var lineCount = 7;



// Write a program that draws a
// diamond like this:
//
//
//    *
//   ***
//  *****
// *******
//  *****
//   ***
//    *
//
// The diamond should have as many lines as lineCount is

//top half
var n = lineCount;
for (let i = 1; i <= n; i+=2) {
    let row = '';
    
    for (let s = 0; s < (n - i / 2 - n / 2); s++) {
        row = ' ' + row;
    }
    for (let j = 1; j <= i; j++) {
        row += '*';
    }
    
    console.log(row);
}

//bottom half
for (let i = n-2; i >= 0; i-= 2) {
    let row = '';
    
    for (let s = 0; s < (n - i / 2 - n / 2); s++) {
        row = ' ' + row;
    }
    for (let j = 1; j <= i; j++) {
        row += '*';
    }
    
    console.log(row);
}