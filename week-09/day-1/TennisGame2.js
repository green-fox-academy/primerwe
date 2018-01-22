'use strict';

var TennisGame2 = function (player1Name, player2Name) {
  this.player1point = 0;
  this.player2point = 0;

  this.player1result = '';
  this.player2result = '';

  this.player1Name = player1Name;
  this.player2Name = player2Name;
};

function determineGameScore(score) {
  return {
    0: 'Love',
    1: 'Fifteen',
    2: 'Thirty',
    3: 'Forty'
  }[score];
}

TennisGame2.prototype.getScore = function () {
  let score = '';

  if (this.player1point === this.player2point && this.player1point < 3) {
    score = determineGameScore(this.player1point)
    score += '-All';
  }

  if (this.player1point === this.player2point && this.player1point > 2)
    score = 'Deuce';

  if (this.player1point > 0 && this.player2point === 0) {
    this.player1result = determineGameScore(this.player1point)
    this.player2result = 'Love';
    score = this.player1result + '-' + this.player2result;
  }

  if (this.player2point > 0 && this.player1point === 0) {
    this.player1result = 'Love';
    this.player2result = determineGameScore(this.player2point);
    score = this.player1result + '-' + this.player2result;
  }

  if (this.player1point > this.player2point && this.player1point < 4) {
    this.player1result = determineGameScore(this.player1point);
    this.player2result = determineGameScore(this.player2point);
    score = this.player1result + '-' + this.player2result;
  }

  if (this.player2point > this.player1point && this.player2point < 4) {
    this.player2result = determineGameScore(this.player2point);
    this.player1result = determineGameScore(this.player1point);
    score = this.player1result + '-' + this.player2result;
  }

  if (this.player1point > this.player2point && this.player2point >= 3) {
    score = 'Advantage player1';
  }

  if (this.player2point > this.player1point && this.player1point >= 3) {
    score = 'Advantage player2';
  }

  if (this.player1point >= 4 && this.player2point >= 0 && (this.player1point - this.player2point) >= 2) {
    score = 'Win for player1';
  }

  if (this.player2point >= 4 && this.player1point >= 0 && (this.player2point - this.player1point) >= 2) {
    score = 'Win for player2';
  }
  return score;
};

TennisGame2.prototype.Setplayer1Score = function (number) {
  let i;
  for (i = 0; i < number; i++) {
    this.player1Score();
  }
};

TennisGame2.prototype.Setplayer2Score = function (number) {
  let i;
  for (i = 0; i < number; i++) {
    this.player2Score();
  }
};

TennisGame2.prototype.player1Score = function () {
  this.player1point++;
};

TennisGame2.prototype.player2Score = function () {
  this.player2point++;
};

TennisGame2.prototype.wonPoint = function (player) {
  if (player === 'player1')
    this.player1Score();
  else
    this.player2Score();
};

if (typeof window === 'undefined') {
  module.exports = TennisGame2;
}
