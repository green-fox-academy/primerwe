'use strict';

const express = require('express');
const bodyParser = require('body-parser');

const app = express();

app.use('/assets', express.static('assets'));
app.use(bodyParser.json());

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

app.get('/doubling', (req, res) => {
  if (req.query.input === undefined) {
    res.json({
      "error": "Please provide an input!"
    })
  } else {
    res.json({
      "received": req.query.input,
      "result": req.query.input * 2,
    })
  }
});

app.get('/greeter', (req, res) => {
  if (req.query.name === undefined) {
    res.json({
      "error": "Please provide a name!"
    })
  } else if (req.query.title === undefined) {
    res.json({
      "error": "Please provide a title!"
    })
  } else {
    res.json({
      "welcome_message": "Oh, hi there " + req.query.name + ", my dear " + req.query.title + "!"
    })
  }
});

app.get('/appenda/:appendable', (req, res) => {
  res.json({"appended": req.params.appendable + "a"})
})

app.listen(8080);
