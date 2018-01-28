'use strict';

const mysql = require('mysql');
const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const port = 8080;

const app = express();
app.use(cors());
app.use(bodyParser.json());
app.use(express.urlencoded());

/*const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '123456',
  database: 'bookstore'
});

connection.connect((err) => {
    if (err) throw err;
    console.log('Connecteion established!');
});*/

let posts = [
  {
  "id": 25,
  "title": "Dear JavaScript",
  "url": "http://9gag.com",
  "timestamp": 14943395,
  "score": 793,
  "owner": null,
  "vote": 1
},
{
  "id": 74,
  "title": "Crockford",
  "url": "http://9gag.com",
  "timestamp": 14941384,
  "score": 567,
  "owner": "kristof4",
  "vote": -1
}];

app.get('/posts', function(req, res) {
    res.json({
        "posts": posts,
    });
});

app.put('/posts/:id/upvote', function(req, res) {
    posts.forEach(item => item.id === parseInt(req.params.id, 10) ? item.score++ : item.score);
    res.json();
});

app.put('/posts/:id/downvote', function(req, res) {
    posts.forEach(item => item.id === parseInt(req.params.id, 10) ? item.score-- : item.score);
    res.json();
});

app.delete('posts/:id', function(req, res) {
    let index = 0;
    posts.forEach(item => item.id === parseInt(req.params.id, 10) ? posts.splice(index, 1): index++);
});

app.post('/posts', function (req, res) {
  req.body.id = Math.max(0, Math.max.apply(null, posts.map(post => post.id))) + 1;
  req.body.timestamp = Date.now();
  posts.push(req.body);
});

