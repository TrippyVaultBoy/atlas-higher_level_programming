#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
    if (w >= 0 || h >= 0) {
      return {}
    }
  }

  print(){
    for (let i = 0; i < this.height; i++) {
      rowString = "";
      for (let j = 0; j < this.width; j++) {
        rowString += "X";
      }
      console.log(rowString);
    }
  }
}
module.exports = Rectangle;
