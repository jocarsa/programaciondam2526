-- =====================================================
-- AÑADIR DESCRIPCIÓN EXTENSA A PRODUCTOS
-- =====================================================

ALTER TABLE producto
ADD COLUMN descripcion_larga TEXT
AFTER descripcion;

-- =====================================================
-- ACTUALIZAR DESCRIPCIONES LARGAS DE PRODUCTO
-- =====================================================

UPDATE producto SET descripcion_larga =
'Portátil de 15 pulgadas diseñado para un uso intensivo tanto en entornos profesionales como educativos. Incorpora una pantalla amplia que permite trabajar cómodamente con documentos, hojas de cálculo y aplicaciones multitarea. Ideal para estudiantes, docentes y trabajadores que necesitan fiabilidad, buen rendimiento y una experiencia equilibrada entre potencia y portabilidad.'
WHERE id = 1;

UPDATE producto SET descripcion_larga =
'Ultrabook compacto y ligero con pantalla de 13 pulgadas, pensado para usuarios que se desplazan con frecuencia. Ofrece un alto rendimiento en un formato reducido, con arranque rápido, bajo consumo energético y un diseño elegante. Perfecto para profesionales que buscan movilidad sin renunciar a potencia.'
WHERE id = 2;

UPDATE producto SET descripcion_larga =
'Ordenador de sobremesa orientado a tareas de oficina, administración y uso doméstico avanzado. Su arquitectura permite una buena ventilación y futuras ampliaciones. Ideal para empresas, centros educativos o usuarios que necesitan estabilidad y rendimiento continuo durante largas jornadas.'
WHERE id = 3;

UPDATE producto SET descripcion_larga =
'Monitor Full HD de 24 pulgadas con excelente reproducción de color y amplio ángulo de visión. Adecuado para trabajo diario, programación, diseño básico y consumo multimedia. Su tamaño ofrece un equilibrio perfecto entre espacio de trabajo y comodidad visual.'
WHERE id = 4;

UPDATE producto SET descripcion_larga =
'Monitor QHD de 27 pulgadas pensado para usuarios exigentes que necesitan mayor resolución y espacio visual. Ideal para diseño gráfico, edición de vídeo, análisis de datos y multitarea avanzada. Proporciona una experiencia visual más nítida y detallada.'
WHERE id = 5;

UPDATE producto SET descripcion_larga =
'Teclado mecánico con retroiluminación, diseñado para ofrecer una pulsación precisa y duradera. Especialmente recomendado para programación, escritura intensiva y gaming. Su construcción robusta garantiza una larga vida útil incluso con uso intensivo.'
WHERE id = 6;

UPDATE producto SET descripcion_larga =
'Teclado inalámbrico silencioso y cómodo, ideal para entornos de oficina o estudio. Su diseño compacto y sin cables ayuda a mantener el escritorio ordenado. Perfecto para usuarios que buscan comodidad y discreción en el uso diario.'
WHERE id = 7;

UPDATE producto SET descripcion_larga =
'Ratón inalámbrico de alta precisión, fácil de instalar mediante receptor USB. Ofrece libertad de movimiento y ergonomía para un uso prolongado. Adecuado para tareas ofimáticas, navegación web y trabajo diario.'
WHERE id = 8;

UPDATE producto SET descripcion_larga =
'Ratón gaming con iluminación RGB y sensor de alta precisión. Diseñado para jugadores que requieren velocidad, exactitud y personalización. También es una excelente opción para diseñadores y usuarios avanzados.'
WHERE id = 9;

UPDATE producto SET descripcion_larga =
'Auriculares Bluetooth con micrófono integrado, pensados para llamadas, videoconferencias y consumo multimedia. Ofrecen libertad de movimiento y buena calidad de sonido, siendo una opción versátil tanto para trabajo como para ocio.'
WHERE id = 10;

UPDATE producto SET descripcion_larga =
'Auriculares gaming con sonido envolvente que permiten una experiencia inmersiva en videojuegos. Incorporan micrófono ajustable y diseño cómodo para largas sesiones. Recomendados para gamers y usuarios exigentes.'
WHERE id = 11;

UPDATE producto SET descripcion_larga =
'Cámara web HD ideal para videollamadas, clases online y reuniones profesionales. Ofrece imagen clara y configuración sencilla. Muy utilizada en entornos educativos y de teletrabajo.'
WHERE id = 12;

UPDATE producto SET descripcion_larga =
'Impresora láser monocromo orientada a oficinas y hogares con alto volumen de impresión. Destaca por su velocidad, bajo coste por página y fiabilidad. Ideal para documentos de texto y uso administrativo.'
WHERE id = 13;

UPDATE producto SET descripcion_larga =
'Unidad SSD de 1TB que mejora notablemente el rendimiento del sistema. Reduce los tiempos de arranque y carga de aplicaciones. Recomendado tanto para actualizar equipos antiguos como para configuraciones nuevas.'
WHERE id = 14;

UPDATE producto SET descripcion_larga =
'Disco duro mecánico de 2TB pensado para almacenamiento masivo de datos, copias de seguridad y archivos multimedia. Solución económica para grandes volúmenes de información.'
WHERE id = 15;

UPDATE producto SET descripcion_larga =
'Memoria USB de 64GB con conexión USB 3.0 para transferencias rápidas. Ideal para transportar documentos, proyectos y material multimedia de forma cómoda y segura.'
WHERE id = 16;

UPDATE producto SET descripcion_larga =
'Router WiFi de doble banda que garantiza una conexión estable y rápida en hogares y oficinas. Permite conectar múltiples dispositivos simultáneamente manteniendo un buen rendimiento.'
WHERE id = 17;

UPDATE producto SET descripcion_larga =
'Tablet Android de 10 pulgadas adecuada para consumo multimedia, navegación, educación y tareas ligeras. Su tamaño la hace cómoda para lectura, vídeo y aplicaciones educativas.'
WHERE id = 18;

UPDATE producto SET descripcion_larga =
'Smartphone con 128GB de almacenamiento interno, pensado para usuarios que necesitan espacio para aplicaciones, fotos y vídeos. Combina buen rendimiento con una experiencia fluida en el día a día.'
WHERE id = 19;

UPDATE producto SET descripcion_larga =
'Silla gaming ergonómica diseñada para largas sesiones frente al ordenador. Proporciona soporte lumbar, ajuste de altura y comodidad, siendo adecuada tanto para gaming como para trabajo de oficina.'
WHERE id = 20;
