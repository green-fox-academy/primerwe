'use strict';

function Sharpie(color, width) {
    this.color = color;
    this.width = width;
    this.inkAmount = 100;
    this.use = function () {
        if (this.inkAmount < this.width) {
            console.log('The sharpie is empty!');
        } else {
            this.inkAmount -= this.width;
        }
    }
}

function useAllInk(sharpie) {
    let originalInkAmount = sharpie.inkAmount;
    for (let i = 0; i < (originalInkAmount / sharpie.width); i++) {
        console.log(sharpie.inkAmount);
        sharpie.use();
    }
}

let pinkSharpie = new Sharpie('pink', 7);

console.log(pinkSharpie.inkAmount);
useAllInk(pinkSharpie);
console.log(pinkSharpie.inkAmount);
