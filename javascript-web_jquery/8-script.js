$(document).ready(function () {
  $.get("https://swapi-api.alx-tools.com/api/films/?format=json", function (data) {
    // Iterate through each movie in the fetched data
    data.results.forEach(function (movie) {
      // Append each movie title as a new list item to the UL#list_movies
      $('#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
});
