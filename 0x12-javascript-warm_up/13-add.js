#!/usr/bin/node

/**
Write a function that returns the addition of 2 integers.

- The function must be visible from outside
- The name of the function must be add
*/
const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);

function add(a, b) {
  return a + b;
}

module.exports = { add };
