#!/usr/bin/node
exports.esrever = function (list) {
  // function that returns the reversed version of a list
  const reversedList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  return reversedList;
};
