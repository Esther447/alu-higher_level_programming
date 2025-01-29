// Using let correctly in a function
let number = 10;
function converter(base) {
  return function (num) {
    let result = num.toString(base); // Declare result variable inside the function scope
    return result;
  };
}
