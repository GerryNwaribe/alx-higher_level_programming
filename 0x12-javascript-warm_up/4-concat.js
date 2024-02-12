#!/usr/bin/node
// Write a script that prints two arguments passed to it, in the following format: “ is ”
const arg1 = process.argv[2];
const arg2 = process.argv[3];

if (arg2 === undefined) {
  console.log(arg1, 'is undefined');
} else {
  console.log(arg1, 'is', arg2);
}
