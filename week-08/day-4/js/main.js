'use strict';

let body = document.querySelector('body');
let apiUrl = 'https://time-radish.glitch.me';

let getPosts = function () {
    let xhr = new XMLHttpRequest();
    xhr.open('GET', apiUrl + '/posts');
    xhr.send(null);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            let datas = JSON.parse(xhr.responseText).posts;
            console.log(datas);
            for (let i = 0; i < datas.length; i++) {
                const htmlContent = `
                <div class="vote">
                    <button class="arrow up">+</button>
                    <div class="score unvoted">${datas[i].score}</div>
                    <button class="arrow down">-</button>
                </div>
                <div class="content">
                    <h2>${datas[i].title}</h2>
                    <p class="tagline">submitted</p>
                    <ul>
                        <li><a href="#">Modify</a></li>
                        <li><a href="#">Remove</a></li>
                    </ul>
                </div>
                <div class="clearfix"></div>
                `;
                let posts = document.querySelector('section');
                posts.innerHTML += htmlContent;
            };
        }
    }
}

getPosts();
