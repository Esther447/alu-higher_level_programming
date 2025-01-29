#!/usr/bin/node
const converter = require('./10-converter').converter;

let myConverter = converter(10);

console.log(myConverter(2));  // "2"
console.log(myConverter(12)); // "12"
console.log(myConverter(89)); // "89"

myConverter = converter(16);

console.log(myConverter(2));  // "2"
console.log(myConverter(12)); // "c"
console.log(myConverter(89)); // "59"
