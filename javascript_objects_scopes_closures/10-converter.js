#!/usr/bin/node

exports.converter = function (base) {
  return function (number) {
    return number.toString(base); // Convert the number to the specified base
  };
};
