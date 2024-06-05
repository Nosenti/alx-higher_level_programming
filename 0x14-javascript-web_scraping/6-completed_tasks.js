#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, { json: true }, (error, response, todos) => {
  if (error) {
    console.error('error:', error);
    return;
  }

  const completedTasks = {};
  todos.forEach((todo) => {
    if (todo.completed) {
      if (completedTasks[todo.userId]) {
        completedTasks[todo.userId] += 1;
      } else {
        completedTasks[todo.userId] = 1;
      }
    }
  });

  console.log(completedTasks);
});
