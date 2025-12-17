sudo mysql -u root -p

CREATE DATABASE satori;

USE satori;

CREATE TABLE paginas(
 	id INT PRIMARY KEY AUTO_INCREMENT,
  titulo VARCHAR(255),
  url VARCHAR(255),
  contenido TEXT
);

DROP TABLE paginas;

CREATE USER 
'satori'@'localhost' 
IDENTIFIED  BY 'Satori123$';

GRANT USAGE ON *.* TO 'satori'@'localhost';

ALTER USER 'satori'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON satori.* 
TO 'satori'@'localhost';

FLUSH PRIVILEGES;