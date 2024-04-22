#!/usr/bin/node
const x = parseInt(process.argv[2]);
if (x == null || isNaN(x)) {
  console.log('Missing size');
} else if (x <= 0) {
  console.log('');
} else {
  for (let i = 0; i < x; i++) {
    let col = '';
    for (let j = 0; j < x; j++) {
      col = col + 'X';
    }
    console.log(col);
  }
}
