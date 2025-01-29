#!/usr/bin/node

exports.converter = function (base) {
  return function (number) {
    if (number === 0) return '0';
    return exports.converter(base)(Math.floor(number / base)) + (number % base).toString(base).replace(/^0+/, '');  // Remove leading zeros
  };
};
