#!/usr/bin/node
function nbOccurences (list, el) {
  let occ = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === el) {
      occ = occ + 1;
    }
  }
  return occ;
}
module.exports = {
  nbOccurences
};
