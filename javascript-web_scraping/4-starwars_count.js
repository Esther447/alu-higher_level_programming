#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.log('Usage: ./4-starwars_count.js <API_URL>');
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  try {
    const data = JSON.parse(body);
    const films = data.results;
    const wedgeCount = films.filter(movie =>
      movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
    ).length;

    console.log(wedgeCount);
  } catch (error) { // ✅ Corrected variable name from `err` to `error`
    console.error('Error parsing JSON:', error);
  }
});
