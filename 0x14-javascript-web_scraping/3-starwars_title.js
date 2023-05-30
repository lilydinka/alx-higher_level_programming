#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
request('https://swapi-api.alx-tools.com/api/films/' + id + '/', function (error, response, body) {  https://swapi-api.alx-tools.com/api/films/:id
  if (error == null) {
    const json = JSON.parse(body);
    console.log(json.title);
  }
});
