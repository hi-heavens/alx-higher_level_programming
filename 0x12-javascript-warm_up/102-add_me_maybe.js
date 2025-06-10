#!/usr/bin/node
'use strict';
/**
Write a function that increments and calls a function.

- The function must be visible from outside
- Prototype: function (number, theFunction)
*/
const addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};

module.exports = { addMeMaybe };
