#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const out = {};

function count (todo) {
  if (todo.completed) {
    const userId = todo.userId.toString();
    out[userId] = out[userId] + 1 || 1;
  }
}

request(url, (error, request, body) => {
  if (error) throw error;
  if (request.statusCode === 200) {
    JSON.parse(body).forEach(count);
    console.log(out);
  }
});
