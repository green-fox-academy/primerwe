'use strict';
// Create a function that prints the ingredient list of dictionaries to the console in the following format:
//
// +--------------------+---------------+----------+
// | Ingredient         | Needs cooling | In stock |
// +--------------------+---------------+----------+
// | vodka              | Yes           | 1        |
// | coffee_liqueur     | Yes           | -        |
// | fresh_cream        | Yes           | 1        |
// | captain_morgan_rum | Yes           | 2        |
// | mint_leaves        | No            | -        |
// +--------------------+---------------+----------+
//
// OPTIONAL
// The frist columns should be automatically as wide as the longest key

const ingredients = [
	{ "name": "vodka", "in_stock": 1, "needs_cooling": true },
	{ "name": "coffee_liqueur", "in_stock": 0, "needs_cooling": true },
	{ "name": "fresh_cream", "in_stock": 1, "needs_cooling": true },
	{ "name": "captain_morgan_rum", "in_stock": 2, "needs_cooling": true },
	{ "name": "mint_leaves", "in_stock": 0, "needs_cooling": false },
	{ "name": "sugar", "in_stock": 0, "needs_cooling": false },
	{ "name": "lime juice", "in_stock": 0, "needs_cooling": true },
	{ "name": "soda", "in_stock": 0, "needs_cooling": true }
]

let longestWord = function getNameLength() {
    let longestWord = 0;
    ingredients.map(ingredient => ingredient.name.length > longestWord ? longestWord = ingredient.name.length : 0);
    return longestWord + 2;
}

function isTrueOrFalse(bool) {
    if (bool === true) {
        return 'Yes';
    }
    return 'NO';
}

function addStockValue(inStock) {
    if (inStock === 0) {
        return '-'
    }
    return inStock;
}

console.log('+' + '-'.repeat(longestWord()) + '+' + '-'.repeat(15) + '+' + '-'.repeat(10) + '+');
console.log('| ' + 'Ingredient' + ' '.repeat(longestWord() - 11) + '|' + ' Needs cooling ' + '|' + ' In stock ' + '|');
console.log('+' + '-'.repeat(longestWord()) + '+' + '-'.repeat(15) + '+' + '-'.repeat(10) + '+');
for (let i = 0; i < ingredients.length; i++) {
    console.log('| ' + ingredients[i].name + ' '.repeat(longestWord() - ingredients[i].name.length - 1) + '|' + ' '.repeat(6)
                + isTrueOrFalse(ingredients[i].needs_cooling) + ' '.repeat(9 - isTrueOrFalse(ingredients[i].needs_cooling).length)
                + '|' + ' '.repeat(5) + addStockValue(ingredients[i].in_stock) + ' '.repeat(5 - ingredients[i].in_stock.toString( ).length) + '|');
}
console.log('+' + '-'.repeat(longestWord()) + '+' + '-'.repeat(15) + '+' + '-'.repeat(10) + '+');
