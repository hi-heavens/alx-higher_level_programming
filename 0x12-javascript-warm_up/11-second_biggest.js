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
      const iValue = parseInt(arr[i]);
      const jValue = parseInt(arr[j]);
      if (iValue < jValue) {
        [temp, arr[i]] = [iValue, jValue];
        arr[j] = temp;
      }
    }
  }
  console.log(arr[arr.length - 2]);
}
