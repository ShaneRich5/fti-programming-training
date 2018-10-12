CREATE TABLE addresses
(
	id int NOT NULL IDENTITY(1,1) PRIMARY KEY,
	street_address varchar(150),
	street_address_2 varchar(150),
	city varchar(150),
	state_id int FOREIGN KEY REFERENCES states(id),
	postal_code varchar(16)
);