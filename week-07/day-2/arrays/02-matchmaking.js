'use strict';
// Join the two array by matching one girl with one boy in the order array
// Exepected output: ['Eve', 'Joe', 'Ashley', 'Fred'...]

var girls = ['Eve', 'Ashley', 'Bözsi', 'Kat', 'Jane'];
var boys = ['Joe', 'Fred', 'Béla', 'Todd', 'Neef', 'Jeff'];
var order = [];

for (let i = 0; i < girls.length; i++) {
    order.push(girls[i], boys[i]);
}

//for (let i = 0; i < boys.length; i++) {
//    order.push(girls[i], boys[i]);
//}

console.log(order);
