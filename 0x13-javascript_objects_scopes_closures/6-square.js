#!/usr/bin/node

const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  charPrint (c) {
    let char;
    if (c === undefined) {
      char = 'X';
    } else {
      char = c;
    }
    for (let i = 0; i < this.width; i++) {
      let row = '';
      for (let j = 0; j < this.height; j++) {
        row = row + char;
      }
      console.log(row);
    }
  }
}
module.exports = Square;
