#!/usr/bin/node
'use strict';
/**
Write a function that executes x times a function.

- The function must be visible from outside
- Prototype: function (x, theFunction)
- You are not allowed to use var
*/
const callMeMoby = function (x, theFunction) {
  let i = 0;
  while (i < x) {
    theFunction();
    i++;
  }
};

module.exports = { callMeMoby };
