'use strict';

let xhr = new XMLHttpRequest;
let btn = document.querySelector('#btn');

btn.addEventListener('click', function() {
    let data = document.querySelector('#input').value;
    console.log(data);
    if (document.querySelector('p')) {
        let element = document.querySelector('p');
        document.body.removeChild(element);
        let map = document.querySelector('iframe')
        document.body.removeChild(map);
    }
    getCoordinates(data);
//            makeTheMap(location);
});

function getCoordinates(data) {
    xhr.open('GET', 'https://devru-latitude-longitude-find-v1.p.mashape.com/latlon.php?location=' + data);
    xhr.setRequestHeader('X-Mashape-Key', 'G5HRfQQXpPmshO8XdWpsncHMnUmZp1nc7rWjsnQiDu017ZVXW6');
    xhr.setRequestHeader('Accept', 'application/json');

    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            let location = JSON.parse(xhr.responseText).Results[0];
            getLocation(location);
        }
    }
    /*xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            let location = JSON.parse(xhr.responseText).Results;
            location.forEach(function(item) { 
                getLocation(item);
            })
        }
    };*/
    xhr.send();
};

function getLocation(location) {
    console.log(location);
    let coordinates = document.createElement('p');
    if (location === undefined) {
        errorMessage()
    } else {
        if (location.ll === '-9999.000000 -9999.000000') {
            coordinates.textContent = 'It\'s a country!';
        } else {
            coordinates.textContent = 'The coordinates you are looking for: ' + location.ll;
        }
        document.body.appendChild(coordinates);
    };
    makeTheMap(location);
};

function makeTheMap(location) {
    let map = document.createElement('iframe');
    map.width = 600;
    map.height = 450;
    map.frameborder = 0;
    map.style = 0;
    if (location === undefined) {
        map.src = 'https://www.google.com/maps/embed/v1/place?key=AIzaSyDJ3kof44euEpMaxSYH8cEY7a-bPJzHU2A&q=green+fox+academy';
    } else {
        map.src = 'https://www.google.com/maps/embed/v1/place?key=AIzaSyDJ3kof44euEpMaxSYH8cEY7a-bPJzHU2A&q=' + location.name;
    }
    document.body.appendChild(map);
}

function errorMessage() {
    let paragraph = document.createElement('p');
    paragraph.textContent = 'Sorry! Couldn\'t find this adress!';
    document.body.appendChild(paragraph);
}