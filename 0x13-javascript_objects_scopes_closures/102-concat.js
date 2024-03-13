#!/usr/bin/node
// Write a script that concats 2 files.

const fs = require('fs');
if (process.argv.length !== 5) {
  console.log('Usage: ./concat_files.js source_file1 source_file2 destination_file');
  process.exit(1);
}

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

fs.readFile(fileA, 'utf8', (err, dataA) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }

  fs.readFile(fileB, 'utf8', (err, dataB) => {
    if (err) {
      console.error(err);
      process.exit(1);
    }

    const concatenatedData = dataA.trim() + '\n' + dataB.trim() + '\n';

    fs.writeFile(fileC, concatenatedData, 'utf8', (err) => {
      if (err) {
        console.error(err);
        process.exit(1);
      }
    });
  });
});
