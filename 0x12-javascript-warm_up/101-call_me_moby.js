#!/usr/bin/node

/**
Write a function that executes x times a function.

- The function must be visible from outside
- Prototype: function (x, theFunction)
- You are not allowed to use var
*/
module.exports.callMeMoby = function (x, theFunction) {
  let i = 0;
  while (i < 3) {
    theFunction();
    i++;
  }
};
