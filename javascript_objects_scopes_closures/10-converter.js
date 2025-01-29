#!/usr/bin/node

exports.converter = function (base) {
  return function (number) {
    // Convert the number to the desired base
    let result = number.toString(base);

    // Ensure that there's no leading zero when the base is 10
    if (base === 10 && result[0] === '0' && result.length > 1) {
      result = result.slice(1);
    }

    return result;
  };
};
