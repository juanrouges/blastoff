// 1. Refactor the above code to use two arrow functions. Turn it into a one-liner.
// function double(arr) {
//   return arr.map(function (val) {
//     return val * 2;
//   });
// }
// My answer
const double = (arr) => arr.map((val) => val * 2);

// 2. Replace ALL functions with arrow functions:
const series = [2, 3, 4, 6, 8, 9, 12, 45, 78, 89, 95, 145, 678];
// function squareAndFindEvens(numbers) {
//   var squares = numbers.map(function (num) {
//     return num ** 2;
//   });
//   var evens = squares.filter(function (square) {
//     return square % 2 === 0;
//   });
//   return evens;
// }
// My answer
const squareAndFindEvens = (numbers) => {
  const squares = numbers.map((num) => num ** 2);
  const evens = squares.filter((square) => square % 2 === 0);
  return evens;
};
console.log(squareAndFindEvens(series));
