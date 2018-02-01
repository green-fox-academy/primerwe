'use strict';

const mysql = require('mysql');
const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const port = 8080;
const app = express();

app.use('/assets', express.static('assets'));
app.use(bodyParser.json());
app.use(cors());

const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '123456',
  database: 'bookstore'
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
  res.sendFile(__dirname + '/index.html');
});

app.get('/books', function (req, res) {
  let data = [];
  let queryString = `
    SELECT book_name, aut_name, cate_descrip, pub_name, book_price 
    FROM book_mast 
    INNER JOIN author ON book_mast.aut_id=author.aut_id 
    INNER JOIN category ON book_mast.cate_id=category.cate_id 
    INNER JOIN publisher ON book_mast.pub_id=publisher.pub_id
  `;
  if (req.query.category || req.query.publisher || req.query.priceLo || req.query.priceHi) {
    queryString += ' WHERE ';
    if (req.query.category) {
      queryString += `cate_descrip LIKE '%${req.query.category}%'`;
    }
    if (req.query.publisher) {
      queryString += ` AND pub_name LIKE '%${req.query.publisher}%'`;
    }
    if (req.query.priceLo) {
      queryString += ` AND book_price >= '${req.query.priceLo}'`;
    }
    if (req.query.priceHi) {
      queryString += ` AND book_price <= '${req.query.priceHi}'`;
    }
    queryString = queryString.replace('WHERE  AND', 'WHERE');
  }
  
  connection.query(queryString, function(err, result, fileds) {
      result.forEach(function(element){
        data.push({'title': element.book_name, 'author': element.aut_name, 'category': element.cate_descrip, 'publisher': element.pub_name, 'price': element.book_price})
      });
      res.send({'books': data});
  });
});

connecToMySql();
app.listen(port, function () {
  console.log('The app is running at localhost: ' + port);
});
