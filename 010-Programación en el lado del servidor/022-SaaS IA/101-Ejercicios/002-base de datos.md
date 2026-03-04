sudo mysql -u root -p

CREATE DATABASE saasia;

USE saasia;

CREATE TABLE clientes (
    id INT(11) NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(255),
    apellidos VARCHAR(255),
    email VARCHAR(255),
    poblacion VARCHAR(255),
    fecha_de_nacimiento DATE,
    PRIMARY KEY (id)
);

INSERT INTO clientes (nombre, apellidos, email, poblacion, fecha_de_nacimiento) VALUES
('Carlos', 'Martínez López', 'carlos.martinez@email.com', 'Valencia', '1985-03-12'),
('Ana', 'Gómez Ruiz', 'ana.gomez@email.com', 'Madrid', '1990-07-25'),
('Luis', 'Fernández Torres', 'luis.fernandez@email.com', 'Sevilla', '1978-11-02'),
('Marta', 'Sánchez Díaz', 'marta.sanchez@email.com', 'Valencia', '1995-01-18'),
('Javier', 'Romero Gil', 'javier.romero@email.com', 'Barcelona', '1982-09-30'),
('Lucía', 'Navarro Pérez', 'lucia.navarro@email.com', 'Madrid', '2000-06-14'),
('David', 'Ortega Moreno', 'david.ortega@email.com', 'Sevilla', '1988-04-09'),
('Elena', 'Castro Jiménez', 'elena.castro@email.com', 'Valencia', '1992-12-21'),
('Pablo', 'Vega Herrera', 'pablo.vega@email.com', 'Barcelona', '1980-05-05'),
('Sara', 'Molina Ramos', 'sara.molina@email.com', 'Madrid', '1997-08-17'),
('Raúl', 'Delgado Serrano', 'raul.delgado@email.com', 'Valencia', '1983-02-11'),
('Laura', 'Iglesias Cano', 'laura.iglesias@email.com', 'Sevilla', '1991-10-27'),
('Miguel', 'Campos León', 'miguel.campos@email.com', 'Barcelona', '1975-07-03'),
('Cristina', 'Fuentes Vidal', 'cristina.fuentes@email.com', 'Madrid', '1989-03-29'),
('Alberto', 'Reyes Cortés', 'alberto.reyes@email.com', 'Valencia', '1993-11-15');

INSERT INTO clientes (nombre, apellidos, email, poblacion, fecha_de_nacimiento) VALUES
('Sergio', 'Blasco Núñez', 'sergio.blasco@email.com', 'Valencia', '1984-02-14'),
('Patricia', 'Calvo Molina', 'patricia.calvo@email.com', 'Madrid', '1996-09-21'),
('Iván', 'Soler Peña', 'ivan.soler@email.com', 'Sevilla', '1981-05-18'),
('Noelia', 'Prieto Lozano', 'noelia.prieto@email.com', 'Barcelona', '1998-12-03'),
('Adrián', 'Cabrera Ríos', 'adrian.cabrera@email.com', 'Málaga', '1993-04-27'),
('Beatriz', 'Hidalgo Crespo', 'beatriz.hidalgo@email.com', 'Zaragoza', '1987-07-09'),
('Óscar', 'Benítez Pastor', 'oscar.benitez@email.com', 'Valencia', '1979-11-30'),
('Rocío', 'Marín Esteban', 'rocio.marin@email.com', 'Madrid', '1994-06-11'),
('Hugo', 'Carmona Lara', 'hugo.carmona@email.com', 'Sevilla', '2001-01-05'),
('Clara', 'Santana Robles', 'clara.santana@email.com', 'Barcelona', '1986-08-22'),

('Andrés', 'Valero Nieto', 'andres.valero@email.com', 'Málaga', '1990-03-17'),
('Julia', 'Redondo Vega', 'julia.redondo@email.com', 'Zaragoza', '1999-10-10'),
('Mario', 'Gallego Pardo', 'mario.gallego@email.com', 'Valencia', '1982-05-02'),
('Alicia', 'Soto Carrasco', 'alicia.soto@email.com', 'Madrid', '1997-07-19'),
('Rubén', 'Rivas Fuentes', 'ruben.rivas@email.com', 'Sevilla', '1985-09-28'),
('Carmen', 'Bravo León', 'carmen.bravo@email.com', 'Barcelona', '1991-02-13'),
('Diego', 'Méndez Ortiz', 'diego.mendez@email.com', 'Málaga', '1977-12-24'),
('Nerea', 'Aguilar Serrano', 'nerea.aguilar@email.com', 'Zaragoza', '2000-04-01'),
('Víctor', 'Cortés Beltrán', 'victor.cortes@email.com', 'Valencia', '1988-06-16'),
('Paula', 'Escribano Reyes', 'paula.escribano@email.com', 'Madrid', '1995-03-08'),

('Fernando', 'Lorenzo Gil', 'fernando.lorenzo@email.com', 'Sevilla', '1983-11-12'),
('Miriam', 'Domingo Ruiz', 'miriam.domingo@email.com', 'Barcelona', '1992-01-29'),
('Gonzalo', 'Pascual Cano', 'gonzalo.pascual@email.com', 'Málaga', '1989-08-04'),
('Esther', 'Cuevas Navarro', 'esther.cuevas@email.com', 'Zaragoza', '1996-05-23'),
('Jaime', 'Olivares Mora', 'jaime.olivares@email.com', 'Valencia', '1976-09-15'),
('Silvia', 'Peinado Ramos', 'silvia.peinado@email.com', 'Madrid', '1993-12-19'),
('Samuel', 'Correa Ibáñez', 'samuel.correa@email.com', 'Sevilla', '1984-07-07'),
('Irene', 'Cardona Vidal', 'irene.cardona@email.com', 'Barcelona', '1998-10-30'),
('Álvaro', 'Montoya Crespo', 'alvaro.montoya@email.com', 'Málaga', '1991-06-02'),
('Teresa', 'Pérez Olmo', 'teresa.perez@email.com', 'Zaragoza', '1980-04-14'),

('Cristóbal', 'Durán Nieto', 'cristobal.duran@email.com', 'Valencia', '1987-03-03'),
('Verónica', 'Suárez León', 'veronica.suarez@email.com', 'Madrid', '1994-11-21'),
('Raquel', 'Padilla Torres', 'raquel.padilla@email.com', 'Sevilla', '1999-09-09'),
('Borja', 'Requena Pardo', 'borja.requena@email.com', 'Barcelona', '1985-01-26'),
('Lidia', 'Villanueva Cruz', 'lidia.villanueva@email.com', 'Málaga', '1992-08-18'),
('Tomás', 'Ferrer Lozano', 'tomas.ferrer@email.com', 'Zaragoza', '1978-02-07'),
('Ismael', 'Salinas Ortiz', 'ismael.salinas@email.com', 'Valencia', '1990-05-12'),
('Natalia', 'Caballero Ríos', 'natalia.caballero@email.com', 'Madrid', '1997-07-25'),
('Enrique', 'Cano Belmonte', 'enrique.cano@email.com', 'Sevilla', '1986-12-05'),
('Gloria', 'Varela Iglesias', 'gloria.varela@email.com', 'Barcelona', '1993-03-16'),

('Emilio', 'Mora Delgado', 'emilio.mora@email.com', 'Málaga', '1982-10-11'),
('Lorena', 'Franco Serra', 'lorena.franco@email.com', 'Zaragoza', '1995-06-28'),
('Guillermo', 'Santamaría Ruiz', 'guillermo.santamaria@email.com', 'Valencia', '1989-04-22'),
('Daniela', 'Arroyo Peña', 'daniela.arroyo@email.com', 'Madrid', '2001-02-15'),
('Manuel', 'Téllez Bravo', 'manuel.tellez@email.com', 'Sevilla', '1975-09-01'),
('Sofía', 'Cifuentes Marín', 'sofia.cifuentes@email.com', 'Barcelona', '1998-11-17'),
('Ricardo', 'Pons Herrera', 'ricardo.pons@email.com', 'Málaga', '1983-07-13'),
('Andrea', 'Alonso Gil', 'andrea.alonso@email.com', 'Zaragoza', '1996-01-31'),
('Marcos', 'Lara Benítez', 'marcos.lara@email.com', 'Valencia', '1988-05-20'),
('Elisa', 'Roldán Soto', 'elisa.roldan@email.com', 'Madrid', '1992-12-08');

SELECT * FROM clientes;
