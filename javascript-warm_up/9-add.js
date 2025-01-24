#!/usr/bin/node

// Define the add function
function add (a, b) {
  return a + b;
}

// Get the arguments passed to the script
const firstArg = parseInt(process.argv[2]);
const secondArg = parseInt(process.argv[3]);

// Print the result of adding the two integers
console.log(add(firstArg, secondArg));
