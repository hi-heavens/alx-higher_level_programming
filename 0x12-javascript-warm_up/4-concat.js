#!/usr/bin/node

const [, , ...otherArgs] = process.argv;

console.log(`${otherArgs[0]} is ${otherArgs[1]}`);
