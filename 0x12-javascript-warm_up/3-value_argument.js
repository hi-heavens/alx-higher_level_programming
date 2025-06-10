#!/usr/bin/node

const [, , ...otherArgs] = process.argv;

console.log(otherArgs[0] ? otherArgs[0] : 'No argument');
