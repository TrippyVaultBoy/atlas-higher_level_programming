#!/usr/bin/node

const number = parseInt(process.argv[2]);

if (isNaN(number) || number < 1) {
  // do nothing
} else {
  for (let i = 0; i < number; i++) {
    console.log('C is fun');
  }
}
