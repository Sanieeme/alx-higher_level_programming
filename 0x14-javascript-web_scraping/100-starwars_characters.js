#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request({
  url: apiUrl,
  method: 'GET',
  strictSSL: false
}, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const movieData = JSON.parse(body);

    const characters = movieData.characters;

    const getCharacterData = (characterUrl) => {
      return new Promise((resolve, reject) => {
        request({
          url: characterUrl,
          method: 'GET',
          strictSSL: false
        }, function (charError, charResponse, charBody) {
          if (!charError && charResponse.statusCode === 200) {
            const characterData = JSON.parse(charBody);
            resolve(characterData);
          } else {
            reject(charError);
          }
        });
      });
    };
    Promise.all(characters.map(getCharacterData))
      .then((characterData) => {
        characterData.forEach((character) => {
          console.log(character.name);
        });
      })
      .catch((error) => {
        console.error('Error fetching character data:', error);
      });
  } else {
    console.error('Error fetching movie data:', error);
  }
});
