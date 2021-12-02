COPY anime(name,type,episodes,rating,members)
FROM 'F:\DB introd data\fixed.csv'
DELIMITER ';'
CSV HEADER;


INSERT INTO types(name)
SELECT DISTINCT(type)
FROM anime
WHERE type is NOT NULL;

select * from types;
select * from anime;
select * from episodes;



-- select * from information 
-- INNER join types
-- ON types.id = information.type

INSERT INTO information(name, type)
SELECT anime.name, types.id
FROM anime
INNER JOIN types
ON types.name = anime.type;


delete from episodes;


INSERT INTO episodes(an_id, episodes, members)
SELECT DISTINCT(information.id), episodes, members 
FROM information
INNER JOIN anime
USING(name)
ORDER BY information.id;

select * from episodes;

INSERT INTO rates(id,value)
SELECT DISTINCT(information.id), rating 
FROM information
INNER JOIN anime
USING(name)

SELECT * FROM information;
SELECT * FROM rates;
SELECT * FROM episodes;
SELECT * FROM types;

SELECT information.id, information.name, types.name, episodes.episodes, episodes.members, rates.value
FROM information
INNER JOIN types 
ON information.type = types.id
INNER JOIN rates
ON information.id = rates.id
INNER JOIN episodes
ON information.id = episodes.an_id;



