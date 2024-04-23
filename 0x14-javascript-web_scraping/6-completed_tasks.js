#!/usr/bin/node
const request = require('request');

function fetchTasks (callback) {
  const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

  request(apiUrl, { json: true }, (err, res, body) => {
    if (err) {
      return callback(err, null);
    }
    if (res.statusCode !== 200) {
      return callback(new Error('Failed to fetch tasks'), null);
    }
    callback(null, body);
  });
}

function tasksCompletedByUserId (tasks, userId) {
  return tasks.filter(task => task.userId === userId && task.completed).length;
}

fetchTasks((err, tasks) => {
  if (err) {
    console.error('Error fetching tasks:', err);
    return;
  }
  const result = {};
  for (let i = 1; i <= 10; i++) {
    result[i.toString()] = tasksCompletedByUserId(tasks, i);
  }

  console.log(result);
});
