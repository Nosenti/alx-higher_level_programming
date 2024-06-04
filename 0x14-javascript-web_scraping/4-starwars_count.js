#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.error('error:', error);
  } else {
    let count = 0;
    const films = body.results || [];
    films.forEach((film) => {
      if (
        film.characters.includes(
          `https://swapi-api.alx-tools.com/api/people/18/`
        )
      ) {
        count++;
      }
    });
    console.log(count);
  }
});
