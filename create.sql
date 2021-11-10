CREATE TABLE anime(
	id INT NOT NULL PRIMARY KEY,
	name VARCHAR(150),
	genre VARCHAR(200),
	type VARCHAR(50),
	episodes VARCHAR(10) NOT NULL,
	rating FLOAT,
	members INT NOT NULL
);


--creating tables according to 4NF
Create TABLE anime_general(
	id INT NOT NULL PRIMARY KEY REFERENCES anime_names(anime_id),
	type INT NOT NULL,
	members INT NOT NULL,
	rates FLOAT,
	episodes VARCHAR(10) NOT NULL,
	FOREIGN KEY (anime_type) REFERENCES anime_types(type_id)
)


CREATE TABLE anime_names(
	ani_name VARCHAR(150),
	anime_id INT NOT NULL primary key
);

CREATE TABLE anime_types(
	type_id SERIAL PRIMARY KEY,
	ani_type VARCHAR(50)
);
