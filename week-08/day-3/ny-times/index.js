'use strict';

let body = document.querySelector('body');

function searchArticles() {
  let xhr = new XMLHttpRequest;
  xhr.open('GET', 'https://api.nytimes.com/svc/search/v2/articlesearch.json?api_key=ba2ecf3fddea4636bc08a5bbcfa25b38&q=apollo&begin_date=19690716&end_date=19690719', true);
  xhr.onload = function () {
    let articles = JSON.parse(xhr.responseText);
    let mainArticles = articles.response.docs;
    //                console.log(mainArticles);
    mainArticles.forEach(function (article) {
      OneArticle(article);
    });
  };
  xhr.send();
};

function OneArticle(article) {
  let h1 = document.createElement('h1');
  h1.textContent = article.headline.main;
  body.appendChild(h1);

  let paragraph = document.createElement('p');
  paragraph.textContent = article.snippet;
  body.appendChild(paragraph);

  let pubDate = document.createElement('h4');
  pubDate.textContent = article.pub_date;
  body.appendChild(pubDate);

  let link = document.createElement('a');
  body.appendChild(link);
  link.textContent = 'Read more';
  link.setAttribute('href', article.web_url);
};

searchArticles();
