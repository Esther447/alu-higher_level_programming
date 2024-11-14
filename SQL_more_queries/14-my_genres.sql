-- This script 
-- Select the title of the TV show from the tv_shows table
-- and the genre name from the tv_genres table

SELECT tv_shows.title, tv_genres.name
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id;
