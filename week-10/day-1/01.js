'use strict';

// Create a constructor for creating Animals.
// it should take one parameter: what the animal says
// Every animal should have a method called say() that prints what the animal says

class Animal {
  constructor() {
    this.says = '';
  }
  
  say(what) {
    console.log('The animal say ' + what)
  }
}

const cat = new Animal;
cat.say('miau');