#!/usr/bin/node
// script that reads and prints the content of a file.

// Importing the File System Module
const fs = require('fs');

function readFileContent (filePath) {
// Read the file using utf-8 encoding
  fs.readFile(filePath, 'utf-8', (err, data) => {
    // Handle any errors that occur during the reading process
    if (err) {
      console.error(err);
      return;
    }
    console.log(data);
  });
}

// Retrieve the file path from the command line arguments
const filePath = process.argv[2];
readFileContent(filePath);
