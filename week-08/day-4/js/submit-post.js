'use strict';

let apiUrl = 'https://time-radish.glitch.me';
let submitButton = document.querySelector('button.btn');
submitButton.addEventListener('click', submit);

function postRequest(request) {
    let xhr = new XMLHttpRequest();
    xhr.open('POST', apiUrl, true);
    xhr.setRequestHeader('Accept', 'application/json');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.setRequestHeader('Username', 'betterLateThanNever');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            console.log('ready state = done');
            if (xhr.status === 200) {
                console.log('status = OK');
                let request = xhr.responseText;
            }
        }
    }
    request = JSON.stringify(request);
    xhr.send(request)
};

function visualizePost() {
    let postText = document.querySelector('#title').value;
    let postUrl = document.querySelector('#url').value;
    
    let sendForPost = new Object();
    sendForPost.title = String(postText);
    sendForPost.url = String(postUrl);
    sendForPost.owner = "betterLateThanNever";
    
    let dataToSend = JSON.stringify(sendForPost);
    console.log(dataToSend);
}

function submit() {
    postRequest(visualizePost());
}