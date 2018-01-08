'use strict';

var lineCount = 4;

// Write a program that draws a
// pyramid like this:
//
//
//    *
//   ***
//  *****
// *******
//
// The pyramid should have as many lines as lineCount is

//for (let i = 0; i < lineCount; i++) {
//    
//    for (let j = 0; j <= (lineCount - 1) + i; j++) {
//        
//        if (j >= (lineCount - 1) - i) {
//            console.log('*');
//        } else {
//            console.log('');
//        }
//    }
//    console.log(' ')
//}

for (let i = 0; i < lineCount; i++) {
    let row = '';
    
    for (let j = 0; j <= (lineCount - 1) + i; j++) {
        if (j >= (lineCount - 1) - i) {
            row += '*';
        } else {
            row = ' ' + row;
        }
    }
    
    console.log(row);
}