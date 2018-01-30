"use strict"

const mysql = require("mysql");
const express = require("express");
const bodyParser = require("body-parser");
const port = 8080;

const app = express();

app.use("/assets", express.static("assets"));
app.use(bodyParser.json());
app.use(function (req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept, Username");
  next();
});

const conn = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "123456",
  database: "licenseplates",
});

function connecToMySql() {
  conn.connect((err) => {
    if (err) {
      console.log("Connection failed!");
      return;
    };
    console.log("Connecteion established!");
  });
};

app.get("/", (req, res) => {
  res.sendFile(__dirname + "/index.html");
});

app.get("/search", function (req, res) {
  if (dataValidator(req.query)) {
    conn.query(`SELECT * FROM licence_plates WHERE plate LIKE "${req.query.q}%";`, function (err, rows) {
      if (rows.length === 0) {
        res.json({
          "result": "notFound",
          "message": "invalid input"
        });
      } else {
        res.json(dataToSend(rows));
      }
    });
  } else {
    res.json({
      "result": "error",
      "message": "invalid input"
    })
  }
});

function dataToSend(data) {
  return {
    result: "OK",
    data: data
  };
};

app.get("/search/:brand", function (req, res) {
  conn.query(`SELECT * FROM licence_plates WHERE car_brand LIKE "${req.params.brand}";`, function (err, rows) {
    res.json(dataToSend(rows));
  })
});

function dataValidator(data) {
  return (data.q.length < 8 && data.q.match(/^[a-z0-9-]+$/i) && data.q.length !== 0)
};

connecToMySql();

app.listen(port, function () {
  console.log("The app is running at localhost: " + port);
});
