'use strict';

var TennisGame3 = function (player1Name, player2Name) {
  this.player1point = 0;
  this.player2point = 0;

  this.player1Name = player1Name;
  this.player2Name = player2Name;
};

TennisGame3.prototype.getScore = function () {
  let s;
  if ((this.player1point < 4 && this.player2point < 4) && (this.player1point + this.player2point < 6)) {
    let p = ['Love', 'Fifteen', 'Thirty', 'Forty'];
    s = p[this.player1point];
    return (this.player1point == this.player2point) ? s + '-All' : s + '-' + p[this.player2point];
  } else {
    if (this.player1point == this.player2point)
      return 'Deuce';
    s = this.player1point > this.player2point ? this.player1Name : this.player2Name;
    return ((this.player1point - this.player2point) * (this.player1point - this.player2point) == 1) ? 'Advantage ' + s : 'Win for ' + s;
  }
};

TennisGame3.prototype.wonPoint = function (playerName) {
  if (playerName == 'player1')
    this.player1point += 1;
  else
    this.player2point += 1;

};

if (typeof window === 'undefined') {
  module.exports = TennisGame3;
}
