'use strict';

var lineCount = 4;

// Write a program that draws a
// triangle like this:
//
// *
// **
// ***
// ****
//
// The triangle should have as many lines as lineCount is


for (let i = 1; i <= lineCount; i++) {
    let row = '';
    
    for (let j = 1; j <= i; j++) {
        row += '*';
    }
    
    console.log(row);
}