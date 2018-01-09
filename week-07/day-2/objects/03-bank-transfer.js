'use strict';

var accounts = [
    {
        'client_name': 'Igor',
        'account_number': 11234543,
        'balance': 203004099.2
    },
    {
        'client_name': 'Vladimir',
        'account_number': 43546731,
        'balance': 5204100071.23
    },
    {
        'client_name': 'Sergei',
        'account_number': 23456311,
        'balance': 1353600.0
    }
]

// Create function that returns the name and balance of cash on an account

function returnAccountNameAndBalance(accountNumber) {
    let nameAndBalance = [];
    for (let i = 0; i < accounts.length; i++) {
        if (accounts[i].account_number === accountNumber) {
            nameAndBalance.push('Name: ' + accounts[i].client_name, 'Account number: ' + accounts[i].account_number);
            return nameAndBalance;
        }
    }
    return '404 - account not found';
}

console.log(returnAccountNameAndBalance(23456311));

// Create function that transfers an amount of cash from one account to another
// it should have three parameters:
//  - from account_number
//  - to account_number
//  - amount of cash to transfer

function transferCash(fromAccountNumber, toAccountNumber, amountOfCash) {
    if (isAccountExist(fromAccountNumber) && isAccountExist(toAccountNumber)) {
        accounts.map(account => account.account_number === fromAccountNumber ? account.balance -= amountOfCash : 0);
        accounts.map(account => account.account_number === toAccountNumber ? account.balance += amountOfCash : 0);
        return 'Success!'
    } else {
        return '404 - account not found!'
    }
}

console.log(transferCash(43546731, 11234543, 71.23));
console.log(accounts);
// Log "404 - account not found" if any of the account numbers don't exist to the console.

function isAccountExist(accountNumber2) {
    let account = []
    for (let i = 0; i < accounts.length; i++) {
        if (accounts[i].account_number === accountNumber2) {
            account.push('Name: ' + accounts[i].client_name, 'Account number: ' + accounts[i].account_number);
            return account;
        } else {
            return '404 - account not found';
        }
    }
}

console.log(isAccountExist(11324542)) 
console.log(isAccountExist(11234543)) 
