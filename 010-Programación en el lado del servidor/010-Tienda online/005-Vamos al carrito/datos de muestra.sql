-- =====================================================
-- DATOS DE MUESTRA AMPLIADOS PARA TIENDA ONLINE
-- Orden correcto según claves foráneas
-- =====================================================

-- =====================
-- PRODUCTOS (20)
-- =====================
INSERT INTO producto VALUES
(1,  'Portátil 15"',              'Portátil para trabajo y estudio',                 '799.99', '25',  'portatil15.jpg'),
(2,  'Portátil 13"',              'Ultrabook ligero y potente',                      '999.99', '15',  'portatil13.jpg'),
(3,  'PC Sobremesa',              'Ordenador de sobremesa para oficina',             '699.00', '10',  'pc.jpg'),
(4,  'Monitor 24"',               'Monitor Full HD 24 pulgadas',                     '179.00', '40',  'monitor24.jpg'),
(5,  'Monitor 27"',               'Monitor QHD 27 pulgadas',                         '299.00', '30',  'monitor27.jpg'),
(6,  'Teclado mecánico',          'Teclado mecánico retroiluminado',                 '89.50',  '60',  'teclado_mec.jpg'),
(7,  'Teclado inalámbrico',       'Teclado inalámbrico silencioso',                  '39.90',  '100', 'teclado_wireless.jpg'),
(8,  'Ratón inalámbrico',         'Ratón óptico inalámbrico USB',                    '19.90',  '150', 'raton_wireless.jpg'),
(9,  'Ratón gaming',              'Ratón gaming RGB alta precisión',                '49.90',  '70',  'raton_gaming.jpg'),
(10, 'Auriculares Bluetooth',     'Auriculares inalámbricos con micrófono',          '59.99',  '80',  'auriculares_bt.jpg'),
(11, 'Auriculares gaming',        'Auriculares gaming con sonido envolvente',        '79.99',  '50',  'auriculares_gaming.jpg'),
(12, 'Webcam HD',                 'Cámara web HD para videollamadas',                '49.00',  '90',  'webcam.jpg'),
(13, 'Impresora láser',           'Impresora láser monocromo',                       '129.00', '20',  'impresora_laser.jpg'),
(14, 'Disco SSD 1TB',             'Disco sólido SSD 1TB SATA',                       '109.00', '75',  'ssd1tb.jpg'),
(15, 'Disco duro 2TB',            'Disco duro mecánico 2TB',                         '79.00',  '60',  'hdd2tb.jpg'),
(16, 'Memoria USB 64GB',          'Pendrive USB 3.0 64GB',                           '14.90',  '200', 'usb64.jpg'),
(17, 'Router WiFi',               'Router WiFi de doble banda',                      '69.00',  '45',  'router.jpg'),
(18, 'Tablet 10"',                'Tablet Android 10 pulgadas',                     '199.00', '35',  'tablet.jpg'),
(19, 'Smartphone 128GB',          'Teléfono móvil 128GB',                            '349.00', '55',  'smartphone.jpg'),
(20, 'Silla gaming',              'Silla ergonómica para escritorio',                '189.00', '25',  'silla_gaming.jpg');

-- =====================
-- CLIENTES (10)
-- =====================
INSERT INTO cliente VALUES
(1,  'Ana',     'Martínez López',   'ana.martinez@email.com',     'C/ Mayor 12, Madrid',          '600123456'),
(2,  'Carlos',  'Pérez Gómez',      'carlos.perez@email.com',    'Av. Libertad 45, Valencia',    '611234567'),
(3,  'Laura',   'Sánchez Ruiz',     'laura.sanchez@email.com',   'C/ del Mar 8, Alicante',       '622345678'),
(4,  'Javier',  'López Torres',     'javier.lopez@email.com',    'Gran Vía 101, Madrid',         '633456789'),
(5,  'Marta',   'Gómez Fernández',  'marta.gomez@email.com',     'C/ Colón 3, Castellón',       '644567890'),
(6,  'David',   'Ruiz Molina',      'david.ruiz@email.com',      'Av. Europa 22, Murcia',       '655678901'),
(7,  'Lucía',   'Navarro Pérez',    'lucia.navarro@email.com',   'C/ Serranos 7, Valencia',     '666789012'),
(8,  'Pablo',   'Hernández Gil',    'pablo.hernandez@email.com', 'C/ San Juan 19, Elche',       '677890123'),
(9,  'Sonia',   'Romero Díaz',      'sonia.romero@email.com',    'Av. Mediterráneo 5, Benidorm','688901234'),
(10, 'Alberto', 'Morales Cano',     'alberto.morales@email.com', 'C/ Alameda 14, Albacete',     '699012345');

-- =====================
-- PEDIDOS (15)
-- =====================
INSERT INTO pedido VALUES
(1,  '2025-12-01 10:15:00', 1),
(2,  '2025-12-01 18:40:00', 2),
(3,  '2025-12-02 09:05:00', 1),
(4,  '2025-12-02 21:30:00', 3),
(5,  '2025-12-03 11:00:00', 4),
(6,  '2025-12-03 16:20:00', 5),
(7,  '2025-12-04 12:10:00', 6),
(8,  '2025-12-04 19:45:00', 7),
(9,  '2025-12-05 08:50:00', 8),
(10, '2025-12-05 14:35:00', 9),
(11, '2025-12-06 10:05:00', 10),
(12, '2025-12-06 17:25:00', 2),
(13, '2025-12-07 09:40:00', 3),
(14, '2025-12-07 20:10:00', 6),
(15, '2025-12-08 13:55:00', 1);

-- =====================
-- LÍNEAS DE PEDIDO (30)
-- =====================
INSERT INTO lineaspedido VALUES
(1,  1,  '1',  1),
(2,  1,  '1',  8),
(3,  2,  '2', 10),
(4,  2,  '1',  4),
(5,  3,  '1',  6),
(6,  3,  '1', 14),
(7,  4,  '1', 18),
(8,  4,  '1',  9),
(9,  5,  '1',  2),
(10, 5,  '1',  7),
(11, 6,  '1', 20),
(12, 6,  '1',  5),
(13, 7,  '2', 16),
(14, 7,  '1', 12),
(15, 8,  '1', 11),
(16, 8,  '1',  9),
(17, 9,  '1', 19),
(18, 9,  '1', 17),
(19, 10, '1', 13),
(20, 10, '1', 15),
(21, 11, '1',  3),
(22, 11, '1', 14),
(23, 12, '2',  8),
(24, 12, '1',  6),
(25, 13, '1',  1),
(26, 13, '1', 10),
(27, 14, '1', 18),
(28, 14, '1', 16),
(29, 15, '1',  2),
(30, 15, '1',  4);
