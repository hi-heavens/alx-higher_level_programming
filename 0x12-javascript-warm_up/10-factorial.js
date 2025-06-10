#!/usr/bin/node

/**
Write a script that computes and prints a factorial

- The first argument is integer (argument can be cast as integer) used for computing the factorial
- Factorial of NaN is 1
- You must do it recursively
- You must use a function
*/
const value = parseInt(process.argv[2]);

function factorial (num) {
  if (isNaN(num) || num === 1) return 1;
  else return num * factorial(num - 1);
}

console.log(factorial(value));
