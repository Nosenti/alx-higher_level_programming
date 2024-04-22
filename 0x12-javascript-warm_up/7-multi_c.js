#!/usr/bin/node
const x = process.argv[2];
if (x == null) {
  console.log('Missing number of occurences');
} else if (parseInt(x) > 0) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
