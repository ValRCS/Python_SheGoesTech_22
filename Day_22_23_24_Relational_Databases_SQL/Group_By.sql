--we will use GROUP BY TO provide statistics
--about some grouping 
-- in first example about albums

SELECT
	albumid,
	COUNT(trackid)
FROM
	tracks
GROUP BY
	albumid;
	
--how about getting total running length of each album?
SELECT
	t.albumid,
	a.Title AlbumTitle,
	a2.Name ArtistName,
	COUNT(trackid),
	SUM(Milliseconds)/(1000*60) AlbumLengthMinutes,
	AVG(Milliseconds)/(1000*60) AverageSongLengthMin,
	MIN(Milliseconds)/(1000*60) ShortestSongMin,
	MAX(Milliseconds)/(1000*60) LongestSongMin
FROM
	tracks t
JOIN albums a 
ON a.AlbumId = t.AlbumId 
JOIN artists a2 
ON a.ArtistId = a2.ArtistId 
GROUP BY
	t.albumid
--SO HAVING is similar to WHERE but we use it in GROUP BY situations
HAVING AlbumLengthMinutes < 80
ORDER BY AlbumLengthMinutes DESC;
--of course we could have created a view and then filtered later