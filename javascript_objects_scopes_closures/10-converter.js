#!/usr/bin/node

exports.converter = function (base) {
  return function (number) {
    return (number === 0) ? '0' : (exports.converter(base)(Math.floor(number / base))
  };
};
