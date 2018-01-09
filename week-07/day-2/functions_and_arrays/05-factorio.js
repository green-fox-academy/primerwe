'use strict';
// - Create a function called `factorio`
//   that returns it's input's factorial

function factorio(number) {
    
    if (number === 0 || number === 1) {
        console.log(1);
    } else {
        for (let i = number - 1; i >= 1; i--) {
            number *= i;
        }
        console.log(number);
    }
}

factorio(0); //1
factorio(1); //1
factorio(5); //120