'use strict';

let apiUrl = 'https://time-radish.glitch.me';

function requestPosts(url) {
    let request = new XMLHttpRequest();
    request.open('GET', url);
    request.onerror = () => {
        console.log('connection error');
    }
    request.send();
    request.onload = function () {
        if (request.status === 200) {
            loadPost(JSON.parse(request.responseText).posts)
        } else {
            console.log('status not OK!')
        }
    }
};

function connection(method, url) {
    let xhr = new XMLHttpRequest();
    xhr.open(method, url);
    xhr.setRequestHeader("Content-type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200) {
            changeDatas(JSON.parse(xhr.responseText), method)
        } else {
            console.log('connection failed')
        }
    }
    xhr.send();
}

function changeDatas(data, method) {
    if (method === 'PUT') {
        document.querySelector(`div[data-id="${data.id}"]`).innerHTML = `${data.score}`
    } else {
        document.querySelector(`#post_article${data.id}`).remove();
    }
}

function loadPost(data) {
    let section = document.querySelector('section');
    data.forEach(function (item) {
        section.insertBefore(createPosts(item), section.firstChild);
        upVote(item.id);
        downVote(item.id);
        deletePost(item.id);
    })
}

function createPosts(post) {
    let item = document.createElement('article');
    item.setAttribute('id', `post_article${post.id}`);
    item.innerHTML = createPostHTML(post);
    return item;
}

function createPostHTML(post) {
    if (post.owner === null) {
        post.owner = 'Anonymus';
    }
    let htmlForPosts = `
    <div class="vote">
            <button id="up${post.id}" class="arrow up"></button>
            <div data-id="${post.id}" class="score ">${post.score}</div>
            <button id="down${post.id}" class="arrow down"></button>
        </div>
        <div class="content">
            <h2>${post.title} <a href="${post.url}" class="posturl">${post.url}</a></h2>
            <p class="tagline">submitted ${convertTime(post.timestamp)} hours ago by <span class="blue">${post.owner}</span></p>
            <ul>
                <li id="modify">Modify</li>
                <li id="remove">Remove</li>
            </ul>
        </div>
        <div class="clearfix"></div>
    `;
    return htmlForPosts;
}

function convertTime(timestamp) {
    let postDate = new Date(timestamp);
    let actualDate = Date.now();
    return parseInt((actualDate - postDate)/1000/60/60);
}

function upVote(postId) {
    document.querySelector('.arrow.up').addEventListener('click', function () {
        connection('PUT', `${apiUrl}/posts/${postId}/upvote`);
    })
}

function downVote(postId) {
    document.querySelector('.arrow.down').addEventListener('click', function () {
        connection('PUT', `${apiUrl}/posts/${postId}/downvote`);
    })
}

function deletePost(postId) {
    document.querySelector('#remove').addEventListener('click', function () {
        connection('DELETE', `${apiUrl}/posts/${postId}`)
    })
}

requestPosts(`${apiUrl}/posts`);
