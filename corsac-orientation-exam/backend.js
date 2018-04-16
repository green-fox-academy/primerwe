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
  database: 'space'
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

app.get('/planets', function (req, res) {
  connection.query(`SELECT * FROM planet`, function (err, rows) {
    res.send({
      "exam": rows
    })
  })
});

app.get('/ship', function (req, res) {
  connection.query(`SELECT * FROM spaceship`, function (err, row) {
    res.send({
      "id": row[0].id,
      "max capacity": row[0].max_capacity,
      "planet": row[0].planet,
      "utilization": row[0].utilization
    })
  })
});

app.put('/movehere/:planetId', function (req, res) {
  if (req.query.planet !== req.body.planet) {
    connection.query(`UPDATE spaceship SET planet="${req.query.planet}" WHERE id="${req.body.id}"`, function (err, result) {
      res.send({
        "result": "success"
      })
    })
  } else {
    res.send({
      "result": "error"
    })
  }
});

app.put('/toship/:planetId', function (req, res) {

})

app.put('/toplanet/:planetId', function (req, res) {
  connection.query(`UPDATE spaceship SET utilization=0 WHERE && UPDATE planet SET population='${req.body.population}' WHERE name='${req.body.planet}'`, function (err, result) {
    console.log('move everybody to the planet');
    res.send();
  });

})

connecToMySql();
app.listen(PORT, () => console.log(`The app is running at localhost: ${PORT}`));

/*let queryString = `SELECT name, planet FROM planet INNER JOIN spaceship ON planet.name=spaceship.planet`;*/
