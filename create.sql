
--creating tables according to 4NF

-- забула, що очищала файли, і 
--там дійсно одному аніме відповідає свій тим, 
--тож я перероблю ERD правильно у 4 лабораторній

CREATE TABLE types( --creating table_types: type_id, type_name
	type_id SERIAL PRIMARY KEY,
	type_name VARCHAR(50)
);

Create TABLE anime( -- creating main table anime: anime_id, anime_name, type_id(from types)
	anime_id SERIAL PRIMARY KEY,
	anime_name varchar,
	type_id INT NOT NULL REFERENCES types(type_id)
);

CREATE TABLE ratings( -- table ratings: anime_id(same id as anime_id from anime), rate_values(current rating), update_date(current date of update)
	anime_id INT NOT NULL REFERENCES anime(anime_id),
	rate_value FLOAT NOT NULL,
	update_date TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP
	--saves the time it was updated
);

CREATE TABLE episodes( -- table episodes: anime_id(same id as anime_id from anime)
	anime_id INT NOT NULL references anime(anime_id),
	episodes INT NOT NULL,
	members INT NOT NULL
);








