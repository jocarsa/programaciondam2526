CREATE DATABASE tiendaonlinedamdaw;
USE tiendaonlinedamdaw;

--aqui pegáis las tablas

CREATE USER 
'tiendaonlinedamdaw'@'localhost' 
IDENTIFIED  BY 'Tiendaonlinedamdaw123$';

GRANT USAGE ON *.* TO 'tiendaonlinedamdaw'@'localhost';

ALTER USER 'tiendaonlinedamdaw'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON tiendaonlinedamdaw.* 
TO 'tiendaonlinedamdaw'@'localhost';

FLUSH PRIVILEGES;