#!/usr/bin/node

const OldSquare = require('./5-square');

module.exports = class Square extends OldSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let rowString = '';
      for (let j = 0; j < this.width; j++) {
        rowString += c;
      }
      console.log(rowString);
    }
  }
};
