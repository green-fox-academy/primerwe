'use strict';

const express = require('express');
const bodyParser = require('body-parser');

const app = express();

app.use(bodyParser.json());

app.post('/arrays', (req, res) => {
  let numbers = req.body.numbers;
  if (req.body.what === "sum" && numbers.length !== 0) {
    res.json({
      "result": sumArray(numbers)
    })
  } else if (req.body.what === "multiply" && numbers.length !== 0) {
    res.json({
      "result": multiplyArray(numbers)
    })
  } else if (req.body.what === "double" && numbers.length !== 0) {
    res.json({
      "result": doubleArray(numbers)
    })
  } else {
    res.json({
      "error": "Please provide what to do with the numbers!"
    })
  }
});

function sumArray(numbers) {
  let result = 0;
  numbers.forEach(number => result += number);
  return result;
};

function multiplyArray(numbers) {
  let result = 1;
  numbers.forEach(number => result *= number);
  return result;
};

function doubleArray(numbers) {
  return numbers.map(number => number * 2);
};

app.listen(8080, function () {
  console.log('the app is running');
});
