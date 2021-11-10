COPY anime(anime_id,ani_name,genre,ani_type,episodes,rating,members)
FROM 'F:\DB introd data\animeTRY.csv'
DELIMITER ';'
CSV HEADER;
