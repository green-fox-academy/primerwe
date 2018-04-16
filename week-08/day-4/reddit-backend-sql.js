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

const conn = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '123456',
  database: 'posts',
});

function connecToMySql() {
  conn.connect((err) => {
    if (err) throw err;
    console.log('Connecteion established!');
  });
};

connecToMySql();

function databaseError(err) {
  if (err) throw err;
  res.status(500).send('Database error');
}

app.get('/posts', function (req, res) {
  conn.query('SELECT * FROM articles ORDER BY score DESC;', function (err, rows) {
    databaseError();
    res.json({
      'posts': rows
    });
  });
});

app.post('/posts', function (req, res) {
  req.body.timestamp = Date.now() / 3600000;
  conn.query('INSERT INTO articles SET ?', req.body, (err, result) => {
    databaseError();
    console.log('saved')
    res.send();
  });
});

app.delete('/posts/:id', function (req, res) {
  conn.query('DELETE FROM articles WHERE id = ?', [req.params.id], (err, result) => {
    databaseError();
    console.log('deleted')
    res.send();
  });
});

app.put('/posts/:id/upvote', function (req, res) {
  conn.query('UPDATE articles SET score = ? WHERE id = ?', [req.body.score, req.body.id], (err, result) => {
    databaseError();
    console.log('upvoted')
    res.send();
  });
});

app.put('/posts/:id/downvote', function (req, res) {
  conn.query('UPDATE articles SET score = ? WHERE id = ?', [req.body.score, req.body.id], (err, result) => {
    databaseError();
    console.log('downvoted')
    res.send();
  });
});

app.listen(port, function () {
  console.log("The app is running at localhost: " + port);
});
