#!/usr/bin/node
function converter (b) {
  return function convert (num) {
    return num.toString(b);
  };
}
module.exports = {
  converter
};
