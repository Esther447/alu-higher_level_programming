#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: ./6-completed_tasks.js <API_URL>');
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching API:', error);
    return;
  }

  try {
    const todos = JSON.parse(body);
    const completedTasks = {};

    todos.forEach(task => {
      if (task.completed === true) { // Ensure task.completed is explicitly checked
        if (!completedTasks[task.userId]) {
          completedTasks[task.userId] = 0;
        }
        completedTasks[task.userId] += 1;
      }
    });

    console.log(completedTasks);
  } catch (err) {
    console.error('Error parsing JSON:', err);
  }
});
