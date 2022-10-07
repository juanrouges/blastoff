// 1. In this exercise, you’ll refactor some ES5 code into ES2015.

// function filterOutOdds() {
//   var nums = Array.prototype.slice.call(arguments);
//   return nums.filter(function(num) {
//     return num % 2 === 0
//   });
// }

// Refactor it to use the rest operator & an arrow function:

// A:

const  filterOutOdds = (...arguments) => arguments.filter((num) => num % 2 === 0);

// ****************************************************************

// 2. findMin

// Write a function called findMin that accepts a variable 
// number of arguments and returns the smallest argument.

// Make sure to do this using the rest and spread operator.

// const findMin = (...args) => Math.min(...args)

// findMin(1,4,12,-3) // -3
// findMin(1,-1) // -1
// findMin(3,1) // 1

// A:
const numeros = [2, 4, 6, 8, 10, 1, 1.25]
const findMin = (...nums) => {
  return nums.reduce((min, next) => min < next ? min : next)
}
console.log(findMin(...numeros));

// ****************************************************************

// 3. mergeObjects

// Write a function called mergeObjects that accepts two objects and 
// returns a new object which contains all the keys and values of the 
// first object and second object.

// mergeObjects({a:1, b:2}, {c:3, d:4}) // {a:1, b:2, c:3, d:4}

// A:
const firstList = {a:1, b:2};
const secondList = {c:3, d:4};
const mergeObjects = (a, b) => ({...a, ...b}); // need parenthesis, otherwise error
console.log(mergeObjects(firstList, secondList));

// ****************************************************************

// 4. doubleAndReturnArgs

// Write a function called doubleAndReturnArgs which accepts an array and 
// a variable number of arguments. The function should return a new array 
// with the original array values and all of additional arguments doubled.

// doubleAndReturnArgs([1,2,3],4,4) // [1,2,3,8,8]
// doubleAndReturnArgs([2],10,4) // [2, 20, 8]

// A:
const doubleAndReturnArgs = (arr, ...more) => {
  const double = more.map((v) => v * 2);
  return [...arr, ...double];
}
console.log(doubleAndReturnArgs([1,2,3],4,4));
console.log(doubleAndReturnArgs([2],10,4));



