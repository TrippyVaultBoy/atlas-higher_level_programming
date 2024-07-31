#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, response, content) => {
  if (err) {
    console.error('Error:', err);
    return;
  }
  if (response.statusCode !== 200) {
    console.error('Status:', response.statusCode);
    return;
  }
  const todos = JSON.parse(content);
  const tasksCompleted = {};

  todos.forEach((todo) => {
    if (todo.completed) {
      if (tasksCompleted[todo.userId]) {
        tasksCompleted[todo.userId]++;
      } else {
        tasksCompleted[todo.userId] = 1;
      }
    }
  });
  console.log(tasksCompleted);
});