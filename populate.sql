-- COPY anime(name,type,episodes,rating,members)
-- FROM 'F:\DB introd data\fixed.csv'
-- DELIMITER ';'
-- CSV HEADER;



select * from types;
select * from anime;
select * from episodes;
select * from ratings;

INSERT INTO types(type_name) VALUES('TV');
INSERT INTO types(type_name) VALUES('Movie');
INSERT INTO types(type_name) VALUES('OVA');
INSERT INTO types(type_name) VALUES('Special');
select * from types;

-- select * from information 
-- INNER join types
-- ON types.id = information.type

INSERT INTO anime(anime_name, type_id)
VALUES('K-On! Movie',2);
INSERT INTO anime(anime_name, type_id)
VALUES('Fullmetal Alchemist: Brotherhood',1);
INSERT INTO anime(anime_name, type_id)
VALUES('Gintama?',1);
INSERT INTO anime(anime_name, type_id)
VALUES('Ginga Eiyuu Densetsu',3);
INSERT INTO anime(anime_name, type_id)
VALUES('Mushishi Special: Hihamukage',4);
INSERT INTO anime(anime_name, type_id)
VALUES('Howl no Ugoku Shiro',2);
select * from anime;

INSERT INTO episodes(anime_id, episodes, members)
VALUES(1, 1, 115252);
INSERT INTO episodes(anime_id, episodes, members)
VALUES(2, 51, 600384);
INSERT INTO episodes(anime_id, episodes, members)
VALUES(3, 201, 336376);
INSERT INTO episodes(anime_id, episodes, members)
VALUES(4, 101, 80679);
INSERT INTO episodes(anime_id, episodes, members)
VALUES(5, 1, 49036);
select * from episodes;

INSERT INTO ratings(anime_id, rate_value)
VALUES(1, 8.15);
INSERT INTO ratings(anime_id, rate_value)
VALUES(2, 9);
INSERT INTO ratings(anime_id, rate_value)
VALUES(3, 7.45);
INSERT INTO ratings(anime_id, rate_value)
VALUES(4, 5.6);
INSERT INTO ratings(anime_id, rate_value)
VALUES(5, 8.42);
INSERT INTO ratings(anime_id, rate_value)
VALUES(6, 10);
select * from ratings;
