--SELECT * FROM tracks t;
-- sqllite tutorial for select is
-- https://www.sqlitetutorial.net/sqlite-select/
-- we use -- for comments
-- Generally you want to limit results
-- maybe you get 1Million rows
-- most Database Management systems will limit rows for  you
-- Dbeaver limits you to 200 by default
-- as you scroll down you will see more results

-- SQL is case insensitive
-- Why?
-- SQL is a standard
-- SQL was started in the 70's
-- SQL was created by IBM
-- not all keyboards had upper case letters or lower case letters in 1970s
-- so SQL was created to be case insensitive

--SELECT * FROM albums a ;
-- a is just an alias for albums table could be any short text
-- aliases are used when we join multiple tables
-- to avoid typing the full table name

--SELECT * FROM albums a

--SELECT 
--    Title,
--    Name
--FROM 
--    albums
--INNER JOIN artists 
--    ON artists.ArtistId = albums.ArtistId;

--SELECT *
--FROM albums a 
--JOIN artists a2 
--ON a.ArtistId = a2.ArtistId;

SELECT * FROM artists a 
WHERE name LIKE "%Valdis%";

SELECT * FROM albums a 
WHERE a.ArtistId = 276;

--SELECT
--*
--FROM
--   artists
--LEFT JOIN albums ON
--   albums.ArtistId = artists.ArtistId
--ORDER BY
--   albums.ArtistId;

--so IF NOT EXISTS will prevent from overwiting old view
CREATE VIEW IF NOT EXISTS v_rock_songs
AS 
SELECT t.Name TrackName, 
	a.Title  AlbumTitle,
	a2.Name ArtistName,
	g.Name Genre,
	mt.Name MediaType,
	t.Milliseconds time_ms,
	t.Milliseconds/1000 seconds,
	t.Milliseconds/(1000*60) minutes,
	t.UnitPrice 
FROM tracks t
JOIN albums a 
ON t.AlbumId = a.AlbumId 
JOIN artists a2 
ON a.ArtistId = a2.ArtistId 
JOIN genres g 
ON t.GenreId = g.GenreId 
JOIN media_types mt 
ON t.MediaTypeId = mt.MediaTypeId
WHERE Genre = "Rock"
ORDER BY seconds DESC;
--LIMIT 20 -- so 20 longest rock songs in this database
--;
--WHERE a2.Name LIKE "Alanis%";

SELECT * FROM v_rock_songs vrs ;

SELECT * FROM v_rock_songs vrs 
WHERE ArtistName LIKE "David%";