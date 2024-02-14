#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  // function that returns the number of occurrences in a list
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }
  return count;
};
