#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    let str = '';
    for (let j = 0; j < num; j++) str += 'X';
    console.log(str);
  }
}
