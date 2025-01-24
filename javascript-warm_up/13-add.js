#!/usr/bin/node

// Define the add function with a space before the parentheses
function add (a, b) {
  return a + b;
}

// Export the function so it can be used outside this file
module.exports.add = add;
