#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    // Check if w and h are positive integers and greater than 0
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
