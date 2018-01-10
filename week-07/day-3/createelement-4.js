'use strict';

const kids = [{
        "pet_name": "Wattled crane",
        "owner": "Bryant"
    },
    {
        "pet_name": "Devil, tasmanian",
        "owner": "Alejandro"
    },
    {
        "pet_name": "Mynah, common",
        "owner": "Nelie"
    },
    {
        "pet_name": "Dolphin, common",
        "owner": "Mariele"
    },
    {
        "pet_name": "Gray duiker",
        "owner": "Maddalena"
    },
    {
        "pet_name": "Crab (unidentified)",
        "owner": "Lucine"
    },
    {
        "pet_name": "Ant (unidentified)",
        "owner": "Lorianna"
    },
    {
        "pet_name": "Bison, american",
        "owner": "Tommie"
    },
    {
        "pet_name": "Yellow mongoose",
        "owner": "Vivyan"
    },
    {
        "pet_name": "Carpet snake",
        "owner": "Veda"
    },
    {
        "pet_name": "Lesser mouse lemur",
        "owner": "Isidor"
    }];

let petsList = document.querySelector('div#pets');

for (let i = 0; i < kids.length; i++) {
    let newItem = document.createElement('article');
    let newH3 = document.createElement('h3');
    let newP = document.createElement('p');
    
    newH3.textContent = kids[i].owner;
    newP.textContent = kids[i].pet_name;
    
    petsList.appendChild(newItem);
    newItem.appendChild(newH3);
    newItem.appendChild(newP);
}
