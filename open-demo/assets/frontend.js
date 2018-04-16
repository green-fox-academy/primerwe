'use strict';

const url = 'http://localhost:8080';
let section = document.querySelector('#students');
let ul = document.querySelector('ul.foxes');
let ol = document.querySelector('ol.foxes');
let studentsList = [];

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

function createStudentList(result) {
  ul.innerHTML = "";
  result.students.forEach(element => {
    ul.innerHTML += `<li>${element.student_name}`;
    studentsList.push(element.student_name);
  });
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

function createShuffleResult(array) {
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

button.addEventListener('click', () => {
  let shuffledStudents = shuffleArray(studentsList);
  console.log('Shuffle: ', shuffledStudents);
  clearItems();
  createShuffleResult(shuffledStudents);
})

connect('GET', url + '/students', createStudentList);
