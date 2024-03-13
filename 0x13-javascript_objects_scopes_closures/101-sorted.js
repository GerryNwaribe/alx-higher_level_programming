#!/usr/bin/node
// Write a script that imports a dictionary of occurrences by user id
// and computes a dictionary of user ids by occurrence.

const { dict } = require('./101-data');
const newDict = Object.keys(dict)
  .sort()
  .reduce((acc, key) => {
    acc[dict[key]] = (acc[dict[key]] || []).concat(key);
    return acc;
  }, {});

console.log(newDict);
