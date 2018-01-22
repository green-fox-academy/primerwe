'use strict';

var TennisGame1 = function (player1Name, player2Name) {
  this.gameScore1 = 0;
  this.gameScore2 = 0;
  this.player1Name = player1Name;
  this.player2Name = player2Name;
};

TennisGame1.prototype.wonPoint = function (playerName) {
  if (playerName === 'player1') {
    this.gameScore1 += 1;
  } else {
    this.gameScore2 += 1;
  }
};

TennisGame1.prototype.getScore = function () {
  let score = '';
  let tempScore = 0;
  if (this.gameScore1 === this.gameScore2) {
    switch (this.gameScore1) {
      case 0:
        score = 'Love-All';
        break;
      case 1:
        score = 'Fifteen-All';
        break;
      case 2:
        score = 'Thirty-All';
        break;
      default:
        score = 'Deuce';
        break;
    }
  } else if (this.gameScore1 >= 4 || this.gameScore2 >= 4) {
    let minusResult = this.gameScore1 - this.gameScore2;
    if (minusResult === 1) {
      score = 'Advantage player1';
    } else if (minusResult === -1) {
      score = 'Advantage player2';
    } else if (minusResult >= 2) {
      score = 'Win for player1';
    } else {
      score = 'Win for player2';
    };
  } else {
    for (let i = 1; i < 3; i++) {
      if (i === 1) {
        tempScore = this.gameScore1;
      } else {
        score += '-';
        tempScore = this.gameScore2;
      }
      switch (tempScore) {
        case 0:
          score += 'Love';
          break;
        case 1:
          score += 'Fifteen';
          break;
        case 2:
          score += 'Thirty';
          break;
        case 3:
          score += 'Forty';
          break;
      }
    }
  }
  return score;
};

if (typeof window === 'undefined') {
  module.exports = TennisGame1;
}
