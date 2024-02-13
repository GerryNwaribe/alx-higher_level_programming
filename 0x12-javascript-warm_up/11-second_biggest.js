#!/usr/bin/node
// Write a script that searches the second biggest integer in the list of arguments.
const args = process.argv.slice(2).map(Number);

if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  // Sort the arguments in descending order
  args.sort((a, b) => b - a);
  // Find the second largest integer
  const secondLargest = args[1];
  console.log(secondLargest);
}
