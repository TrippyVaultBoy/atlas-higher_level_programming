#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, (err, response, content) => {
  if (err) {
    console.error(err);
    return;
  }
  if (response.statusCode !== 200) {
    console.error('Status:', response.statusCode);
    return;
  }
  const todos = JSON.parse(content);
  const completed = {};

  todos.forEach(todo => {
    if (todo.completed) {
      if (completed[todo.userID]) {
        completed[todo.userID]++;
      } else {
        completed[todo.userID] = 1;
      }
    }
  });
  console.log(completed);
});