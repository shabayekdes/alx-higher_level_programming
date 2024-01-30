#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (!err) {
    const todos = JSON.parse(body);

    const completed = todos.reduce((acc, todo) => {
      if (todo.completed) {
        const { userId } = todo;
        acc[userId] = (acc[userId] || 0) + 1;
      }
      return acc;
    }, {});

    console.log(completed);
  } else {
    console.error('Error:', err);
  }
});
