#!/usr/bin/node
const request = require('request');

const filmId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

request(url, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else {
    const film = JSON.parse(body);
    console.log(`${film.title}`);
  }
});
