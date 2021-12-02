CREATE TABLE anime(
	name VARCHAR(500),
	type VARCHAR(50),
	episodes INT,
	rating FLOAT NOT NULL,
	members INT
);


--creating tables according to 4NF

CREATE TABLE types(
	id SERIAL PRIMARY KEY,
	name VARCHAR(50)
);
Create TABLE information(
	id SERIAL PRIMARY KEY ,
	name varchar,
	type INT NOT NULL REFERENCES types(id)
);

CREATE TABLE rates(
	id INT NOT NULL REFERENCES information(id),
	value FLOAT NOT NULL
);


CREATE TABLE episodes(
	an_id INT NOT NULL references information(id),
	episodes INT NOT NULL,
	members INT NOT NULL
);


drop table anime;





