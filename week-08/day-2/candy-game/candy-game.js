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
let candyGenerator = setInterval(function () {
    candiesPerSecond(multiplier);
}, 1000);


let candyMachine = document.querySelector('button.candy-machine');
candyMachine.addEventListener('click', makeCandyRain);



function addCandy() {
    candyNumber++;
    candyCounter.textContent = candyNumber;
}


function addLollypop() {
    if (candyCounter.textContent >= 100) {
        candyNumber -= 100;
        candyCounter.textContent = candyNumber;
        lollypopCounter.textContent += '🍭';
        lollypopNumber++;
        candySpeed += 1;
        candyPerSec.textContent = candySpeed;
    }
}


function candiesPerSecond(multiplier) {
    candyNumber = candyNumber + (lollypopNumber * multiplier);
    candyCounter.textContent = candyNumber;
}

function makeCandyRain() {
    multiplier *= 10;
    candySpeed *= 10;
    candyPerSec.textContent = candySpeed;
}
