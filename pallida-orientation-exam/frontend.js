'use strict';

function connect() {
  let xhr = new XMLHttpRequest();
  let url = `http://localhost:8080/search${query}`;
  xhr.open('GET', url);
  xhr.onreadystatechange = function () {
    if (xhr.readyState === xhr.DONE && xhr.status === 200) {
      console.log(xhr);
      createDataInHtml(JSON.parse(xhr.responseText))
    } else {
      console.log('status not OK!')
    }
  };
  xhr.send();
};

function createDataInHtml(datas) {
  if (datas.result === 'notFound') {
    document.querySelector('table').innerHTML = 'Sorry, the submitted licence plate is not valid';
  } else if (datas.result === 'error') {
    document.querySelector('table').innerHTML = 'Wrong format!';
  } else {
    createTable(datas.data);
  }
};

function createTable(data) {
  document.querySelector('table').innerHTML =
    `<tr>
      <th>Plate</th>
      <th>Brand</th>
      <th>Model</th>
      <th>Color</th>
      <th>Year</th>
    </tr>`;
  data.forEach(function (car) {
    document.querySelector('table').innerHTML +=
      `<tr>
        <td>${car.plate}</td>
        <td class="brand" src="${car.car_brand}">[${car.car_brand}]</td>
        <td>${car.car_model}</td>
        <td>${car.color}</td>
        <td>${car.year}</td>
      </tr>`;
  });
  addEventToBrand();
};

function addEventToBrand() {
  let className = document.getElementsByClassName('brand');
  Array.from(className).forEach(function (item) {
    item.addEventListener('click', clickOnBrand);
  });
};

function clickOnBrand(event) {
  connect(`/${event.target.getAttribute('src')}`);
}

function createQuery(query) {
  if (document.querySelector('#rb').checked) {
    query = `?q=rb`;
  } else if (document.querySelector('#dt').checked) {
    query = `?q=dt`;
  } else {
    query = `?q=${query}`;
  }
  connect(query);
};

function getInput() {
  createQuery(document.querySelector('#input_text').value)
};

function queryDatabase () {
  document.querySelector('.query_btn').addEventListener('click', getInput);
}

queryDatabase();