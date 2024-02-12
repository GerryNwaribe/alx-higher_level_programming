#!/usr/bin/node
// Write a script that prints the addition of 2 integers
const arg1 = process.argv[2];
const arg2 = process.argv[3];

if (arg1 === undefined || isNaN(arg1) || arg2 === undefined || isNaN(arg2)) {
  console.log('NaN');
} else {
  function add (a, b) {
    const sum = parseInt(a) + parseInt(b);
    console.log(sum);
  }
  add(arg1, arg2);
}
