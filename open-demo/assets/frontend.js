'use strict';

const url = 'http://localhost:8080';
let h2 = document.querySelector('#students>h2');
let ul = document.querySelector('ul.foxes');
let ol = document.querySelector('ol.foxes');

function connect(method, url, callback) {
  let xhr = new XMLHttpRequest();
  xhr.open(method, url);
  xhr.setRequestHeader("Accept", "application/json");
  xhr.setRequestHeader("Content-type", "application/json");
  xhr.onreadystatechange = function () {
    if (xhr.readyState === xhr.DONE && xhr.status === 200) {
      callback(JSON.parse(xhr.responseText));
      console.log(JSON.parse(xhr.responseText));
    }
  };
  xhr.send();
};

let studentsList = [];

function createStudentList(result) {
  h2.textContent = 'Foxes:';
  ul.innerHTML = '';
  result.students.forEach(element => {
    ul.innerHTML += `<li>${element.name}`;
  });
  let items = document.querySelectorAll('ul>li');
  studentsList = Array.prototype.map.call(items, (obj) => {
    return obj.textContent;
  })
  console.log('Students list:', studentsList);
  return studentsList;
}

function shuffleArray(array) {
  for (let i = array.length - 1; i > 0; i--) {
    let j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
  return array;
}

let h3 = document.querySelector('#result>h3');

function createShuffleResult(array) {
  h3.textContent = `And Today's order is:`;
  ol.innerHTML = '';
  array.forEach(element => {
    ol.innerHTML += `<li>${element}</li>`;
  });
}

function clearItems() {
  while (ol.firstChild) {
    ol.removeChild(ol.firstChild);
  }
}

let button = document.querySelector('button#start');
let asbest = document.querySelector('button#asbest');
let badcat = document.querySelector('button#badcat');
let please = document.querySelector('button#please');
let clear = document.querySelector('button#clear');

asbest.addEventListener('click', () => {
  clearItems();
  connect('GET', url + '/asbest', createStudentList);
});

badcat.addEventListener('click', () => {
  clearItems();
  connect('GET', url + '/badcat', createStudentList);
});

please.addEventListener('click', () => {
  clearItems();
  connect('GET', url + '/please', createStudentList);
})

clear.addEventListener('click', () => {
  window.location.reload();
})

let message = document.querySelector('#message');
let stu = document.querySelector('#students');
let res = document.querySelector('#result');
button.addEventListener('click', () => {
  if (!studentsList.length) {
    message.innerHTML = "Please select class first!";
  } else {
    message.innerHTML = '';
    message.setAttribute('class', 'hide');
    let shuffledStudents = shuffleArray(studentsList);
    console.log('Shuffle: ', shuffledStudents);
    clearItems();
    createShuffleResult(shuffledStudents);
  }
});
