'use strict';

//let body = document.querySelector('body');
let apiUrl = 'https://time-radish.glitch.me';
let xhr = new XMLHttpRequest();

let getPosts = function () {
    xhr.open('GET', apiUrl + '/posts');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === xhr.DONE && xhr.status === 200) {
            let datas = JSON.parse(xhr.responseText).posts;
            console.log(datas);
            for (let i = 0; i < datas.length; i++) {
                if (datas[i].owner === null){
                    datas[i].owner = 'Annonymus';
                }
                const htmlContent = `
                <div class="vote">
                    <button class="arrow up">+</button>
                    <div class="score unvoted">${datas[i].score}</div>
                    <button class="arrow down">-</button>
                </div>
                <div class="content">
                    <h2>${datas[i].title} <span class="postUrl">${datas[i].url}</span></h2>
                    <p class="tagline">submitted ${parseInt(datas[i].timestamp/1000/60/60/24)} days ago by ${datas[i].owner}</p>
                    <ul>
                        <a href="#">Modify</a>
                        <a href="#">Remove</a>
                    </ul>
                </div>
                <div class="clearfix"></div>
                `;
                let posts = document.querySelector('section');
                posts.innerHTML += htmlContent;
            };
        }
    }
    xhr.send();
}

getPosts();
