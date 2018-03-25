'use strict';

let url = 'http://localhost:8080/books';

function connect(method, url, callback) {
  let xhr = new XMLHttpRequest();
  xhr.open(method, url);
  xhr.setRequestHeader("Accept", "application/json");
  xhr.setRequestHeader("Content-type", "application/json");
  xhr.onreadystatechange = function () {
    if (xhr.readyState === xhr.DONE && xhr.status === 200) {
      let request = JSON.parse(xhr.response);
      callback(request);
    }
  }
  xhr.send();
};

function createTable(result) {
  let message = document.querySelector('section#message');
  let table = document.querySelector('table');
  if (!result.books.length) {
    table.innerHTML = "";
    message.innerHTML = `<h2>No Match</h2>`;
  } else {
    message.innerHTML = "";
    table.innerHTML =
      `<tr>
        <th>Title</th>
        <th>Author</th>
        <th>Category</th>
        <th>Publisher</th>
        <th>Price</th>
      </tr>`
    result.books.forEach(function (item) {
      const fill =
        `<tr>
        <td>${item.title}</td>
        <td>${item.author}</td>
        <td>${item.category}</td>
        <td>${item.publisher}</td>
        <td>${item.price}</td>
      </tr>`
      table.innerHTML += fill;
    })
  }
};

let category = document.querySelector('#category');
let publisher = document.querySelector('#publisher');
let priceLo = document.querySelector('#price_lo');
let priceHi = document.querySelector('#price_hi');
let button = document.querySelector('button.search_button');

function clickButton() {
  button.addEventListener('click', function () {
    let link = url + '?';
    if (category.value.length) {
      link += `category=${category.value}`;
    }
    if (publisher.value.length) {
      link += `publisher=${publisher.value}`;
    }
    if (priceLo.value.length) {
      link += `priceLo=${priceLo.value}`;
    }
    if (priceHi.value.length) {
      link += `priceHi=${priceHi.value}`;
    }
    link = link.replace('?&', '?');
    connect('GET', link, createTable);
  })
};

function start() {
  connect('GET', url, createTable);
  clickButton();
}

start();
