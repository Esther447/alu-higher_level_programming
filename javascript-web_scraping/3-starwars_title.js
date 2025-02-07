#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: ./3-starwars_title.js <movie_id>');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  try {
    const data = JSON.parse(body);
    console.log(data.title);
  } catch (err) {
    console.error('Error parsing JSON:', err);
  }
});
