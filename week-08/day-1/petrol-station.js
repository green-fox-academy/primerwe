'use strict';

let car = {
    petrolLevel: 0,
    petrolCapacity: 50,
    refill: function (amount) {
        let fuel = (amount + (this.petrolCapacity - amount)) - this.petrolLevel;
        this.petrolLevel += (amount + (this.petrolCapacity - amount)) - this.petrolLevel;
        return fuel;
    }
};

let station = {
    petrolStorage: 3000,
    provide: function(car) {
        this.petrolStorage -= car.refill(this.petrolStorage);
    }
};

console.log(car.petrolLevel);
console.log(station.petrolStorage);

station.provide(car);

console.log(car.petrolLevel);
console.log(station.petrolStorage);