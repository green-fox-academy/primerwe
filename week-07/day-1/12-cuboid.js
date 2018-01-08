'use strict';

// Write a program that stores 3 sides of a cuboid as variables (floats)
// The program should write the surface area and volume of the cuboid like:
//
// Surface Area: 600
// Volume: 1000

let a = 2;
let b = 10;
let c = 50;

let area = 2 * ((a * b) + (a * c) + (b * c));
let volume = a * b * c;

console.log('Surface Area: ' + area);
console.log('Volume: ' + volume);