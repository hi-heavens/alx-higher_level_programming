#!/usr/bin/node

const [, , ...otherArgs] = process.argv;

const convertNum = parseInt(otherArgs[0]);
console.log(isNaN(convertNum) ? 'Not a number' : `My number: ${convertNum}`);
