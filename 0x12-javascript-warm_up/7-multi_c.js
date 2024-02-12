#!/usr/bin/node
// Write a script that prints x times “C is fun”
const arg1 = process.argv[2];
const x = parseInt(arg1);

if (isNaN(x) || x < 0) {
  // Do nothing for negative numbers
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
