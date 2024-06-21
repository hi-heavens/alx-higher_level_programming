#!/usr/bin/node

const [, , ...otherArgs] = process.argv;

if (otherArgs.length) {
  console.log(`Argument${otherArgs.length > 1 ? 's' : ''} found`);
} else {
  console.log('No argument');
}
