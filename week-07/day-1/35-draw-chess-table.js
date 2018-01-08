// Crate a program that draws a chess table like this
//
// % % % %
//  % % % %
// % % % %
//  % % % %
// % % % %
//  % % % %
// % % % % 
//  % % % %
//

let lineCount = 8

for (i = 1; i <= lineCount; i++) {
    let row = '';
    if (i % 2 === 0) {
        row = 'XoXoXoXo';
    } else {
        row = 'oXoXoXoX';
    }
    console.log(row);
}