#!/usr/bin/node
// Write a script that prints My number: <first argument converted in integer>
// if the first argument can be converted to an integer
const arg1 = process.argv[2];
const intValue = parseInt(arg1);

if (isNaN(intValue)) {
  console.log('Not a number');
} else {
  console.log('My number:', intValue);
}
