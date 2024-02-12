#!/usr/bin/node
// Write a script that computes and prints a factorial
const arg = parseInt(process.argv[2]);

function factorial (n) {
  if (isNaN(n)) {
    return 1; // Factorial of NaN is 1
  }
  if (n === 0 || n === 1) {
    return 1; // Base case: factorial of 0 and 1 is 1
  } else {
    return n * factorial(n - 1); // Recursive case: n * factorial(n-1)
  }
}

console.log(factorial(arg));
