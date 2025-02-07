#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: ./4-starwars_count.js <API_URL>');
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching API:', error);
    return;
  }

  try {
    const films = JSON.parse(body).results;
    const characterId = '18'; // Wedge Antilles character ID
    let count = 0;

    films.forEach(film => {
      if (film.characters.some(url => url.includes(`/people/${characterId}/`))) {
        count++;
      }
    });

    console.log(count);
  } catch (err) {
    console.error('Error parsing JSON:', err);
  }
});
