#!/usr/bin/node
function addMeMaybe(x, fn) {
  x = x + 1;
  fn(x);
}
module.exports = {
  addMeMaybe
};
