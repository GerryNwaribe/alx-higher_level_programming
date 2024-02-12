#!/usr/bin/node
// Write a script that prints a square
const size = process.argv[2];
const sizeInt = parseInt(size);

if (isNaN(sizeInt)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < sizeInt; i++) {
    let row = '';
    for (let j = 0; j < sizeInt; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
