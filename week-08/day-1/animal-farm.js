'use strict';

class Animal {
    constructor(type) {
        this.type = type;
        this.hunger = 5;
        this.thirst = 5;
    }

    eat() {
        if (this.hunger > 0) {
            this.hunger -= 1;
        }
    }

    drink() {
        if (this.thirst > 0) {
            this.thirst -= 1;
        }
    }

    play() {
        this.hunger += 1;
        this.thirst += 1;
    }
}

class Farm {
    constructor(slots) {
        this.slots = slots;
        this.animals = [];
        for (let i = 1; i <= slots; i++) {
            this.animals.push(new Animal('sheep'));
        }
    }

    breed() {
        if (this.animals.length < this.slots) {
            this.animals.push(new Animal('sheep'));
        }
    }

    slaugter() {
        let min = 99;
        let index = -1;
        for (let i = 0; i < this.animals.length; i++) {
            if (this.animals[i].hunger <= min) {
                min = this.animals[i].hunger;
                index = i;
            }
        }
        this.animals.splice(index, 1);
    }

    printReport() {
        if (this.animals.length === 0) {
            console.log('The farm has ' + this.animals.length + ' living animals, we are bankrupted!');
        } else {
            console.log('The farm has ' + this.animals.length + ' living animals.');
        }
        if (this.animals.length === this.slots) {
            console.log('The farm has ' + this.animals.length + ' living animals, we are full!');
        }
    }

    progress() {
        for (let i = 0; i < this.animals.length; i++) {
            if ((Math.floor((Math.random() * 2) + 1)) === 1) {
                this.animals[i].drink();
            }
            if ((Math.floor((Math.random() * 2) + 1)) === 1) {
                this.animals[i].eat();
            }
            if ((Math.floor((Math.random() * 2) + 1)) === 1) {
                this.animals[i].play();
            }
        }
        this.breed();
        this.slaugter();
        this.printReport();
    }
}

// Create a sheep farm with 20 slots
const SheepFarm = new Farm(20);

console.log(SheepFarm.animals); // Should log 20 Animal objects

const button = document.querySelector('button');

button.addEventListener('click', function () {
    SheepFarm.progress()
}, false);

// Add a click event to the button and call 'progress'

// The progress function should log the following to the console:
//  - The farm has 20 living animals, we are full
