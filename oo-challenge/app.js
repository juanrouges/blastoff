// Part One

// Create a class for vehicle. Each vehicle instance should have the following properties:
// make
// model
// year
// Each vehicle instance should have access to a method called honk, which returns the string “Beep.”

// let myFirstVehicle = new Vehicle("Honda", "Monster Truck", 1999);
// myFirstVehicle.honk(); // "Beep."
// Each vehicle instance should have a method called toString, which returns the string containing the make, model and year.

// let myFirstVehicle = new Vehicle("Honda", "Monster Truck", 1999);
// myFirstVehicle.toString(); // "The vehicle is a Honda Monster Truck from 1999."

class Vehicle {
  constructor(make, model, year) {
    this.make = make;
    this.model = model;
    this.year = year;
  }

  honk() {
    return 'Beep.'
  }

  toString() {
    const {make, model, year} = this; 
    return 'The vehicle is a ' + make + ' ' + model + ' ' + year;
  }
}

let myFirstVehicle = new Vehicle("Honda", "Monster Truck", 1999);
console.log(myFirstVehicle.honk());
console.log(myFirstVehicle.toString());

// ******************************************************************************************************

// Part Two

// Create a class for a car. The Car class should inherit from Vehicle and each car instance should have a property called numWheels which has a value of 4.

// let myFirstCar = new Car("Toyota", "Corolla", 2005);
// myFirstCar.toString(); // "The vehicle is a Toyota Corolla from 2005."
// myFirstCar.honk();     // "Beep."
// myFirstCar.numWheels;  // 4

class Car extends Vehicle {
  constructor(make, model, year, wheels = 4) {
    super(make, model, year);
    this.wheels = wheels;
  }

  numWheels() {
    return this.wheels;
  }
}

let myFirstCar = new Car("Toyota", "Corolla", 2005);
console.log(myFirstCar.toString()); 
console.log(myFirstCar.honk());     
console.log(myFirstCar.numWheels()); 

// ******************************************************************************************************

// Part Three

// Create a class for a Motorcycle. This class should inherit from Vehicle and each motorcycle instance should have a property called numWheels which has a value of 2. It should also have a revEngine method which returns “VROOM!!!”

// let myFirstMotorcycle = new Motorcycle("Honda", "Nighthawk", 2000);
// myFirstMotorcycle.toString(); // "The vehicle is a Honda Nighthawk from 2000."
// myFirstMotorcycle.honk();     // "Beep."
// myFirstMotorcycle.revEngine(); // "VROOM!!!"
// myFirstMotorcycle.numWheels;  // 2