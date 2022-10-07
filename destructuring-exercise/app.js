// 1. Object Destructuring 1

// What does the following code return/print?
// let facts = {numPlanets: 8, yearNeptuneDiscovered: 1846};
// let {numPlanets, yearNeptuneDiscovered} = facts;

// console.log(numPlanets); // 8
// console.log(yearNeptuneDiscovered); // 1846

// ***********************************************************************

// 2. Object Destructuring 2

// What does the following code return/print?
let planetFacts = {
  numPlanets: 8,
  yearNeptuneDiscovered: 1846,
  yearMarsDiscovered: 1659
};

let {numPlanets, ...discoveryYears} = planetFacts;

console.log(discoveryYears); // { yearNeptuneDiscovered: 1846, yearMarsDiscovered: 1659}

// ***********************************************************************

// 3. Object Destructuring 3

//What does the following code return/print?
function getUserData({firstName, favoriteColor="green"}){
  return `Your name is ${firstName} and you like ${favoriteColor}`;
}

console.log(getUserData({firstName: "Alejandro", favoriteColor: "purple"})) // Your name is Alejandro and you like purple
console.log(getUserData({firstName: "Melissa"})) // Your name is Melissa and you like green
console.log(getUserData({})) // Error // Your name is undefined and you like green

// ***********************************************************************

// 4. Array Destructuring 1

// What does the following code return/print?
let [first, second, third] = ["Maya", "Marisa", "Chi"];

console.log(first); // Maya
console.log(second); // Marisa
console.log(third); // Chi

// ***********************************************************************

// 5. Array Destructuring 2

// What does the following code return/print?
let [raindrops, whiskers, ...aFewOfMyFavoriteThings] = [
  "Raindrops on roses",
  "whiskers on kittens",
  "Bright copper kettles",
  "warm woolen mittens",
  "Brown paper packages tied up with strings"
]

console.log(raindrops); // Raindrops on roses
console.log(whiskers); // whiskers on kittens
console.log(aFewOfMyFavoriteThings); // ["Bright copper kettles", "warm woolen mittens", "Brown paper packages tied up with strings"]

// ***********************************************************************

// 6. Array Destructuring 3

// What does the following code return/print?
let numbers = [10, 20, 30];
[numbers[1], numbers[2]] = [numbers[2], numbers[1]]

console.log(numbers) //[10 , 30, 20]

// ***********************************************************************

// 7. ES5 Assigning Variables to Object Properties

// Write an ES2015 Version
var obj = {
  numbers: {
    a: 1,
    b: 2
  }
};
// var a = obj.numbers.a;
// var b = obj.numbers.b;
// A: 
let { numbers: {a, b} } = obj;
console.log(a);
console.log(b);