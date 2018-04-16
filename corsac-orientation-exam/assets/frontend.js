'use strict';

const url = 'http://localhost:8080';
let table = document.querySelector('table');

//const button = document.querySelector('.btn');

function connect(method, url, callback) {
  let xhr = new XMLHttpRequest();
  xhr.open(method, url);
  xhr.setRequestHeader("Accept", "application/json");
  xhr.setRequestHeader("Content-type", "application/json");
  xhr.onreadystatechange = function () {
    if (xhr.readyState === xhr.DONE && xhr.status === 200) {
      callback(JSON.parse(xhr.responseText));
    }
  };
  xhr.send();
};

function createTable(result) {
  table.innerHTML = "";
  table.innerHTML =
    `<tr>
      <th>Planet</th>
      <th>Population</th>
      <th>Spaceship location</th>
      <th>People on ship</th>
    </tr>`;
  result.exam.forEach(function (item) {
    table.innerHTML +=
      `<tr>
        <td>${item.name}</td>
        <td>${item.population}</td>
        <td id="${item.id}">
          <button class="move-btn btn">Move here</button>
          <button class="movetoplanet-btn no-display"><-to planet</button>
          <button class="movetoship-btn no-display">to ship-></button>
        </td>
        <td>-</td>
      </tr>`
  });
}

let button = document.querySelector('button.move-btn');
let toPlanet = document.querySelector('button.movetoplanet-btn');
let toShip = document.querySelector('button.movetoship-btn');

function isShipOnPlanet(planetId) {
  //if ship on planet change the move here button to 'to ship' and 'to planet' button
  if (planetId === `${req.body.id}`) {
    button.classList.add('no-display');
    toPlanet.classList.remove('no-display');
    toShip.classList.remove('no-display');
  }
  connect('GET', url + '/ship', createTable);
};

function moveShipHere(planetId) {
  button.addEventListener('click', function () {
    connect('PUT', url + `/movehere/${planetId}`, createTable);
  })
}

function moveToPlanet(planetId) {
  toPlanet.addEventListener('click', function () {
    connect('PUT', url + `/toplanet/${planetId}`, createTable);
  })
}

function moveToShip(planetId) {
  toShip.addEventListener('click', function () {
    connect('PUT', url + `/toship/${planetId}`, createTable);
  })
}

connect('GET', url + '/planets', createTable);
