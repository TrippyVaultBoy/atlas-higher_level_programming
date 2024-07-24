#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  if (list === undefined || searchElement === undefined) {
    return 0;
  }
  let count = 0;
  list.foreach((element) => {
    if (element === searchElement) {
      count++;
    }
  })

  return count;
}