#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filePath = process.argv[3];

request(url, { json: true }, (error, response, body) => {
  if (error) {
    console.error('error:', error);
  } else {
    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        console.error('error:', err);
      }
    });
  }
});
