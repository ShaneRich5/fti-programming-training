CREATE TABLE users
(
	id int NOT NULL IDENTITY(1,1) PRIMARY KEY,
	username varchar(30),
	first_name varchar(75),
	last_name varchar(100),
	email varchar(255),
	primary_address_id int FOREIGN KEY REFERENCES addresses(id),
);