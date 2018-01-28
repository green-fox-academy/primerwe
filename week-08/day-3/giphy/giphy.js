'use strict'

const search = document.querySelector('button#searchBtn');

search.addEventListener('click', function () {
    let value = document.querySelector('input#searchBox').value.replace(' ', '+');
    let number = document.querySelector('input#numberBox').value;
    let link = 'http://api.giphy.com/v1/gifs/search?api_key=2NaHf0oqvaBflMtJ9Ya71Xm218wJ9do2&q=' + value + '&limit=' + number + '&offset=0&rating=G&lang=en';
    console.log(value);
    let xhr = new XMLHttpRequest();
    xhr.open('GET', link, true);
    xhr.onload = function () {
        if (xhr.status === 200) {
            let content = JSON.parse(xhr.responseText).data;
            content.forEach(function (item) {
                staticGiphies(item);
            });
            console.log(content);
        } else {
            console.log('Connection failed!');
        }
    };
    xhr.send();
});

function clearGiphies() {
    let queryValue = document.querySelector('input#searchBox').value;
    console.log(queryValue);
    if (document.querySelector('img')) {
        let item = document.querySelector('img');
        while (item.firstChild) {
            item.removeChild(item.firstChild);
        }
    }
};

function staticGiphies(item) {
    let image = document.createElement('img');
    image.src = item.images['fixed_height_still'].url;
    document.body.appendChild(image);

    image.addEventListener('click', function () {
        image.src = item.images['fixed_height'].url;
    });
};
