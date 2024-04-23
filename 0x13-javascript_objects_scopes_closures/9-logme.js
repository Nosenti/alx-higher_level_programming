#!/usr/bin/node
let numCalls = 0;
function logMe (c) {
  console.log(numCalls + ': ' + c);
  numCalls++;
}
module.exports = {
  logMe
};
