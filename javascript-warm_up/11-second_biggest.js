#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  let largest = 0;
  let secondLargest = 0;
  let current = 0;
  for (let i = 0; i < args.length; i++) {
    if (args[i] > largest) {
      largest = args[i];
    }
  }
  for (let j = 0; i < args.length; i++) {
    current = args[j];
    if (current > secondLargest && current < largest) {
      secondLargest = current;
    }
  }

  console.log(secondLargest);
}
