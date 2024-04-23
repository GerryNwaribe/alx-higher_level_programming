#!/usr/bin/node
// script that writes a string to a file.

// Importing the File System Module
const fs = require('fs');

function writeFileContent (filePath, string) {
// Read the file using utf-8 encoding
  fs.writeFile(filePath, string, 'utf-8', (err) => {
  // Handle any errors that occur during the reading process
    if (err) {
      console.error(err);
      return;
    }
    console.log(string);
  });
}

// Retrieve the file path from the command line arguments
const filePath = process.argv[2];
const string = process.argv[3];
writeFileContent(filePath, string);
