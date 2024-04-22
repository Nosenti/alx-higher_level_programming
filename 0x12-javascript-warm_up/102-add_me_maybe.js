#!/usr/bin/node
function addMeMaybe (x, fn) {
  for (let i = 0; i < x; i++) {
    x = x + 1;
    fn();
  }
}
module.exports = {
  addMeMaybe
};
