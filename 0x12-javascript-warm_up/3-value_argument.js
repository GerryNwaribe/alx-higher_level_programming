#!/usr/bin/node
// Write a script that prints the first argument passed to it

const myVar = process.argv[2];

if (myVar === undefined) {
  console.log('No argument');
} else {
  console.log(myVar);
}
