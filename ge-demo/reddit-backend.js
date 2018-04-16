'use strict';

const mysql = require('mysql');
const express = require('express');
const cors = require('cors');
// const bodyParser = require('body-parser');
const PORT = 8080;

const app = express();
app.use(cors());
app.use(express.json());
app.use(express.urlencoded());
app.use(express.static(__dirname + '/assets'))

let posts = [{
    "id": 25,
    "title": "Dear JavaScript",
    "url": "http://9gag.com",
    "timestamp": 1514913143395,
    "score": 793,
    "owner": null,
    "vote": 1
  },
  {
    "id": 74,
    "title": "Crockford",
    "url": "http://9gag.com",
    "timestamp": 1514913141384,
    "score": 567,
    "owner": "kristof4",
    "vote": -1
  },
  {
    "id": 114,
    "title": "Stranger things",
    "url": "http://9gag.com",
    "timestamp": 1523540536254,
    "score": 1567,
    "owner": "UFO",
    "vote": 1
  }
];

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/assets/index.html');
})

app.get('/posts', (req, res) => {
  res.json({
    "posts": posts,
  });
});

app.put('/posts/:id/upvote', (req, res) => {
  posts.forEach(item => item.id === req.params.id ? item.score++ : item.score);
  res.json();
});

app.put('/posts/:id/downvote', (req, res) => {
  posts.forEach(item => item.id === req.params.id ? item.score-- : item.score);
  res.json();
});

app.delete('posts/:id', (req, res) => {
  let index = 0;
  posts.forEach(item => item.id === req.params.id ? posts.splice(index, 1) : index++);
});

app.post('/posts', (req, res) => {
  req.body.id = Math.max(0, Math.max.apply(null, posts.map(post => post.id))) + 1;
  req.body.timestamp = Date.now();
  posts.push(req.body);
});

app.listen(PORT, () => {
  console.log(`The app is running at localhost: ${PORT}`);
});
