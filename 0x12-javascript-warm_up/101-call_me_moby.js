#!/usr/bin/node
// Write a function that executes x times a function
function callMeMoby (x, theFunction) {
  for (let a = 0; a < x; a++) {
    theFunction();
  }
}
module.exports.callMeMoby = callMeMoby;
