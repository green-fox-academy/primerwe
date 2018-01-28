'use strict'

const button = document.querySelector('button#btn');

button.addEventListener('click', function getGiphies() {
    let xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://api.giphy.com/v1/gifs/search?api_key=2NaHf0oqvaBflMtJ9Ya71Xm218wJ9do2&q=cat&limit=16&offset=0&rating=G&lang=en', true);
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

function staticGiphies(item) {
    let image = document.createElement('img');
    image.src = item.images['fixed_height_still'].url;
    document.body.appendChild(image);

    image.addEventListener('click', function () {
        image.src = item.images['fixed_height'].url;
    });
};

//getGiphies();
