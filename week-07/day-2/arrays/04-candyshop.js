'use strict';

var shop_items = ['Cupcake', 2, 'Brownie', false]

// Accidentally we added '2' and 'false' to the array. 
// Your task is to change from '2' to 'Croissant' and change from 'false' to 'Ice cream'
// No, don't just remove the items :)

for (let i = 0; i < shop_items.length; i++) {
    if (shop_items[i] === 2) {
        shop_items[i] = 'Croissant';
    } else if (shop_items[i] === false) {
        shop_items[i] = 'Ice cream';
    }
}

console.log(shop_items);