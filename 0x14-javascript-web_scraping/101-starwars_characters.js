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
    console.error('Failed to retrieve data');
    return;
  }

  const characters = body.characters;
  printCharacters(characters, 0);
});

const printCharacters = (characters, index) => {
  if (index >= characters.length) {
    return;
  }

  request(characters[index], { json: true }, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      console.log(body.name);
      printCharacters(characters, index + 1);
    } else {
      console.error('Failed to retrieve character');
    }
  });
};
