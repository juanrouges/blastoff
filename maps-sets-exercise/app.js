// Quick Question #1

// What does the following code return?
console.log(new Set([1,1,2,2,3,4]));
// {1,2,3,4}

// ********************************************

// Quick Question #2

// What does the following code return?
console.log([...new Set("referee")].join(""));
// ref

// ********************************************

// Quick Questions #3

// What does the Map m look like after running the following code?
let m = new Map();
console.log(m.set([1,2,3], true));
// [[1,2,3], true]
console.log(m.set([1,2,3], false));
// [[1,2,3], false]

// ********************************************

// hasDuplicate #4

// Write a function called hasDuplicate which accepts an array and returns true or false if that array contains a duplicate
console.log(hasDuplicate([1,3,2,1])); // true
console.log(hasDuplicate([1,5,-1,4])); // false

function hasDuplicate(arr) {
  return [...new Set(arr)].length === arr.length ? false : true;
}

// ********************************************

// vowelCount #4
 
//  Write a function called vowelCount which accepts a string and returns a map where the keys are numbers and the values are the count of the vowels in the string.
vowelCount('awesome') // Map { 'a' => 1, 'e' => 2, 'o' => 1 }
vowelCount('Colt') // Map { 'o' => 1 }

