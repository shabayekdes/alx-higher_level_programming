#!/usr/bin/node
const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, response, body) {
  console.log(err || JSON.parse(body).title);
});
