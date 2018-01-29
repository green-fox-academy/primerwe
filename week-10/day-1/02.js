'use strict';

// Create a constructor for creating Rectangles.
// it should take two parameters: the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference

function Rectangle(a, b) {

  this.getArea = function () {
    let area = a * b;
    console.log('The area is: ' + area);
  }

  this.getCircumference = function () {
    let circum = 2 * (a + b);
    console.log('The circumference is: ' + circum);
  }
}

const rect = new Rectangle(5, 10);
rect.getArea();
rect.getCircumference();
