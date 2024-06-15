CREATE TABLE users(
  id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(256) NOT NULL,
  password VARCHAR(256) NOT NULL
);

INSERT INTO users (username, password) VALUES ('admin', 'unguessable_dont_brute_this');
