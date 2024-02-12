#!/usr/bin/node
// Write a script that prints x times “C is fun”
if (process.argv.length < 3 || isNaN(Number(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  let times = Number(process.argv[2]);
  const message = 'C is fun';

  while (times--) {
    console.log(message);
  }
}
