'use strict';
// Add "My todo:" to the beginning of the todoText
// Add " - Download games" to the end of the todoText
// Add " - Diablo" to the end of the todoText but with indention

// Expected outpt:

// My todo:
//  - Buy milk
//  - Download games
//      - Diablo

var todoText = " - Buy milk\n";
let myTodo = "My todo:\n"
let toDos = " - Download games\n";
let games = "   - Diablo";

console.log(myTodo.concat(todoText, toDos, games));