'use strict';

var lineCount = 6;


// Write a program that draws a
// square like this:
//
//
// %%%%%
// %%  %
// % % %
// %  %%
// %   %
// %%%%%
//
// The square should have as many lines as lineCount is

for (let i = 1; i <= lineCount; i++) {
    let row = '';
    let str = ' ';
    for (let j = 1; j <= (lineCount - 1); j++) {
         if (i === 1 || i === lineCount) {
            row += '%';
        } else {
            row = '%' + str.repeat(lineCount - 3) + '%';
        }
    }

    console.log(row);
}