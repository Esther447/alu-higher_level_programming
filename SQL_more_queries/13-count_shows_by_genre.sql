-- This script lists all genres from the hbtn_od_tvshows
-- display the number of shows linked to each genre
-- The results are sorted a by the number of shows in decreasing order.

SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
HAVING COUNT(tv_shsow_genres.show_id) > 0
ORDER BY number_of_shows DESC;
