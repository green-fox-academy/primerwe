'use strict';

let createCandy = document.querySelector('button.create-candies');
let candyCounter = document.querySelector('dd.candies');
let candyNumber = 0;
createCandy.addEventListener('click', addCandy);

let buyLollypop = document.querySelector('button.buy-lollypops');
let lollypopCounter = document.querySelector('dd.lollypops');
let lollypopNumber = 0;
buyLollypop.addEventListener('click', addLollypop);

let candyPerSec = document.querySelector('dd.speed');
let candySpeed = 0;
let multiplier = 1;
let candyGenerator = setInterval(function(){
    candiesPerSecond(multiplier);
}, 1000);

let candyMachine = document.querySelector('button.candy-machine');
candyMachine.addEventListener('click', makeCandyRain);

