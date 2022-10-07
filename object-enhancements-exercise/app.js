// 1. Same keys and values

// Write an ES2015 Version of:

// function createInstructor(firstName, lastName){
//   return {
//     firstName: firstName,
//     lastName: lastName
//   }
// }

// A: 
const createInstructor = (first, last) => {
  return {
    first,
    last,
  }
}
console.log(createInstructor('Juan', 'Rojas'));

// ***************************************************************

// 2. Computed Property Names

// Write an ES2015 Version of :

// var favoriteNumber = 42;
// var instructor = {
//   firstName: "Colt"
// }

// instructor[favoriteNumber] = "That is my favorite!"

const instructor = {name: 'Colt'};
instructor[42] = 'That is my favorite';
console.log(instructor);

// ***************************************************************

// 3. Object Methods

// Write an ES2015 Version of:

// var instructor = {
//   firstName: "Colt",
//   sayHi: function(){
//     return "Hi!";
//   },
//   sayBye: function(){
//     return this.firstName + " says bye!";
//   }
// }

// A: 
const greetInstructor = {
  firstName: 'Colt',
  sayHi() {
    return 'Hi!'
  },
  sayBye() {
    return `${this.firstName} says bye!`
  }
}
console.log(greetInstructor.sayHi());
console.log(greetInstructor.sayBye());




