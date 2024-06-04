#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, { json: true }, (error, response, body) => {
  if (error) {
    console.error('error:', error);
  } else if (response.statusCode === 200) {
    console.log(body.title);
  } else {
    console.log(
      `Failed to retrieve data: HTTP status code ${response.statusCode}`
    );
  }
});
