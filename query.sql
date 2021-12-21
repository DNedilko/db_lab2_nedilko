--creating query to check if all the data was downloaded

--1 
SELECT types.type_name, count(anime.type_id) as num_of_records
FROM anime
INNER JOIN types
ON anime.type_id=types.type_id
group by types.type_name;

--2
SELECT episodes.members, anime.anime_name
FROM anime
INNER JOIN episodes
ON anime.anime_id = episodes.anime_id
ORDER BY members;

--3
SELECT AVG(rate_value), types.type_name, types.type_id
FROM anime
INNER JOIN ratings
USING(anime_id)
INNER JOIN types
ON types.type_id = anime.type_id
GROUP BY types.type_name, types.type_id ;