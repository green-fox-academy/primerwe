'use strict';

const planetData = [
    {
        category: 'inhabited',
        content: 'Foxes',
        asteroid: true
      },
    {
        category: 'inhabited',
        content: 'Whales and Rabbits',
        asteroid: true
      },
    {
        category: 'uninhabited',
        content: 'Baobabs and Roses',
        asteroid: true
      },
    {
        category: 'inhabited',
        content: 'Giant monsters',
        asteroid: false
      },
    {
        category: 'inhabited',
        content: 'Sheep',
        asteroid: true
      }
    ];

let asteroidList = document.querySelector('ul.asteroids');
let kingAsteroid = document.querySelector('li');
asteroidList.removeChild(kingAsteroid);

for (let i = 0; i < planetData.length; i++) {
    let newItem = document.createElement('li');
    if (planetData[i].asteroid) {
        newItem.textContent = planetData[i].content;
        newItem.setAttribute('class', planetData[i].category);
        asteroidList.appendChild(newItem);
        }
}
