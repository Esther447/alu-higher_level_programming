-- This script lists all shows in the hbtn_0d_tvshows database,
-- displaying each show's title and its associated genre_id.
-- Shows without a genre will display NULL for the genre_id.
SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;

