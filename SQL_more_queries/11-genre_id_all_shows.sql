-- this script lists all shows in the hbtn_od_ztcshows,
-- displaying each show's title and its associated genre_id.
-- Shows without a genre will display NULL for the genre_id.
-- Results are sorted in ascending order by title.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
