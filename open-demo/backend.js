'use strict';

const mysql = require('mysql');
const express = require('express');
const PORT = 8080;
const app = express();

app.use(express.static(__dirname + '/assets'));
app.use(express.json());
app.use(function (req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept, Username");
  next();
});

const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'root',
  database: 'open_demo'
});

function connecToMySql() {
  connection.connect((err) => {
    if (err) {
      console.log("Connection failed!");
      return;
    };
    console.log("Connecteion established!");
  });
};

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/assets/index.html');
});

app.get('/students', (req, res) => {
  connection.query(`SELECT student_name FROM students`, (err, rows) => {
    res.send({
      "students": rows
    })
  })
});

connecToMySql();
app.listen(PORT, () => console.log(`The app is running at localhost: ${PORT}`));
