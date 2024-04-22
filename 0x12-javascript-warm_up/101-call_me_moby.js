#!/usr/bin/node
function callMeMoby (x, fn) {
  for (let i = 0; i < x; i++) {
    fn();
  }
}
module.exports = {
  callMeMoby
};
