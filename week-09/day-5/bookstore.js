'use strict';

const mysql = require('mysql');
const express = require('express');
const port = 8080;
const app = express();

const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '123456',
  database: 'bookstore'
});

connection.connect((err) => {
  if (err) throw err;
  console.log('Connecteion established!');
});

app.get('/', function (req, res) {
  connection.query('SELECT book_name FROM book_mast;', function (err, rows) {
    if (err) {
      console.log(err.toString());
      res.status(500).send('Database error');
      return;
    }
    res.send(rows);
  });
});

app.listen(port, function () {
  console.log("The app is running at localhost: " + port);
});
