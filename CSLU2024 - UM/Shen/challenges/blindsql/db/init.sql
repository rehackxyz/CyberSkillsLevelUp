CREATE DATABASE IF NOT EXISTS levelup;
USE levelup;

DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS toys;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS toys (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(100) NOT NULL
);

INSERT INTO users (username, password) VALUES ('admin', 'password_has_length_of_10_this_is_not_the_actual_password'); 

INSERT INTO toys (name, description) VALUES ('Red Robot', 'A big red robot');
INSERT INTO toys (name, description) VALUES ('Blue Robot', 'A small blue robot');
