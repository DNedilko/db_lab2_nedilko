--creating query to check if all the data was downloaded

--1 
SELECT count(information.type) as num_of_records, types.name
FROM information
INNER JOIN types
ON information.type=types.id
group by types.name;

--2
SELECT episodes, information.name
FROM information
INNER JOIN episodes
ON information.id = episodes.an_id
ORDER BY members DESC
LIMIT 10;

--3
SELECT AVG(value), types.name, type
FROM information
INNER JOIN rates
USING(id)
INNER JOIN types
ON types.id = information.type
GROUP BY types.name, type ;