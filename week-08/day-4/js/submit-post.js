'use strict';

document.addEventListener('DOMContentLoaded', submit, false);

function submit() {
    let submitButton = document.querySelector('.submit_button');
    submitButton.addEventListener('click', getPosts, true);
};

function getPosts() {
    let title = document.querySelector('#post_title');
    let url = document.querySelector('#post_url');
    title.value === '' || url.value === '' ? alert('Required!') : formatTexts(title.value, url.value);
};

function formatTexts(title, url, owner){
    submitPosts(`{ "title": "${title}", "url": "${url}"}, "owner": 'betterLateThanNever'`);
};

function submitPosts(message) {
    let link = 'https://time-radish.glitch.me/posts';
    let xhr = new XMLHttpRequest();
    xhr.open('POST', link);
    xhr.setRequestHeader("Content-type", "application/json");
    xhr.onreadystatechange = function() {
        xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200 ? console.log('Ready!') : console.log('Failed!');
    }
    xhr.send(message);
}