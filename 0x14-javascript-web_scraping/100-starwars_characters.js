#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, { json: true }, (error, response, body) => {
  if (error) {
    console.error('error:', error);
    return;
  }
  if (!body || response.statusCode !== 200) {
    console.error('Failed to retrieve movie data');
    return;
  }

  const characters = body.characters;
  characters.forEach((characterUrl) => {
    request(characterUrl, { json: true }, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        console.log(body.name);
      } else {
        console.error('Failed to retrieve character');
      }
    });
  });
});
