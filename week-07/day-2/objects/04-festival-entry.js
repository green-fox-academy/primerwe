'use strict';

var watchlist = []

var security_alchol_loot = 0

var queue = [
	{ 'name': 'Amanda', 'alcohol': 10, 'guns': 1 },
	{ 'name': 'Tibi', 'alcohol': 0, 'guns': 0 },
	{ 'name': 'Dolores', 'alcohol': 0, 'guns': 1 },
	{ 'name': 'Wade', 'alcohol': 1, 'guns': 1 },
	{ 'name': 'Anna', 'alcohol': 10, 'guns': 0 },
	{ 'name': 'Rob', 'alcohol': 2, 'guns': 0 },
	{ 'name': 'Joerg', 'alcohol': 20, 'guns': 0 }
]

// Queue of festivalgoers at entry
// no. of alcohol units 
// no. of guns

// Create a security_check function that returns a list of festivalgoers who can enter the festival

// If guns are found, remove them and put them on the watchlist (only the names)
// If alcohol is found confiscate it (set it to zero and add it to security_alchol_loot) and let them enter the festival

function securityCheck(queue) {
    for(let i = 0; i < queue.length; i++) {
        if (queue[i].guns > 0) {
            queue[i].guns = 0;
            watchlist.push(queue[i].name);
        }
        if (queue[i].alcohol > 0) {
            security_alchol_loot += queue[i].alcohol;
            queue[i].alcohol = 0;
        }
    }
}

securityCheck(queue);

console.log('Watchlist: ' + watchlist);
console.log('Security alcohol loot: ' + security_alchol_loot);