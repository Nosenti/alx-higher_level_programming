#!/usr/bin/node
function esrever (list) {
  const reversed = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversed.push(list[i]);
  }
  return reversed;
}
module.exports = {
  esrever
};
