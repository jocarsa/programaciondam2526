sudo mysql -u root -p

CREATE DATABASE camaron;
USE camaron;

CREATE TABLE viviendas (
    id INT UNSIGNED AUTO_INCREMENT,
    localidad VARCHAR(255),
    precio INT UNSIGNED,
    metroscuadrados DECIMAL(6,2),
    aniodeconstruccion YEAR,
    direccion VARCHAR(255),
    altura INT,
    tipodevivienda VARCHAR(255),
    descripcion TEXT,
    estado VARCHAR(255),
    banios INT,
    habitaciones INT,
    teniente VARCHAR(255),
    PRIMARY KEY (id)
);

CREATE TABLE imagenes (
    id INT UNSIGNED AUTO_INCREMENT,
    id_vivienda INT UNSIGNED,
    imagen VARCHAR(255),
    PRIMARY KEY (id),
    CONSTRAINT fk_imagenes_viviendas
        FOREIGN KEY (id_vivienda)
        REFERENCES viviendas(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);


CREATE USER 
'camaron'@'localhost' 
IDENTIFIED  BY 'Camaron123$';

GRANT USAGE ON *.* TO 'camaron'@'localhost';

ALTER USER 'camaron'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON camaron.* 
TO 'camaron'@'localhost';

FLUSH PRIVILEGES;


INSERT INTO viviendas 
(localidad, precio, metroscuadrados, aniodeconstruccion, direccion, altura, tipodevivienda, descripcion, estado, banios, habitaciones, teniente)
VALUES
('Valencia', 185000, 85.50, 1998, 'Calle Colón 12', 3, 'Piso',
 'Piso luminoso en el centro, cercano a transporte público y comercios.',
 'Buen estado', 1, 3, 'propietario'),

('Valencia', 320000, 120.00, 2010, 'Avenida del Puerto 45', 6, 'Ático',
 'Ático con terraza y vistas al mar, acabados modernos.',
 'Excelente', 2, 4, 'propietario'),

('Alboraya', 210000, 95.00, 2005, 'Carrer del Miracle 7', 2, 'Piso',
 'Vivienda familiar en zona tranquila, cerca de colegios.',
 'Buen estado', 2, 3, 'banco'),

('Torrent', 145000, 78.20, 1985, 'Calle San Vicente 33', 1, 'Piso',
 'Piso reformado recientemente, ideal para parejas.',
 'Reformado', 1, 2, 'propietario'),

('Gandía', 275000, 110.00, 2015, 'Paseo Marítimo 1', 4, 'Apartamento',
 'Apartamento en primera línea de playa.',
 'Excelente', 2, 3, 'propietario'),

('Sagunto', 165000, 90.00, 1992, 'Calle Mayor 18', 3, 'Piso',
 'Vivienda amplia en casco histórico.',
 'Buen estado', 1, 3, 'banco'),

('Paterna', 350000, 160.00, 2008, 'Urbanización La Cañada 22', 0, 'Chalet',
 'Chalet independiente con jardín y piscina.',
 'Excelente', 3, 4, 'propietario'),

('Burjassot', 130000, 70.00, 1978, 'Calle Cervantes 9', 4, 'Piso',
 'Piso económico, ideal como inversión.',
 'A reformar', 1, 2, 'propietario'),

('Xàtiva', 190000, 100.00, 2000, 'Avenida República Argentina 5', 2, 'Piso',
 'Piso espacioso con balcón.',
 'Buen estado', 2, 3, 'propietario'),

('Cullera', 420000, 140.00, 2018, 'Urbanización Cap Blanc 14', 7, 'Ático',
 'Ático de lujo con vistas panorámicas al mar.',
 'Excelente', 2, 4, 'propietario');
 
 
 
INSERT INTO imagenes (id_vivienda, imagen) VALUES
-- Vivienda 1
(1, 'vivienda1_img1.jpg'),
(1, 'vivienda1_img2.jpg'),
(1, 'vivienda1_img3.jpg'),

-- Vivienda 2
(2, 'vivienda2_img1.jpg'),
(2, 'vivienda2_img2.jpg'),
(2, 'vivienda2_img3.jpg'),
(2, 'vivienda2_img4.jpg'),

-- Vivienda 3
(3, 'vivienda3_img1.jpg'),
(3, 'vivienda3_img2.jpg'),
(3, 'vivienda3_img3.jpg'),

-- Vivienda 4
(4, 'vivienda4_img1.jpg'),
(4, 'vivienda4_img2.jpg'),

-- Vivienda 5
(5, 'vivienda5_img1.jpg'),
(5, 'vivienda5_img2.jpg'),
(5, 'vivienda5_img3.jpg'),
(5, 'vivienda5_img4.jpg'),

-- Vivienda 6
(6, 'vivienda6_img1.jpg'),
(6, 'vivienda6_img2.jpg'),

-- Vivienda 7
(7, 'vivienda7_img1.jpg'),
(7, 'vivienda7_img2.jpg'),
(7, 'vivienda7_img3.jpg'),
(7, 'vivienda7_img4.jpg'),
(7, 'vivienda7_img5.jpg'),

-- Vivienda 8
(8, 'vivienda8_img1.jpg'),
(8, 'vivienda8_img2.jpg'),

-- Vivienda 9
(9, 'vivienda9_img1.jpg'),
(9, 'vivienda9_img2.jpg'),
(9, 'vivienda9_img3.jpg'),

-- Vivienda 10
(10, 'vivienda10_img1.jpg'),
(10, 'vivienda10_img2.jpg'),
(10, 'vivienda10_img3.jpg'),
(10, 'vivienda10_img4.jpg');

SELECT v.id, v.localidad, COUNT(i.id) AS total_imagenes
FROM viviendas v
LEFT JOIN imagenes i ON v.id = i.id_vivienda
GROUP BY v.id;