#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: ./4-starwars_count.js <API_URL>');
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  try {
    const data = JSON.parse(body);
    if (!data.results) {
      console.error('Invalid API response format');
      return;
    }

    const films = data.results;
    const wedgeId = '18'; // Wedge Antilles' character ID

    const wedgeCount = films.filter(movie =>
      movie.characters.some(url => url.includes(`/${wedgeId}`))
    ).length;

    console.log(wedgeCount);
  } catch (error) {
    console.error('Error parsing JSON:', error);
  }
});
