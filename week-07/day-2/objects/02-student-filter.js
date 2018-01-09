'use strict';

var students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

// create a function that takes a list of students and logs:
// - Who has got more candies than 4 candies

// create a function that takes a list of students and logs: 
//  - how many candies they have on average

function whoHasGotMoreThenFourCandies() {
    let nameWhoHas = [];
    students.map(student => student.candies > 4 ? nameWhoHas.push(student.name) : 0);
    return nameWhoHas;
}

console.log(whoHasGotMoreThenFourCandies(students));

function howManyCandiesTheyHaveOnAverage() {
    let sumOfCandies = 0;
    students.map(student => sumOfCandies += student.candies);
    return sumOfCandies / students.length;
}

console.log(howManyCandiesTheyHaveOnAverage(students));