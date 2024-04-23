#!/usr/bin/node
// script that displays the status code of a GET request

const request = require('request');

// Retrieve the URL from the command line arguments
const url = process.argv[2];

// Make a GET request to the specified URL
request.get(url, (error, response) => {
  if (error) {
    console.error(error);
    return;
  }

  // Display the status code
  console.log(`code: ${response.statusCode}`);
});
