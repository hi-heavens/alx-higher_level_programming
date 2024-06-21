#!/usr/bin/node

/**
Write a script that searches the second biggest integer in the list of arguments.

- You can assume all arguments can be converted to integer
- If no argument passed, print 0
- If the number of arguments is 1, print 0
*/
const [, , ...arr] = process.argv;

const size = arr.length;

if (size <= 1) console.log(0);
else {
  for (let i = 0; i < arr.length; i++) {
    let temp;
    for (let j = 0; j < arr.length; j++) {
      if (arr[i] < arr[j]) {
        [temp, arr[i]] = [arr[i], arr[j]];
        arr[j] = temp;
      }
    }
  }
  console.log(parseInt(arr[arr.length - 2]));
}
